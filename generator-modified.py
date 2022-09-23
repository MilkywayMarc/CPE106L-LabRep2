"""
Program: generator-modified.py
Author: Group 4
Generates and displays sentences using a simple grammar
and vocabulary.  Words are chosen at random.
"""

import random
import string

fileName = input("Enter the articles file name: ")
f = open(fileName, 'r')
articles = []
for line in f:
    stripped_line = line.strip()
    articles.append(stripped_line)
articles = tuple(articles)
print(articles)
f.close()

fileName1 = input("Enter the nouns file name: ")
g = open(fileName1, 'r')
nouns = []
for line in g:
    stripped_line = line.strip()
    nouns.append(stripped_line)
nouns = tuple(nouns)
g.close()

fileName2 = input("Enter the verbs file name: ")
h = open(fileName2, 'r')
verbs = []
for line in h:
    stripped_line = line.strip()
    verbs.append(stripped_line)
verbs = tuple(verbs)
h.close()

fileName3 = input("Enter the prepositions file name: ")
i = open(fileName3, 'r')
prepositions = []
for line in i:
  stripped_line = line.strip()
  prepositions.append(stripped_line)
prepoisitions = tuple(prepositions)
i.close()

def sentence():
    """Builds and returns a sentence."""
    return nounPhrase() + " " + verbPhrase()

def nounPhrase():
    """Builds and returns a noun phrase."""
    return random.choice(articles) + " " + random.choice(nouns)

def verbPhrase():
    """Builds and returns a verb phrase."""
    return random.choice(verbs) + " " + nounPhrase() + " " + \
           prepositionalPhrase()

def prepositionalPhrase():
    """Builds and returns a prepositional phrase."""
    return random.choice(prepositions) + " " + nounPhrase()

def main():
    """Allows the user to input the number of sentences
    to generate."""
    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence())

# The entry point for program execution
if __name__ == "__main__":
    main()

