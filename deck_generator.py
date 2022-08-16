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
        for entry in jsonData:
            commanders.add(entry['categories'][0])
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

        halfdeckSize = {selectedCommanders[0]: 0, selectedCommanders[1]: 0}
        selectedCommanders.append('Common Cards')
        # Build Decklist
        with open('decklist.txt', 'w') as decklist:
            for card in jsonData:
                cardCategory = card['categories'][0]
                if cardCategory in selectedCommanders:
                    # Determine Color Identity
                    if card['card']['oracleCard']['name'].startswith(selectedCommanders[0]):
                        print(card['card']['oracleCard']['name'], end=' & ')
                        firstColour = card['card']['oracleCard']['colorIdentity'][0]
                    elif card['card']['oracleCard']['name'].startswith(selectedCommanders[1]):
                        print(card['card']['oracleCard']['name'])
                        secondColour = card['card']['oracleCard']['colorIdentity'][0]

                    # Halfdeck Size Increment
                    if cardCategory != 'Common Cards':
                        halfdeckSize[cardCategory] +=1

                    # Write Card to Decklist
                    cardOutput="%s %s %s"%(card['quantity'],card['card']['oracleCard']['name'], "#"+cardCategory)
                    decklist.write(cardOutput+'\n')

            # Add Basic Lands
            if firstColour != secondColour:
                firstTotal =  17 - (halfdeckSize[selectedCommanders[0]] - 30)
                if firstColour == 'White':
                    firstLand = 'Plains'
                elif firstColour == 'Blue':
                    firstLand = 'Island'
                elif firstColour == 'Black':
                    firstLand = 'Swamp'
                elif firstColour == 'Red':
                    firstLand = 'Mountain'
                elif firstColour == 'Green':
                    firstLand = 'Forest'

                landOutput="%s %s"%(firstTotal, firstLand)
                decklist.write(landOutput+'\n')
                
                secondTotal = 17 - (halfdeckSize[selectedCommanders[1]] - 30)
                if secondColour == 'White':
                    secondLand = 'Plains'
                elif secondColour == 'Blue':
                    secondLand = 'Island'
                elif secondColour == 'Black':
                    secondLand = 'Swamp'
                elif secondColour == 'Red':
                    secondLand = 'Mountain'
                elif secondColour == 'Green':
                    secondLand = 'Forest'
                
                landOutput="%s %s"%(secondTotal, secondLand)
                decklist.write(landOutput)
            else:
                combinedTotal = 34 - (halfdeckSize[selectedCommanders[0]] + halfdeckSize[selectedCommanders[1]] - 60)
                if firstColour == 'White':
                    basicLand = 'Plains'
                elif firstColour == 'Blue':
                    basicLand = 'Island'
                elif firstColour == 'Black':
                    basicLand = 'Swamp'
                elif firstColour == 'Red':
                    basicLand = 'Mountain'
                elif firstColour == 'Green':
                    basicLand = 'Forest'
                
                landOutput="%s %s"%(combinedTotal, basicLand)
                decklist.write(landOutput)


        