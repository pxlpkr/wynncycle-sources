import requests
import json

WEIGHTS_URL = "https://athena.wynntils.com/cache/get/itemWeights"
URLS_URL = "https://raw.githubusercontent.com/Wynntils/Static-Storage/refs/heads/main/Data-Storage/urls.json"

WYNNCYCLE_WEIGHTS_URL = "https://raw.githubusercontent.com/pxlpkr/wynncycle-sources/refs/heads/main/public/item_weights.json"

def buildWeights():
    # EXTERNAL
    response = requests.get(WEIGHTS_URL)
    externalData = response.json()

    # INTERNAL
    with open('source/item_weight.json', 'r', encoding='utf-8') as file:
        internalData = json.load(file)

    # CONVERT
    externalData["wynncycle_weights"] = internalData

    # WRITE
    with open('public/item_weights.json', 'w+', encoding='utf-8') as file:
        json.dump(externalData, file)

def buildURLs():
    # EXTERNAL
    response = requests.get(URLS_URL)
    externalData = response.json()

    # CONVERT
    for obj in [i for i in externalData if "id" in i and i["id"] == "dataAthenaItemWeights"]:
        obj["url"] = WYNNCYCLE_WEIGHTS_URL

    # WRITE
    with open('public/urls.json', 'w+', encoding='utf-8') as file:
        json.dump(externalData, file)

if __name__ == "__main__":
    buildWeights()
    buildURLs()