import numpy as np
import math

EMBEDDINGS_NUM = 50

def read_embeddings(n=1000):
    # Reads n embeddings from file
    # Returns a dictionary where embedding[w] is the embeding of string w
    embedding = {}
    count = 0
#    For this program you need glove word emebeddings.
    with open('/<Word embeddings path>/glove.6B/glove.6B.50d.txt', encoding="utf8") as f:
        for line in f: 
            ls = line.split(" ")
            emb = [np.float32(x) for x in ls[1:]]
            embedding[ls[0]]=np.array(emb) 
            count+=1    
            if count>= n:
                break
    return embedding

def word_analogy(pair,w,options,emb):
    wa = 'embedings' # Add code to find the right wa

    uknown = embedding[w]

    known1 = embedding[pair[0]]
        
    known2 = embedding[pair[1]]
    
    desired_vector = uknown + known1 - known2
            
    min_distance_to_word = abs(embedding[options[0]] - desired_vector)
    current_index = 0
    for i in range(1, len(options)):
        opt_vector = embedding[options[i]]
        diff_with_desired_vector = abs(opt_vector - desired_vector)
        if sum(min_distance_to_word) > sum(diff_with_desired_vector):
            min_distance_to_word = diff_with_desired_vector
            current_index = i
    
    wa = options[current_index]
    S = '{} is to {} as {} is to {}'.format(pair[0],pair[1],w,wa)
    return S
    
if __name__ == "__main__":  
    vocabulary_size = 30000        
    embedding = read_embeddings(vocabulary_size)
    
    pair = ['france','paris']
    w = 'spain'
    options = ['washington','berlin','moscow','madrid']
    print(word_analogy(pair,w,options,embedding))
    
    pair = ['woman','queen']
    w = 'man'
    options = ['president','lord','minister','politician','king']
    print(word_analogy(pair,w,options,embedding))
    
    pair = ['princess','queen']
    w = 'prince'
    options = ['president','lord','minister','politician','king']
    print(word_analogy(pair,w,options,embedding))
    
    pair = ['algorithm','program']
    w = 'recipe'
    options = ['food','restaurant','taco','banana']
    print(word_analogy(pair,w,options,embedding))
    
    pair = ['cat','dog']
    w = 'tiger'
    options = ['lion','wolf','coyote','whale','dolphin']
    print(word_analogy(pair,w,options,embedding))
    
    pair = ['france','french']
    w = 'germany'
    options = ['spanish','english','russian','persian','german']
    print(word_analogy(pair,w,options,embedding))

    pair = ['child','person']
    w = 'colt'
    options = ['lion','wolf','coyote','whale','horse']
    print(word_analogy(pair,w,options,embedding))

    pair = ['old','new']
    w = 'fast'
    options = ['slow','planet','berlin','earth','king','german']
    print(word_analogy(pair,w,options,embedding))

    pair = ['toe','foot']
    w = 'finger'
    options = ['slow','planet','hand','earth','king','german']
    print(word_analogy(pair,w,options,embedding))

    pair = ['positive','negative']
    w = 'proton'
    options = ['neutron','electron','atom','molecule']
    print(word_analogy(pair,w,options,embedding))

'''
france is to paris as spain is to madrid
woman is to queen as man is to king
princess is to queen as prince is to king
algorithm is to program as recipe is to food
cat is to dog as tiger is to wolf
france is to french as germany is to german
child is to person as colt is to horse
old is to new as fast is to slow
toe is to foot as finger is to hand
positive is to negative as proton is to electron
'''
