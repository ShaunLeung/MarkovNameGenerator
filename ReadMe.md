# Markov Name Generator

## Overview
Using a Markov-Chain model constructed from three databases, pharma.csv, philo.csv and, pkmn.csv the program will generate a random name with influences from the previously
mentioned databases. 

The idea for this name generator arose from a simple game that host/streamer [Sean 'Day[9]' Plott](https://www.twitch.tv/day9tv) would play when they would see interesting online
handles while playing multiplayer games. The game was simply called "Pokemon, Philosopher, or Pharamceutical" and it was just to decided which of the three categories the name
fell under. 

## Markov Chain Model
The Markov Chain Model consists of three parts, starting entries, intermidiate entries and ending entries and can be adjusted to look at sub-strings of size k for each entry. The
model will process each word in the databases recording which k letters is starts with adding it to the starting list or incrementing the wieght if it has already recorded that
starting entry. The model will then look at the next character of the word and update the intermediate entry using the previous k characters as a key and record the character as 
a possible next letter in the values, if the character already exists as a next possible letter in the intermediate entry's values then the weighting will be increased. When the
model gets to the end of the word , words will be appended with the special character '\*', it will record that this is a possible ending and add it as an entry or increase the 
weighting like it did with the previous entries. 

When a name is being generated the model will randomly (weighted) select a starting point from the list of possible starting entries. It will then randomly select the next 
character from the list of possible next characters that the starting entry has. This will go on until the Model runs into an ending character '\*' at which point it will check if 
the name that was generated was unique and did not already exist in the databases. If the name is unique it will be returned, if not a new name will be generated.
