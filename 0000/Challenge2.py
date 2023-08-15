# IMPORTS
from string import ascii_uppercase as ascii_upper
from string import ascii_lowercase as ascii_lower
from re import sub as sub


# CONFIG
cipher = '''PDV KLRBC IOEXQ AEY TLGMF EJVO PDV NSWH ZEU.
PDRF PVYP RF S MSQUOSG, XDRBD GVSQF PDSP RP BEQPSRQF SNN 26 NVPPVOF EA PDV VQUNRFD SNMDSIVP. PDRF GSCVF RP RZVSN AEO AOVKLVQBH SQSNHFRF, SF PDV BOHMPSQSNHFP BSQ BEGMSOV PDV AOVKLVQBH EA NVPPVOF RQ PDV BRMDVOPVYP PE PDV CQEXQ AOVKLVQBH EA NVPPVOF RQ PDV VQUNRFD NSQULSUV.

AEO VYSGMNV, PDV GEFP BEGGEQ NVPPVO RQ PDV VQUNRFD NSQULSUV RF V. RA PDV GEFP BEGGEQ NVPPVO RQ PDV BRMDVOPVYP RF Y, PDVQ PDV BOHMPSQSNHFP BSQ SFFLGV PDSP Y RF NRCVNH PE IV S FLIFPRPLPREQ AEO V.

EPDVO BEGGEQ NVPPVOF RQ PDV VQUNRFD NSQULSUV RQBNLZV P, S, E, R, Q, F, SQZ D. PDV BOHMPSQSNHFP BSQ LFV PDRF RQAEOGSPREQ PE GSCV VZLBSPVZ ULVFFVF SIELP PDV EPDVO FLIFPRPLPREQF RQ PDV BRMDVOPVYP.

ANSU{QEX_RJV_NVSOQVZ_GH_SIBF}'''


# Key: Cipher
# Value: Plain Text
LOOKUP = {
    'A': 'F',
    'B': 'C',
    'C': 'K',
    'D': 'H',
    'E': 'O',
    'F': 'S',
    'G': 'M',
    'H': 'Y',
    'I': 'B',
    'J': 'V',
    'K': 'Q',
    'L': 'U',
    'M': 'P',
    'N': 'L',
    'O': 'R',
    'P': 'T',
    'Q': 'N',
    'R': 'I',
    'S': 'A',
    'T': 'J',
    'U': 'G',
    'V': 'E',
    'W': 'Z',
    'X': 'W',
    'Y': 'X',
    'Z': 'D',
}

# Frequency Analysis
frequency = {}
for c in ascii_upper:
    if c.isalpha():
        frequency[c] = 0

for c in cipher:
    if c.isalpha():
        frequency[c] += 1

print(dict(sorted(frequency.items(), key=lambda item: item[1], reverse=True)))


for c in cipher:
    try:
        if LOOKUP[c] != '':
            print(LOOKUP[c], end='')
        else:
            print('?', end='')
    except:
        print(c, end='')