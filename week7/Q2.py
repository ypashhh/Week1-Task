'''Write and test three functions that each take two words (strings) as parameters and
return sorted lists (as defined above) representing respectively:
Letters that appear in at least one of the two words.
Letters that appear in both words.
Letters that appear in either word, but not in both.
Hint: These could all be done programmatically, but consider carefully what topic we
have been discussing this week! Each function can be exactly one line'''
def list_return(w1, w2):
    word_1 = []
    for i in w1:
        word_1.append(i)
        
    word_2 = []
    for i in w2:
        word_2.append(i)
        
    return word_1, word_2    
    

def uni(w1, w2):
    word1, word2 = list_return(w1, w2)
    word1 = set(word1)
    word2 = set(word2)
    unon = set.union(word1, word2)
    unon = list(unon)
    unon.sort()
    return unon
def inter(w1, w2):
    word1, word2 = list_return(w1, w2)
    word1 = set(word1)
    word2 = set(word2)
    intern = set.intersection(word1, word2)
    intern = list(intern)
    intern.sort()
    return intern

def sym_diff(w1, w2):
    word1, word2 = list_return(w1, w2)
    word1 = set(word1)
    word2 = set(word2)
    diff = set.symmetric_difference(word1, word2)
    diff = list(diff)
    diff.sort()
    return diff

w1 = input("Enter a word: ")
w2 = input("Enter a word: ")

print(f"Union = {uni(w1, w2)}")
print(f"Intersection = {inter(w1, w2)}")
print(f"Symmetric Difference = {sym_diff(w1, w2)}")
