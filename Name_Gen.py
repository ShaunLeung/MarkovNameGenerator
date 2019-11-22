import Markov_Chain as mc
import pandas as pd 
import sys

pkmn = pd.read_csv("pkmn.csv")
pharma = pd.read_csv("pharma.csv")
philo = pd.read_csv("philo.csv")


db = list(pharma['name']) + list(pkmn['name']) + list(philo['name'])

for i in range(0,15):
    print(mc.generate(mc.build_markov_chain(db,3)))

