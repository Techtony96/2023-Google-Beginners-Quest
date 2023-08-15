# IMPORTS
from string import ascii_uppercase as ascii_upper
from string import ascii_lowercase as ascii_lower
from re import sub as sub
import struct
import itertools


# CONFIG
cipher = 'rsâ£râ£enigmâ£â£aierheâ£iâ£gluucsclhetersntiâ£aâ£rlaâ£tâ£riayrgpetaiâ£diuâ£Fawhiho}sipatfyâ£ihrâ£aâ£rfaâ£pesâ£etohwreaâ£octtoneeâ£eihetTpxcdeghiâ£roâ£pedâ£yGaledemXToneepetlhtseghectnatanstâ£ripctiharaicsâ£foarsceeâ£ebrnâ£teâ£doemrrâ£c__ltcsaicsaâ£cooâ£wbrnâ£â£aranmeibti,haarhra,sipkltiâ£ci.ctstâ£aâ£lxtcnaenlkLeoakelXpohryâ£patakrntdâ£cilxsUâ£ineheâ£cwthersâ£rpoâ£narahhtrâ£aienlsrtrrâ£o.{rd___nXntiâ£â£ornrtoyrgoorsâ£te.ksipâ£â£crsâ£â£câ£pohelhgctnâ£ieâ£erntatecgâ£teeeAsuvesuX'

# Frequency: {'Â': 54, '\x90': 54, '£': 54, 'E': 44, 'R': 37, 'T': 36, 'A': 33, 'I': 27, 'S': 21, 'C': 21, 'N': 20, 'H': 20, 'O': 19, 'L': 14, 'P': 13, 'G': 9, 'D': 7, 'X': 7, 'U': 6, 'Y': 5, '_': 5, 'K': 5, 'M': 4, 'F': 4, 'W': 4, 'B': 3, '.': 3, ',': 2, '}': 1, '{': 1, 'V': 1}
key = 'CAESAR'
# TEST CASE
key = 'TOMATO'
cipher="ROFOACDTEDSEEEACWEIVRLENE"
columns = len(key)
# rows = int(len(cipher) / columns) + 1
rows = 6
table = [ [0]*columns for i in range(rows)]
lastRowCount = len(cipher) - (columns * (rows - 1))


def getKeySequence(key):
    key = key.upper()
    seq = [None] * len(key)
    count = 0
    for c in ascii_upper:
        if c in key:
            # key = key.replace(c, str(count))
            for index in [i for i in range(len(key)) if key[i] == c]:
                 seq[index] = count
            count+=1
    return seq

def getKeySequenceNoDuplicates(key):
    key = key.upper()
    seq = [None] * len(key)
    count = 0
    for c in ascii_upper:
        if c in key:
            # key = key.replace(c, str(count))
            for index in [i for i in range(len(key)) if key[i] == c]:
                seq[index] = count
                count+=1
    return seq

def getNextCipherCharacter():
    global cipher
    if len(cipher) == 0:
        return '?'
    c = cipher[0]
    cipher = cipher[1::]
    return c

def shouldPutSymbol(row, column):
    if row < rows-1:
        return True
    elif column+1 <= lastRowCount:
        return True
    return False

def shouldPutSymbol(row, column, seqNo):
    if column <= seqNo:
        return True
    else: 
        return False

sequence = getKeySequence(key)

# For comb approach


    
for seqNumber in range(0, max(sequence)+1):
    if sequence.count(seqNumber) > 1:
        # LEFT TO RIGHT
        for row in range(rows):
            for column in [i for i in range(columns) if sequence[i] == seqNumber]:
                if shouldPutSymbol(row, column, len(sequence) - 1 - sequence[::-1].index(seqNumber)):
                    table[row][column] = getNextCipherCharacter()
    else:
        # DOWN
        for row in range(rows):
            column = sequence.index(seqNumber)
            if shouldPutSymbol(row, column, len(sequence) - 1 - sequence[::-1].index(seqNumber)):
                table[row][column] = getNextCipherCharacter()

transmuted = ''
for row in table:
    for c in row:
        if c != 0:
            transmuted += c
print(transmuted)