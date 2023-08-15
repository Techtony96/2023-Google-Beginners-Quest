# IMPORTS
from string import ascii_uppercase as ascii_upper
from string import ascii_lowercase as ascii_lower
from re import sub as sub


# CONFIG
cipher = 'Vhi Nixgnije tkplwr zu a tglpcltzasgtmu sldsxatlvisf czrhij. Ik ks e eoig sshhzutmuakgd zwrjkor gf kje Gsejcr gapygr, azitj uwws r uirylv uhmxt mclyw tf gngjygv tlw eevivw mvuseye. WNAK{yek_xikyy_nktl_at}'

TABLE = [ [0]*26 for i in range(26)]
for left in range(len(ascii_upper)):
    startIndex = left
    for top in range(len(ascii_upper)):
        TABLE[left][top] = ascii_upper[(startIndex + top) % 26]

# Strip out special characters from cipher
cipher_strip = sub("[^A-Za-z]", '', cipher).upper()
key = "CAESAR"
key = (key * len(cipher_strip))[0:len(cipher_strip)]
plainText=''


# SOLVE
for i in range(len(cipher_strip)):
    keyChar = key[i].upper()
    cipherChar = cipher_strip[i].upper()

    cipherIndex = ascii_upper.index(cipherChar)
    keyIndex = ascii_upper.index(keyChar)

    row = TABLE[keyIndex]
    plainTextindex = row.index(cipherChar)
    plainText += ascii_upper[plainTextindex]

# Print the result, with correct formatting    
for i in range(len(cipher)):
    cipherChar = cipher[i]
    if cipherChar.isalpha():
        if cipherChar.islower():
            print(plainText[0].lower(), end='')
        else:
            print(plainText[0], end='')
        plainText = plainText[1:]
    else:
        print(cipherChar, end='') 

