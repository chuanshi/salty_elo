"""
generates a tessdata dictionary file from db.pickle
"""

import pickle

db = pickle.load(open('db.pickle'))

word_list = []

for char in db.keys():
    for word in char.split(' '):
        if len(word) > 0:
            word_list.append(word)

with open('eng2.user-words', 'w') as f:
    f.writelines(("%s\n" % l for l in word_list))
