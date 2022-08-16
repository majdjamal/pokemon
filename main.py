
""" A dimensionality reduction analysis of the pokemon dataset.
"""

__author__ = '__Majd Jamal__'

from DB_container.data_manager import PokemonDB
from ML_container.manifold_learning.models.isomap import Isomap
from ML_container.utils.utils import plotter

if __name__ == '__main__':
    print(
    """ 
    \033[0;33m
                                      ,'|
        _.----.        ____         ,'  _\   ___    ___     ____
    _,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.
    \      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |
     \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |
       \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |
        \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |
         \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |
          \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |
           \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |
            \_.-'       |__|    `-._ |              '-.|     '-.| |   |
                                    `'                            '-._|
    \033[0m                 
    """)

    print('Welcome to this Pokemon analysis!')

    data_obj = PokemonDB()

    data, columns = data_obj.ReadCSV()
    data_obj.InitializeDB()
    data_obj.Pandas2SQL(data)

    DATA_MTX, names, unique_type_1, unique_type_2 = data_obj.numpy()

    data_without_hp = DATA_MTX[:, [0, 2, 3, 4, 5, 6, 7]]
    isomap = Isomap()

    reduced_mtx = isomap.fit_transform(data_without_hp.T)

    plotter(DATA_MTX, reduced_mtx, None)#names)



