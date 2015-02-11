import numpy as np
from textblob import TextBlob
import re
from sklearn.feature_extraction.text import TfidfVectorizer as TfidV


def main_function(bloblist, word1, word2):
    lista = []
    for blobstring in bloblist:
        x = findword(blobstring.lower(), word1)
        y = findword(blobstring.lower(), word2)
        l1 = wordlength(blobstring, 0, 10)
        l2 = wordlength(blobstring, 10, 20)
        l3 = wordlength(blobstring, 20, 30)
        l4 = wordlength(blobstring, 30, 40)
        l5 = wordlength(blobstring, 40, 999999)
        nc1 = numbercheck(blobstring, 1)
        nc2 = numbercheck(blobstring, 2)
        nc3 = numbercheck(blobstring, 3)
        nc5 = numbercheck(blobstring, 5)
        nc10 = numbercheck(blobstring, 10)
        z = startword(blobstring)
        lista.append([x, y, l1, l2, l3, l4, l5, nc1, nc2, nc3, nc5, nc10, z])
    return lista


def findword(blobstring, word):
    if blobstring.find(word) == -1:
        return 0
    else:
        return 1

def startword(blobstring):
    if blobstring.starts_with('spam'):
        return 1
    else:
        return 0

def wordlength(blobstring, num1, num2):
    if num1 < len(blobstring.words) <= num2:
        return 1
    else:
        return 0

def numbercheck1(blobstring):
    astring = str(blobstring)
    if re.search(r"[0-9]{1}", astring):
        return 1
    else:
        return 0
