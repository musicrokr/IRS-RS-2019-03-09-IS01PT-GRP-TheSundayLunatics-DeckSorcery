#this file handle all the reading and writing of data files

import csv
import json
#cards will hold a list of class dictonary object 

cardJsonFile = "data/cards-in-use.json"
cardCsvFile = "data/cards-wild.csv"
cardLibraryCsvFile = "data/cards-library.csv"
cardStatsFile = "data/card-stats.json"
deckStatsFile = "data/deck-stats.json"

standardSet = ["GILNEAS", "BOOMSDAY", "TROLL", "CORE", "DALARAN"]
cards = []
cards2 = []
cardIdsLibrary = []
cardStats = {}
deckStats = {}
#data processing cards data
with open(cardJsonFile, "rb") as infile:
    #load from json file
    cards = json.load(infile)

with open(cardStatsFile, "rb") as infile:
    cardStats = json.load(infile)["series"]["data"]
   
with open(deckStatsFile, "rb") as infile:
    deckStats = json.load(infile)["series"]["data"]

with open(cardCsvFile,encoding ="ISO-8859-1") as infile:
    reader = csv.reader(infile, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True)
    cards2 = [r for r in reader]

with open(cardLibraryCsvFile,encoding ="ISO-8859-1") as infile:
    for line in infile:
        cardIdsLibrary = [int(l) for l in line.strip().split(",")]

rules = {}
heroClasses = ["DRUID", "HUNTER", "MAGE", "PALADIN", "PRIEST", "ROGUE", "SHAMAN", "WARLOCK", "WARRIOR"]
for hc in heroClasses:
    rules[hc] = {"HIGH": [], "LOW": [], "MEDIUM": []}
    with open("data/{0}-rule.csv".format(hc), 'r') as infile:
        for line in infile:
            results = line.strip().split(",")
            antecedent = [int(x) for x in results[0:len(results)-1]]
            consequence = results[len(results)-1]
            rules[hc][consequence].append(antecedent)
            

            

# validate card names from csv file match with json file
for card in cards2:
    result = [a for a in cards if a["name"] == card[0] and ("set" not in a or a["set"] != "HERO_SKINS")]
    if len(result) != 1:
        print("{0}: found {1}".format(card[0], len(result)))

myCardList = []
for card in cards:
    if "set" not in card or card["set"] == "HERO_SKINS" or card["set"] == "CORE" and card["type"] == "HERO" or "collectible" not in card or not card["collectible"]:
        continue

    cardId = card["dbfId"]
    name = card["name"]
    cardType = card["type"]
    cardRarity = card["rarity"]
    cardClass = card["cardClass"]
    cardRace = card["race"] if "race" in card else ""
    health = card["health"] if "health" in card else ""
    attack = card["attack"] if "attack" in card else ""
    cost = card["cost"] if "cost" in card else ""
    classSet = card["set"]
    durability = card["durability"] if "durability" in card else ""
    myCardList.append({
        "id": cardId,
        "name": name,
        "type": cardType,
        "rarity": cardRarity,
        "class": cardClass,
        "race": cardRace,
        "health": health,
        "attack": attack,
        "cost": cost,
        "set": classSet,
        "durability": durability
    })

cardDict = {c["id"]: c for c in myCardList}
races = {c["race"] for c in myCardList}
#print(races)

def getCardStats():
    return cardStats

def getDeckStats():
    return deckStats

def getAllCards():
    return myCardList

def getAvailableCardIdsForConstruction(heroClass): 
    return [c["id"] for c in myCardList if c["class"].lower() in [heroClass.lower(), "neutral"] and c["set"] in standardSet and c["id"] != 50477]

def getRarity(cardId):
    return cardDict[cardId]["rarity"]

def getCardName(cardId):
    return cardDict[cardId]["name"]

def getCardRace(cardId):
    return cardDict[cardId]["race"]

def getCardType(cardId):
    return cardDict[cardId]["type"]

def getCardClass(cardId):
    return cardDict[cardId]["class"]

def getCardRarity(cardId):
    return cardDict[cardId]["rarity"]

def getCardHealth(cardId):
    return int(cardDict[cardId]["health"]) 

def getCardAttack(cardId):
    return int(cardDict[cardId]["attack"])

def getCardCost(cardId):
    return int(cardDict[cardId]["cost"])

def getAllHeroClass():
    classes = [card['class'] for card in myCardList]
    return list(dict.fromkeys(classes))

def getCardsForHero(heroClass):
    cardsForHero=[card for card in myCardList if card['class'] == heroClass and card["set"] in standardSet]
    cardsForHero = sorted(cardsForHero, key=lambda x:(int(x["cost"]), x["name"]))
    print(cardsForHero)
    return cardsForHero

def getCardId(name):
    for c in myCardList:
        if c["name"] == name:
            return c["id"]
    
    print("notfound: {0}".format(name))

def getLibrary():
    result = [c for c in myCardList if c["id"] in cardIdsLibrary]
    result = sorted(result, key=lambda x : (x["class"],x["cost"],x["name"]))
    return [r["id"] for r in result]

def getAssociationRules(heroClass):
    return rules[heroClass]

def getLibraryCardIdsForConstruction(heroClass):
    return [c for c in cardIdsLibrary if getCardClass(int(c)) == heroClass or getCardClass(int(c)) == "NEUTRAL"]