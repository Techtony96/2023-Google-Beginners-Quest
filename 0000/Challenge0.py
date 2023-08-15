# IMPORTS
from string import ascii_letters as ascii


# CONFIG
cipher = 'Naljnl, Pnrfne jnf n fxvyyrq pbzzhavpngbe, naq ur hfrq n inevrgl bs zrgubqf gb xrrc uvf zrffntrf frperg sebz uvf rarzvrf. Bar bs gurfr zrgubqf jnf gur Pnrfne pvcure, n fvzcyr grpuavdhr gb boshfpngr pbzzhavpngvbaf. SYNT{ebgngr_gung_nycunorg}'
ALPHABET = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'

# SETUP

# SOLVE
for i in range(0, len(ALPHABET), 2):
    result = ''
    for c in cipher:
        try :
            index = ALPHABET.index(c)
            result += ALPHABET[(index + i) % len(ALPHABET)]
        except:
            result += c

    if "FLAG{" in result.upper():
        print(result)
