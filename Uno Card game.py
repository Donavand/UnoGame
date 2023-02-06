import random


def Builddeck():
    Deck = []
    colors = ["Blue", "Green", "Red", "Yellow"]
    values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "Draw Two", "Draw Four", "Skip", "Reverse"]
    wilds = ["Wild", "Wild Draw Four"]
    for color in colors:
        for value in values:
            cardval = "{} {}".format(color, value)
            Deck.append(cardval)

    for i in range(4):
        Deck.append(wilds[0])
        Deck.append(wilds[1])
    return Deck


def shuffleDeck(Deck):
    for cardPos in range(len(Deck)):
        randPos = random.randint(0, len(Deck) - 1)
        Deck[cardPos], Deck[randPos] = Deck[randPos], Deck[cardPos]
    return Deck


def drawCards(numCards):
    cardsDrawn = []
    for x in range(numCards):
        cardsDrawn.append(unoDeck.pop(0))
    return cardsDrawn


def ShowHand(player, playerHand):
    print("Player {}'s Turn".format((player + 1)))
    print("Your Hand")
    print("-------------")
    y = 1
    for card in playerHand:
        print("{}){}".format(y, card))
        y += 1
    print("")


def canPlay(color, value, playersHand):
    for card in playersHand:
        if "wild" in card:
            return True
        elif color in card or value in card:
            return True
    return False


unoDeck = Builddeck()
unoDeck = shuffleDeck(unoDeck)
discards = []
print(unoDeck)

players = []
colors = ["Blue", "Green", "Red", "Yellow"]
numplayers = int(input("How many players? "))
while numplayers < 2 or numplayers > 4:
    numplayers = int(input("invalid. Please enter a number between 2-4. How many player?"))
for player in range(numplayers):
    players.append(drawCards(5))

playerTurn = 0
playerDirection = 1
playing = True
discards.append(unoDeck.pop(0))
splitCard = discards[0].split()
currentcolor = splitCard[0]
if currentcolor != "Wild":
    cardval = splitCard[1]
else:
    cardval = "Any"

while playing:
    ShowHand(playerTurn, players[playerTurn])
    print("Card on the top of the discard pile:{}".format(discards[-1]))
    if canPlay(currentcolor, cardval, players[playerTurn]):
        cardchosen = int(input("Which card do you want to play?"))
    while not canPlay(currentcolor, cardval, players[playerTurn][cardchosen - 1]):
        cardchosen = int(input(" Not a valid card. Which card do you want to play?"))
        print("You played{}".format(players[playerTurn][cardchosen - 1]))
        discards.append(players[playerTurn].pop(cardchosen - 1))
    if len(players[playerTurn]) == 0:
        playing = False
        winner = "Player {}".format(playerTurn + 1)
    else:
        # checking for special cards
        splitCard = discards[-1].split("cardval")
    currentcolor = splitCard[0]
    if len(splitCard) == 1:
        cardval = "Any"
    else:
        cardval = splitCard[1]
    if currentcolor == "Wild":
        for x in range(len(colors)):
            print("{}){}".format(x + 1, colors[x]))
        newColor = int(input("What color would you like to choose? "))
        while newColor < 1 or newColor > 4:
            newColor = int(input(" Invalid option. What color would you like to choose? "))
        currentcolor = colors[newColor - 1]
    if cardval == "Reverse":
        playerDirection = playerDirection * -1
    elif cardval == "Skip":
        playerTurn += playerDirection
        if playerTurn >= numplayers:
            playerTurn = 0
        elif playerTurn < 0:
            playerTurn = numplayers - 1
    elif cardval == "Draw Two":
        playerTurn += playerDirection
        if playerTurn == numplayers:
            playerTurn = 0
        elif playerTurn < 0:
            playerTurn = numplayers - 1
        players[playerTurn].extend(drawCards(2))
    elif cardval == "Draw Four":
        if playerTurn == numplayers:
            playerTurn = 0
        elif playerTurn < 0:
            playerTurn = numplayers - 1
        players[playerTurn].extend(drawCards(4))
    else:
        print("You cant play. You have to draw card.")
        players[playerTurn].extend(drawCards(1))
        playerTurn += playerDirection
if playerTurn >= numplayers:
    playerTurn = 0
elif playerTurn < 0:
    playerTurn = numplayers - 1
print("Game Over")
print("{} is winner".format(winner))
