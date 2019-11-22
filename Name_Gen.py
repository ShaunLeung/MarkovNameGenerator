import Markov_Chain as mc
import pandas as pd 
import sys

pkmn = pd.read_csv("pkmn.csv")
pharma = pd.read_csv("pharma.csv")
philo = pd.read_csv("philo.csv")

db = list(filter(lambda x: x.isalpha() ,pharma['brand_name']))
db = list(map(lambda item: str(item[0]).upper() + str(item[1:]).lower(), db ))

for i in range(0,15):
    print(mc.generate(mc.build_markov_chain(db,3)))
