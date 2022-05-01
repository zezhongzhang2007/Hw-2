import numpy as np
import pandas as pd

pokemon_key = "Ivysaur"

empty_df = pd.DataFrame(np.array(['Bulbasaur', 'Grass', 'Poison', 318, 45, 49, 49, 65, 65, 45, 1, 'False',
                                  'Ivysaur', 'Grass', 'Poison', 405, 60, 62, 63, 80, 80, 60, 1, 'False',
                                  'Venusaur', 'Grass', 'Poison', 525, 80, 82, 83, 100, 100, 80, 1, 'False',
                                  'VenusaurMega Venusaur', 'Grass', 'Poison', 625, 80, 100, 123, 122, 120, 80, 1,
                                  'False',
                                  'Charmander', 'Fire', '', 309, 39, 52, 43, 60, 50, 65, 1, 'False']).reshape(5, 12),
                        index=[1, 2, 3, 4, 5],
                        columns=['Name', 'Type 1', 'Type 2', 'Total', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def',
                                 'Speed', 'Generation', 'Legendary'])
print(empty_df)
print(empty_df.loc[empty_df['Name'] == pokemon_key])
