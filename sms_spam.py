import numpy as np
from textblob import TextBlob
import re


def word_frequency(bloblist):
    """Creates a dictionary of all the words that appear in the list
    and the number of times they appear"""
    a_dict = {}
    for blob in bloblist:
        xlist = [x for x in blob.words]
        for item in xlist:
            if item.lower() in a_dict:
                a_dict[item.lower()] += 1
            else:
                a_dict[item.lower()] = 1
    return a_dict


def top_dict(a_dict, num):
    """Returns the top 'num' most frequently appearing words"""
    sorted_list = sorted(a_dict.items(), key=lambda x: x[1], reverse=True)
    return sorted_list[0:num]


def main_function(bloblist, word1, word2):
    """Makes a list of lists.  Each list is a list of the 0/1 values
    for each feature"""
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
        lista.append([a, b, c, d, e, f, g, h, i, j, l1, l2, l3, l4, l5,
                      nc1, nc5, nc10, z])
    return lista


def findword(blobstring, word):
    """If the word is in the string, returns 1.  Otherwise returns 0."""
    if blobstring.find(word) == -1:
        return 0
    else:
        return 1


def startword(blobstring):
    """Checks to see if the string starts with word spam.  1 for spam,
    0 for ham."""
    if blobstring.starts_with('spam'):
        return 1
    else:
        return 0


def wordlength(blobstring, num1, num2):
    """Checks to see if the number of words in the string is between
    num1 and num2"""
    if num1 < len(blobstring.words) <= num2:
        return 1
    else:
        return 0


def numbercheck1(blobstring):
    """Checks to see if there's a number in the string"""
    astring = str(blobstring)
    if re.search(r"[0-9]{1}", astring):
        return 1
    else:
        return 0


def numbercheck5(blobstring):
    """Checks to see if there's 5 numbers in a row in the string"""
    astring = str(blobstring)
    if re.search(r"[0-9]{5}", astring):
        return 1
    else:
        return 0


def numbercheck10(blobstring):
    """Checks to see if there's 10 numbers in a row in the string"""
    astring = str(blobstring)
    if re.search(r"[0-9]{10}", astring):
        return 1
    else:
        return 0
