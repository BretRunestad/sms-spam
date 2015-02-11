import numpy as np
from textblob import TextBlob
import re
from sklearn.feature_extraction.text import TfidfVectorizer as TfidV


def main_function(bloblist, word1, word2):
    lista = []
    for blobstring in bloblist:
        a = findword(blobstring.lower(), 'i')
        b = findword(blobstring.lower(), 'free')
        c = findword(blobstring.lower(), 'mobile')
        d = findword(blobstring.lower(), 'call')
        e = findword(blobstring.lower(), 'cash')
        f = findword(blobstring.lower(), 'cust')
        g = findword(blobstring.lower(), 'cash')
        h = findword(blobstring.lower(), 'stop')
        i = findword(blobstring.lower(), 'reply')
        j = findword(blobstring.lower(), 'txt')
        l1 = wordlength(blobstring, 0, 10)
        l2 = wordlength(blobstring, 10, 20)
        l3 = wordlength(blobstring, 20, 30)
        l4 = wordlength(blobstring, 30, 40)
        l5 = wordlength(blobstring, 40, 999999)
        nc1 = numbercheck1(blobstring)
        nc5 = numbercheck5(blobstring)
        nc10 = numbercheck10(blobstring)
        z = startword(blobstring)
        lista.append([a, b, c, d, e, f, g, h, i, j, l1, l2, l3, l4, l5, nc1, nc5, nc10, z])
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

def numbercheck5(blobstring):
    astring = str(blobstring)
    if re.search(r"[0-9]{5}", astring):
        return 1
    else:
        return 0

def numbercheck10(blobstring):
    astring = str(blobstring)
    if re.search(r"[0-9]{10}", astring):
        return 1
    else:
        return 0
