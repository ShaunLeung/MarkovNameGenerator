import random

def build_markov_chain(data, n):
    chain = {
        '_initial':{},
        '_names': set(data)
    }
    for word in data:
        word_wrapped = str(word) + '*'
        for i in range(0, len(word_wrapped) - n):
            tuple = word_wrapped[i:i + n]
            next = word_wrapped[i + 1:i + n + 1]
            
            if tuple not in chain:
                entry = chain[tuple] = {}
            else:
                entry = chain[tuple]
            
            if i == 0:
                if tuple not in chain['_initial']:
                    chain['_initial'][tuple] = 1
                else:
                    chain['_initial'][tuple] += 1
                    
            if next not in entry:
                entry[next] = 1
            else:
                entry[next] += 1
    return chain 

def select_random_item(items):
    rnd = random.random() * sum(items.values())
    for item in items:
        rnd -= items[item]
        if rnd < 0:
            return item 

def generate(chain):
    tuple = select_random_item(chain['_initial'])
    result = [tuple]
    
    while True:
        tuple = select_random_item(chain[tuple])
        last_character = tuple[-1]
        if last_character == '*':
            break
        result.append(last_character)
    
    generated = ''.join(result)
    if generated not in chain['_names']:
        return generated
    else:
        return generate(chain)

