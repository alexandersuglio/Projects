# deckOfCards.py
import random

sentinel = 51
playerScore = 0
dealerScore = 0

# suits = ["hearts", "diamonds", "spades", "clubs"]
# hearts =   ["Ace",2,3,4,5,6,7,8,9,10,"J","Q","K"]
# diamonds = ["Ace",2,3,4,5,6,7,8,9,10,"J","Q","K"]
# spades =   ["Ace",2,3,4,5,6,7,8,9,10,"J","Q","K"]
# clubs =    ["Ace",2,3,4,5,6,7,8,9,10,"J","Q","K"]
# deck =          [hearts, diamonds, spades, clubs]

card_categories = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
cards_list = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

# aceH = 0
# aceD = 0
# aceC = 0
# aceS = 0

aceCount = 0

# sentinel = 8
# card_categories = ['Hearts']
# cards_list = ['2', '3', '4', '5', '6', '7', '8', '9', '10']

deck = [(card, category) for category in card_categories for card in cards_list]
random.shuffle(deck)

playerHand = []
dealerHand = []

def draw1():

    global sentinel
    range1 = random.randint(0, sentinel)

    pick1 = deck[range1]
    # print("you picked ", pick1)

    playerHand.append(pick1)

    global playerScore

    if deck[range1][0] == "Jack" or deck[range1][0] == "Queen" or deck[range1][0] == "King":
        playerScore += 10

    elif deck[range1][0] == "Ace":
        playerScore += 11

        #scoreDiff = 21 - score
        #if scoreDiff < 11:

        #global aceCount
        #aceCount += 1

    else:
        playerScore += int(deck[range1][0])


    sentinel -= 1
    deck.pop(range1)

    if sentinel == 0:
        print("out of cards!")
        exit()


def draw2():

    global sentinel
    range1 = random.randint(0, sentinel)
    pick1 = deck[range1]

    # print(range, "you picked ", pick1)
    playerHand.append(pick1)

    global playerScore

    if deck[range1][0] == "Jack" or deck[range1][0] == "Queen" or deck[range1][0] == "King":
        playerScore += 10

    elif deck[range1][0] == "Ace":
        playerScore += 11

        # global aceCount
        # aceCount += 1

    else:
        playerScore += int(deck[range1][0])


    sentinel -= 1
    deck.pop(range1)

    range2 = random.randint(0, sentinel)
    pick2 = deck[range2]

    # print("you picked ", pick1, "and", pick2)
    playerHand.append(pick2)

    if deck[range2][0] == "Jack" or deck[range2][0] == "Queen" or deck[range2][0] == "King":
        playerScore += 10

    elif deck[range2][0] == "Ace":
        playerScore += 11

        # global aceCount
        # aceCount += 1

    else:
        playerScore += int(deck[range2][0])


    sentinel -= 1
    deck.pop(range2)

    if sentinel == 0:
        print("out of cards!")
        exit()


def dealerDraw1():

    global sentinel
    range1 = random.randint(0, sentinel)

    global dealerScore

    print('Calling me')

    #while dealerScore < 17:
        #
        # pick1 = deck[range1]
        # # print("you picked ", pick1)
        #
        # dealerHand.append(pick1)

    # if deck[range1][0] == "Jack" or deck[range1][0] == "Queen" or deck[range1][0] == "King":
    #     dealerScore += 10
    #
    # elif deck[range1][0] == "Ace":
    #     dealerScore += 11

        #scoreDiff = 21 - score
        #if scoreDiff < 11:

        #global aceCount
        #aceCount += 1

    # else:
    #     dealerScore += int(deck[range1][0])
    #
    #
    # sentinel -= 1
    # deck.pop(range1)
    #
    # if sentinel == 0:
    #     print("out of cards!")
    #     exit()


def dealerDraw2():

    global sentinel

    range1 = random.randint(0, sentinel)
    pick1 = deck[range1]

    # print(range, "you picked ", pick1)
    dealerHand.append(pick1)

    global dealerScore

    if deck[range1][0] == "Jack" or deck[range1][0] == "Queen" or deck[range1][0] == "King":
        dealerScore += 10

    elif deck[range1][0] == "Ace":
        dealerScore += 11

        # global aceCount
        # aceCount += 1

    else:
        dealerScore += int(deck[range1][0])


    sentinel -= 1
    deck.pop(range1)

    range2 = random.randint(0, sentinel)
    pick2 = deck[range2]

    # print("you picked ", pick1, "and", pick2)
    dealerHand.append(pick2)

    if deck[range2][0] == "Jack" or deck[range2][0] == "Queen" or deck[range2][0] == "King":
        dealerScore += 10

    elif deck[range2][0] == "Ace":
        dealerScore += 11

        # global aceCount
        # aceCount += 1

    else:
        dealerScore += int(deck[range2][0])


    sentinel -= 1
    deck.pop(range2)

    if sentinel == 0:
        print("out of cards!")
        exit()




def intro():
    entry = str(input("Welcome to BlackJack. H for Deal "))

    if entry == 'H' or entry == "h":
        dealerDraw2()
        draw2()
        print("Dealer Hand:", dealerHand)
        print("Your Score:", dealerScore)
        print()
        print("Your Hand:", playerHand)
        print("Your Score:", playerScore)

        if playerScore == 21:
            print("You win!")
            exit()

        if playerScore > 21:
            print("Bust!")
            exit()

        nextRound()

    else:
        exit()

def nextRound():
    gameover = False

    while gameover != True:

        entry = str(input("Hit or Stay: "))

        if entry == "h" or entry == "H":
            draw1()
            print("Dealer Hand:", dealerHand)
            print("Your Score:", dealerScore)
            print()
            print("Your Hand:", playerHand)
            print("Your Score:", playerScore)

            if playerScore == 21:
                print("You win!")
                exit()

            if playerScore > 21:
                print("Bust!")
                exit()

        if entry == "s" or entry == "S":
            # exit()
            print("Dealer draws...")

            while dealerScore < 17:
                dealerDraw1()
                print(dealerHand)

            gameover = True



                # if dealerScore == 21:
                #     print("Dealer wins, you lose!")
                #
                # if dealerScore > 21:
                #     print("Dealer Bust! You win!")
                #     exit()




        #else:
        #    exit()


intro()
## print(deck)
