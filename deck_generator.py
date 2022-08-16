import requests
import json
import random
import sys

# Query
response = requests.get("https://archidekt.com/api/decks/2098253/")

# Update Halfdecks
json_object = json.dumps(response.json(), sort_keys=True, indent=4)
with open('halfdecks.json', 'w') as outfile:
    outfile.write(json_object)

# Partner Arguments
firstPartner = '';
if len(sys.argv) > 1:
    firstPartner = sys.argv[1].capitalize()
secondPartner = '';
if len(sys.argv) > 2:
    secondPartner = sys.argv[2].capitalize()

commanders = {'Common Cards', 'Commander'}
with open('halfdecks.json') as jsonFile:
        data = json.load(jsonFile)
        jsonData = data['cards']

        # Find Commander Options
        for card in jsonData:
            commanders.add(card['categories'][0])
        commanders.remove('Common Cards')
        commanders.remove('Commander')

        # Select Commanders
        selectedCommanders = [];
        if firstPartner and commanders.__contains__(firstPartner.capitalize()):
            if secondPartner and commanders.__contains__(secondPartner.capitalize()):
                selectedCommanders = [firstPartner, secondPartner]
            else:
                selectedCommanders.append(firstPartner)
                commanders.remove(firstPartner)
                selectedCommanders.append(random.sample(commanders, 1)[0])
        else:
            selectedCommanders = random.sample(commanders, 2)
        
        print(selectedCommanders)

        selectedCommanders.append('Common Cards')
        # Build Decklist
        with open('decklist.txt', 'w') as decklist:
            for card in jsonData:
                if card['categories'][0] in selectedCommanders:
                    cardOutput="%s %s %s"%(card['quantity'],card['card']['oracleCard']['name'], "#"+card['categories'][0])
                    decklist.write(cardOutput+'\n')