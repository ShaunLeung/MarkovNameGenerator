import Markov_Chain as mc
import pandas as pd 
import sys

pkmn = pd.read_csv("pkmn.csv")
pharma = pd.read_csv("pharma.csv")
philo = pd.read_csv("philo.csv")

db = []
for entry in pharma['brand_name']:
    if entry.isalpha():
        db.append(entry)
db = list(dict.fromkeys(db))

newdb = []
for item in db:
    newdb.append( str(item[0]).upper() + str(item[1:]).lower() )

for i in range(0,15):
    print(mc.generate(mc.build_markov_chain(newdb,3)))