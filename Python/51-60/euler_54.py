import time
startTime = time.clock()
ranks = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
handsFile = open('C:\Users\Aidan\Desktop\p054_poker.txt', 'r')
hands = [sorted(i.split(" ")[0:5], key=lambda k: ranks[k[0]], reverse=True) + sorted(i.split(" ")[5:10], key=lambda k: ranks[k[0]], reverse=True) for i in handsFile.read().split("\n")]
playerOneWins = 0

def highCard(hand, player):
    card = 0
    while ranks[hands[hand][card][0]] == ranks[hands[hand][card + 5][0]]:
        card += 1
    return ranks[hands[hand][card][0]] if player == 1 else ranks[hands[hand][card + 5][0]]

def onePair(hand, player):
    card = 0
    while card < 4:
        if ranks[hands[hand][card + ((player - 1) * 5)][0]] == ranks[hands[hand][card + 1 + ((player - 1) * 5)][0]]:
            return ranks[hands[hand][card + ((player - 1) * 5)][0]]
        card += 1
    return 0

def twoPair(hand, player):
    card = 0
    pairs = []
    while card < 4:
        if ranks[hands[hand][card + ((player - 1) * 5)][0]] == ranks[hands[hand][card + 1 + ((player - 1) * 5)][0]]:
            pairs.append(ranks[hands[hand][card + ((player - 1) * 5)][0]])
        card += 1
    if len(pairs) == 2 and not pairs[0] == pairs[1]:
        return pairs
    return 0
    
def threeKind(hand, player):
    card = 0
    while card < 3:
        if ranks[hands[hand][card + ((player - 1) * 5)][0]] == ranks[hands[hand][card + 1 + ((player - 1) * 5)][0]] == ranks[hands[hand][card + 2 +((player - 1) * 5)][0]]:
            return ranks[hands[hand][card + ((player - 1) * 5)][0]]
        card += 1
    return 0

def straight(hand, player):
    highCard = ranks[hands[hand][((player - 1) * 5)][0]]
    card = 1
    while card < 5:
        if ranks[hands[hand][((player - 1) * 5 + card)][0]] + card != highCard:
            return 0
        card += 1
    return ranks[hands[hand][((player - 1) * 5)][0]]

def flush(hand, player):
    card = 1
    suit = hands[hand][((player - 1) * 5)][1]
    while card < 5:
        if hands[hand][((player - 1) * 5 + card)][1] != suit:
            return 0
        card += 1
    return suit
        
def fullHouse(hand, player):
    three = threeKind(hand, player)
    two = twoPair(hand, player)
    if three and two:
        return [three, two[0]] if two[0] != three else [three, two[1]]
    return 0

def fourKind(hand, player):
    card = 0
    while card < 2:
        if ranks[hands[hand][card + ((player - 1) * 5)][0]] == ranks[hands[hand][card + 1 + ((player - 1) * 5)][0]] == ranks[hands[hand][card + 2 +((player - 1) * 5)][0]] == ranks[hands[hand][card + 3 +((player - 1) * 5)][0]]:
            return ranks[hands[hand][card + ((player - 1) * 5)][0]]
        card += 1
    return 0

def straightFlush(hand, player):
    if flush(hand, player) and straight(hand, player):
        return straight(hand, player)
    return 0

def royalFlush(hand, player):
    if straightFlush(hand, player) == ranks["A"]:
        return straightFlush(hand, player)
    
for i in range(1000):
    if royalFlush(i, 1) != royalFlush(i, 2):
        print("you fucked up fam")
    elif straightFlush(i, 1) != straightFlush(i, 2):
        playerOneWins += (straightFlush(i, 1) > straightFlush(i, 2))
    elif fourKind(i, 1) != fourKind(i, 2):
        playerOneWins += (fourKind(i, 1) > fourKind(i, 2))
    elif fullHouse(i, 1) != fullHouse(i, 2):
        playerOneWins += (fullHouse(i, 1) > fullHouse(i, 2))
    elif flush(i, 1) != flush(i, 2):
        playerOneWins += (flush(i, 1) > flush(i, 2))
    elif straight(i, 1) != straight(i, 2):
        playerOneWins += (straight(i, 1) > straight(i, 2))
    elif threeKind(i, 1) != threeKind(i, 2):
        playerOneWins += (threeKind(i, 1) > threeKind(i, 2))
    elif twoPair(i, 1) != twoPair(i, 2):
        playerOneWins += (twoPair(i, 1) > twoPair(i, 2))
    elif onePair(i, 1) != onePair(i, 2):
        playerOneWins += (onePair(i, 1) > onePair(i, 2))
    else:
        playerOneWins += (highCard(i, 1) > highCard(i, 2))



print playerOneWins
print("--- %s seconds ---" % (time.clock() - startTime))
