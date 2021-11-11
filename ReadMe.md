# Markov Name Generator
## Overview
By analysing 3 seperate databases of Pokemon names, pharmaceuticals and ancient philosophers the program will generate a random name based on the structure of the analysed data.

I wanted to get some practice with AI programing, and I was also about to start a new DnD campaign and thought I could combine the two. The subject matter for the names came from Twitch Streamer Sean "Day 9" Plott, who would posit the question "Pokemon, pharmaceutical, or philosopher" whenever he would enounter an unusual name when playing online games. 

I chose to write the program in Python because dictionaries make organizing the seperate links of the Markov chain much clearer since looking up objects is simpler in Python as compared to a language like C. Python also requires fewer includes, with built in CSV parsing the only module I needed to include was Random so that each link of the chain could be randomly selected. 

## How it Works
### Name Generator
This file merges the raw databases into a single object containing all the names to be parsed. The number of names to be generated can be controlled by changing the i value of the for loop. The program will then print the randomized names to the console. 

### Markov Chain logic 
#### build_markov_chain(data, n)
This function sets up the main dictionary that will be used to build the randomly generated names. It requires two parameters, data, and n. Data is the long list of names that will be parsed to create the chain and n is the number of characters that will be considered when parsing. For example if n was 3 the word apple would broken down into app-ppl-ple-le-e. If n was 2 it would be ap-pp-pl-le-e. The lower the n value the more "random" the names will be since they will have less context. 

The first thing this function does is to initialize the chain object which is composed of two objects. The first object is called \_initial which contains all the possible starting points for generated names. It is essentially just a list of the first n characters of each word in data. The second object in chain is \_names which contains all the names for the the data that was passed in, this can be used to cross check if you accidently generated a name that was part of the data.   

The function then adds a special chracter, in this instance \*, to the end of of each word in data. This allows the program to randomly select an endpoint from the the chain instead of just constantly adding links infinitly. 

The next part of the funtion splits the word and parses each length n section of the word. It is broken down into section being looked at and the next link in the chain. We don't have to worry about going out of bounds since the loop to only loops at the length of the word - n.

```
tuple = word_wrapped[i:i + n]
next = word_wrapped[i + 1:i + n + 1]
```

The sections are then added to the chain and weights are either started or increased. 

Finally the function returns the chain which now contains all the information needed to start generating some random names. 

#### select_random_item(items)
This function simply selects a random item from a list, taking in account weighting with heavier weighted items being picked more frequently than lighter items. 
The first thing it does is that it selects a random number between 0 and the total sum of all item weights. From there it goes through the list of items and subtracts the items' weight from the sum. If the weight of the item reduces the sum to or below 0 the item is chosen. This means that items with a larger weight will take a bigger chunk off of the sum and have a greater chance of being selected. 

```
def select_random_item(items):
    rnd = random.random() * sum(items.values())
    for item in items:
        rnd -= items[item]
        if rnd < 0:
            return item 
```

#### generate(chain)
The parameter for this function is the completed chain from build_markov_chain. This contains all the information needed to generate a random name. 

This is the function that builds the randomly generated name, chaining from each section to the next until it encounters an \*. Finally the function check the list of names that was used to build the chain and if it turns out that if the generated name was one that already existed it will recursively get a new name and return that.
