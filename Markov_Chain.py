import random

def build_markov_chain(data, n):
    chain = {
        '_initial':{},
        '_names': set(data)
    }
    for word in data:
        #Append a special character to denote the last char of a word
        word_wrapped = str(word) + '*'

        for i in range(0, len(word_wrapped) - n):
            #isolate each n char long frame in the word and next frame
            tuple = word_wrapped[i:i + n]
            next = word_wrapped[i + 1:i + n + 1]
            
            #start new entry or update existing entry for the particualr frame
            if tuple not in chain:
                entry = chain[tuple] = {}
            else:
                entry = chain[tuple]
            
            #Adding the strart of this word as a possible start for a chain
            #Adding the frame to the chain or increasing the weight of the 
            #frame in the chain
            if i == 0:
                if tuple not in chain['_initial']:
                    chain['_initial'][tuple] = 1
                else:
                    chain['_initial'][tuple] += 1
                    
            #Adding or increasing the weight of the next link of the frame
            if next not in entry:
                entry[next] = 1
            else:
                entry[next] += 1

    return chain 

#Okay this part is a little weird.
#It works by getting a sum of all the weighting and then multiplying it by a 
#random number between 0-1 so our next random frame will be one in the next list
#from there it goes item by item subtracting the next link weighting from the 
#random starting point until it is less than 0 which means we found the next
#item to return 
def select_random_item(items):
    rnd = random.random() * sum(items.values())
    for item in items:
        rnd -= items[item]
        if rnd < 0:
            return item 

def generate(chain):
    #Grab an initial starting point
    tuple = select_random_item(chain['_initial'])
    result = [tuple]
    
    while True:
        #Grab the next link
        tuple = select_random_item(chain[tuple])

        #Stop if you are at an end
        last_character = tuple[-1]
        if last_character == '*':
            break

        #Add the char to the generated name
        result.append(last_character)
    
    #Stitch the generated name together to make a string
    generated = ''.join(result)

    #We don't want names that were in our DB
    if generated not in chain['_names']:
        return generated
    else:
        return generate(chain)

