## Coded by Lucas-Faiad

import Loto_facil
import Mega_sena
loteria = str(input("Qual loteria voce deseja aposta?\n(1)Mega sena (2)Loto Facil")).lower()
if loteria == "1" or loteria == "mega sena":
    Mega_sena.Mega()
elif loteria == "2" or loteria == "loto facil":
    Loto_facil.Loto()