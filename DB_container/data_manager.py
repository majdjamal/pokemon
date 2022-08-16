""" Makes a database object of a csv file.
"""

import pandas as pd
import numpy as np
import sqlite3
from collections import Counter

__author__ = 'Majd Jamal'

class PokemonDB:

    def __init__(self):

        self.csv_file_name = 'Pokemon.csv'
        self.database_name = 'pokemon_dataset'

    def ReadCSV(self) -> pd.DataFrame:
        """ Read CSV file and convert it to a Pandas Dataframe
        """
        pokemons = pd.read_csv(f'DB_container/{self.csv_file_name}')
        csv_columns = list(pokemons.columns)

        return pokemons, csv_columns

    def InitializeDB(self) -> None:
        """ Initialize databse with SQLlite3 and saves it as a .db file.
        """
        connect_to_db = sqlite3.connect(f'DB_container/{self.database_name}')
        db = connect_to_db.cursor()

        if 'pokemon' in self.database_name:
            query = f'CREATE TABLE IF NOT EXISTS pokemons (id INTEGER PRIMARY KEY, name TEXT, type_1 TEXT, type_2 TEXT, total INTEGER, hp INTEGER, attack INTEGER, defense INTEGER, sp_atk INTEGER, sp_def INTEGER, speed INTEGER, generation INTEGER, legendary BOOLEAN)'

        db.execute(query)
        connect_to_db.commit()

    def Retrieve(self) -> list:
        """ Helper function to retrieve all data points from the pokemon SQL table
        """

        connect_to_db = sqlite3.connect(f'DB_container/{self.database_name}')
        db = connect_to_db.cursor()

        if 'pokemon' in self.database_name:
            query = ''' SELECT * FROM pokemons '''

        db.execute(query)

        db_rows = []

        for row in db.fetchall():
            db_rows.append(row)

        return db_rows

    def Pandas2SQL(self, data) -> None:
        """
            Uses data stored in a Pandas format and convert its format to a SQL database.

        :param data: CSV file represented in a Pandas format
        """
        connect_to_db = sqlite3.connect(f'DB_container/{self.database_name}')
        data.to_sql('DB_container/pokemons', connect_to_db, if_exists='replace', index=False)

    def numpy(self) -> np.ndarray:
        """ Generates a numpy dataset of the SQL pokemon table.

        :returns DATA_MTX: Matrix of pokemon data points, shape = (Npts, Nclmns - 2), where - 2 to remove id and pokemon name attribute
        :returns names: Dictionary mapping between ID and pokemon name
        :returns unique_type_1: Unique type 1, where the position of the type corresponds to the integer in the DATA_MTX.
            For example, if pikachu is stored at index 10 in the names dictionary, then the pikachu card type is unique_type_1[10] = Electric
        :returns unique_type_2: Unique type 2, where the position of the type corresponds to the integer in the DATA_MTX
        """
        db_rows = self.Retrieve()

        Npts = len(db_rows)
        Nclmn = len(db_rows[0])

        DATA_MTX = np.zeros((Npts, Nclmn - 2))

        names = {}

        type_1 = []
        type_2 = []

        for row in db_rows:

            type_1.append(row[2])
            type_2.append(row[3])

        unique_type_1 = list(Counter(type_1).keys())
        unique_type_2 = list(Counter(type_2).keys())

        for ind, row in enumerate(db_rows):

            numpy_representation_of_row = np.zeros(Nclmn - 2)   # Removing the ID and name attribute

            numpy_representation_of_row[0] = unique_type_1.index(row[2])    # type_1
            numpy_representation_of_row[1] = unique_type_2.index(row[3])    # type_2

            numpy_representation_of_row[2:] = row[4:]   # Attack, Defence, etc.

            DATA_MTX[ind] = numpy_representation_of_row

            names[ind + 1] = row[1] # ID to Name dictionary

        return DATA_MTX, names, unique_type_1, unique_type_2

if __name__ == '__main__':

    data_obj = PokemonDB()

    data, columns = data_obj.ReadCSV()

    data_obj.InitializeDB()

    DATA_MTX = data_obj.numpy()






