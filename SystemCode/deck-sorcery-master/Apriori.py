from DataProvider import *
from apyori import apriori
from sklearn.preprocessing import KBinsDiscretizer
import time

heroClasses = ["DRUID", "HUNTER", "MAGE", "PALADIN", "PRIEST", "ROGUE", "SHAMAN", "WARLOCK", "WARRIOR"]
deckStats = getDeckStats()

rules = []
start = time.time()

for hc in heroClasses:
    print("starting for class: {0}".format(hc))
    decks = []
    wr = []
    for deck in deckStats[hc]:
        cardArrays = [str(cardId) for cardId, count in json.loads(deck["deck_list"])]
        #cardArrays = [str(item) for sublist in cardArrays for item in sublist]
        decks.append([hc] + cardArrays + [str(deck["win_rate"])])
        wr.append([deck["win_rate"]])

    est = KBinsDiscretizer(n_bins=3, encode="ordinal").fit(wr)
    twr = est.transform(wr)

    actualDecks = []
    writeData = []
    writeDataPretty = []
    for d,w in zip(decks, twr):
        wrGroup = list(w)[0]
        #print(wrGroup)
        hc = d[0]
        mapping = {0:"LOW", 1:"MEDIUM", 2:"HIGH"}
        theDeck = d[1:len(d)-1] + [mapping[wrGroup]]
        #print(theDeck)
        actualDecks.append(theDeck)
        writeData.append(d[1:] + [mapping[wrGroup]])
        writeDataPretty.append([getCardName(int(c)) for c in d[1:len(d)-1]] + [d[len(d)-1]] + [mapping[wrGroup]])

    #with open("data/{0}-data.csv".format(hc), "w") as outfile:
    #    for wd in writeData:
    #        outfile.write(",".join(wd)+"\n")

    #with open("data/{0}-data-withname.csv".format(hc), "w") as outfile:
    #    for wd in writeDataPretty:
    #        outfile.write(",".join(wd)+"\n")

    association_rules = apriori(actualDecks, min_support=0.25, min_confidence=0.1, min_lift=1, min_length=2)
    association_results = list(association_rules)

    classRulesPretty = []
    classRules = []
    for items, support, orderStats in association_results:
        #print("items: {0}, support: {1}, orderStats: {2}".format(items,support,orderStats))
        for ibase, iadd, confidence, lift in orderStats:
            #if len(iadd) == 1:
            #   print(next(iter(iadd)))
            if len(ibase) > 0 and len(iadd) == 1 and next(iter(iadd)) in ["VERY LOW", "LOW", "MEDIUM", "HIGH", "VERY HIGH"]:
                rules.append(([a for a in ibase], next(iter(iadd))))
                classRules.append([a for a in ibase] + [next(iter(iadd))])
                classRulesPretty.append([getCardName(int(a)) for a in ibase] + [next(iter(iadd))])

    with open("data/{0}-rule.csv".format(hc), "w") as outfile:
        for wd in classRules:
            outfile.write(",".join(wd) + "\n")
    #with open("data/{0}-rule-withname.csv".format(hc), "w") as outfile:
    #    for wd in classRulesPretty:
    #        outfile.write(",".join(wd) + "\n")
    print("completed class: {0}".format(hc))
    print("{0} rules found".format(len(association_results)))
    print("interested rules: {0}".format(len(classRules)))

end = time.time()
for x in rules:
    print(x)

print("{0}s elapsed".format(end-start))
print("all interested rules: {0}".format(len(rules)))
