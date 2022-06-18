import string
import random
import sys
from nltk.corpus import wordnet as wn


help_dict = {"fruit": ["apple", "blueberry"], "animal": ["dog", "horse", "shark"]}

def cleaner(text):
    res = text.split('.')
    return res[0]

def check_hypo(synset, category):
    for example in help_dict[category]:
        if wn.synsets(example)[0] in synset.hyponyms():
            return True
    return False

def pick_hypo(synset, letter):
    result = []
    for hypo in synset.hyponyms():
        name = hypo.lemma_names('eng')[0]
        if name[0].upper() == letter:
            result.append(name)
    return result
        
CAT = ["fruit"]

asking_cat = random.choice(CAT)
asking_letter = random.choice(string.ascii_uppercase)

category_synset = wn.synsets(asking_cat)[0]
not_found = True
system_answer = []

for hypo in category_synset.hyponyms():
    if check_hypo(hypo, asking_cat) and not_found:
        system_answer = pick_hypo(hypo, asking_letter)
        if system_answer != []:
            not_found = False

if system_answer != []:
    print(f"The {asking_cat} that starts with letter {asking_letter} is: {random.choice(system_answer)}")
else:
    print(f"There is no {asking_cat} that starts with letter {asking_letter}")





'''answer = input(f"Hello! Pick a {asking_cat} that starts with letter {asking_letter}: ")


if wn.synsets(answer) != None:
    full_hypo = set([i for i in category_synset.closure(lambda s:s.hyponyms())])
    
    if wn.synsets(answer)[0] in full_hypo:
        print("Good Answer")
    else:
        print("No good")
else:
    print("No good")'''