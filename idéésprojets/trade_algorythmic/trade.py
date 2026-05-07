import random
import time
from pathlib import Path
import json

start_time = time.time()

dossier_parent = Path(__file__).parent
ch_fichier_json_trade = dossier_parent / "trade.json"

with open(ch_fichier_json_trade, "r") as fichier_ouvert:
    DB_trade_json = json.load(fichier_ouvert)
    bitcoin_value = DB_trade_json["bitcoin value"]


def algorythme_crypto(valeur_of_crypto):
    pourcentage_de_changement = random.randint(65, 100)
    valeur_de_changement = valeur_of_crypto / pourcentage_de_changement

    augmenter_ou_baisser = random.randint(1, 2)
    if augmenter_ou_baisser == 1:
        valeur_of_crypto += valeur_de_changement
    elif augmenter_ou_baisser == 2:
        valeur_of_crypto -= valeur_de_changement

    return valeur_of_crypto


for _ in range(100000):
    bitcoin_value = algorythme_crypto(bitcoin_value)
    print(f"{bitcoin_value} $")
