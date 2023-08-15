# IMPORTS
from string import ascii_uppercase as ascii_upper
from string import ascii_lowercase as ascii_lower
from re import sub as sub
import struct
import itertools


# CONFIG
cipher = 'rsâ£râ£enigmâ£â£aierheâ£iâ£gluucsclhetersntiâ£aâ£rlaâ£tâ£riayrgpetaiâ£diuâ£Fawhiho}sipatfyâ£ihrâ£aâ£rfaâ£pesâ£etohwreaâ£octtoneeâ£eihetTpxcdeghiâ£roâ£pedâ£yGaledemXToneepetlhtseghectnatanstâ£ripctiharaicsâ£foarsceeâ£ebrnâ£teâ£doemrrâ£c__ltcsaicsaâ£cooâ£wbrnâ£â£aranmeibti,haarhra,sipkltiâ£ci.ctstâ£aâ£lxtcnaenlkLeoakelXpohryâ£patakrntdâ£cilxsUâ£ineheâ£cwthersâ£rpoâ£narahhtrâ£aienlsrtrrâ£o.{rd___nXntiâ£â£ornrtoyrgoorsâ£te.ksipâ£â£crsâ£â£câ£pohelhgctnâ£ieâ£erntatecgâ£teeeAsuvesuX'
characters = ascii_upper
length = 8


# TEST CASE
#key = 'TOMATO'
#cipher="ROFOACDTEDSEEEACWEIVRLENE"

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

def shouldPutSymbol(row, column, rows, lastRowCount):
    if row < rows-1:
        return True
    elif column+1 <= lastRowCount:
        return True
    return False

def decrypt(key, cipher):
    columns = len(key)
    rows = int(len(cipher) / columns) + 1
    table = [ [0]*columns for i in range(rows)]
    lastRowCount = len(cipher) - (columns * (rows - 1))
    sequence = getKeySequence(key)
    for seqIndex in range(0, max(sequence)+1):
        if sequence.count(seqIndex) > 1:
            # LEFT TO RIGHT
            for row in range(rows):
                for column in [i for i in range(columns) if sequence[i] == seqIndex]:
                    if shouldPutSymbol(row, column, rows, lastRowCount):
                        table[row][column] = getNextCipherCharacter()
        else:
            # DOWN
            for row in range(rows):
                column = sequence.index(seqIndex)
                if shouldPutSymbol(row, column, rows, lastRowCount):
                    table[row][column] = getNextCipherCharacter()

    transmuted = ''
    for row in table:
        for c in row:
            if c != 0:
                transmuted += c
    return transmuted

print("Starting brute force...")
for password_length in range(1, length):
    for guess in itertools.product(characters, repeat=password_length):
        guess = ''.join(guess)
        print(f"Guessing {guess}...")
        cleartext = decrypt(guess, cipher)
        if "FLAG{" in cleartext.upper():
            print("FOUND!!")
            exit()

            

