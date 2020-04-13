import random
q = "q"
Q = "Q"
h = "h"
H = "H"
c = "c"
C = "C"
s = "s"
S = "S"
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.next = None

    def printCard(self):
        return ("{} of {}".format(self.value,self.suit))
    def printSuit(self):
        return ("This is a card of {}".format(self.suit))

    def printValue(self):
        return ("The value of the card is {}".format(self.value))

class Stack:

    def __init__(self, sname = None, otherStack=None):

        self.stackTop = None
        self.nCards   = 0
        self.stackName= sname
        if (otherStack!=None):  #Copy Constructor
            self.stackTop = None
            self.copyStack(otherStack)


    def initializeStack(self):
        self.nCards = 0
        while (self.stackTop != None):
            temp = self.stackTop
            self.stackTop = self.stackTop.next
            del temp

    def isEmptyStack(self):
        return self.stackTop == None

    def isEmpty(self):
        return self.stackTop == None

    def isFullStack(self):
        return False

    def pushNode(self, newNode):
        if (self.size()>0 and type(newNode.data) != type(self.stackTop.data)):
            print("Invalid data Type. This stack is a stack for the " + str(type(self.stackTop.data)) + " data type.")
            return

        newNode.next  = self.stackTop
        self.stackTop = newNode
        self.nCards+=1


    def push(self, cardValue, cardSuit):
       
        newCard = Card(cardSuit,cardValue)

        newCard.next = self.stackTop
        self.stackTop = newCard
        self.nCards+=1

    def top(self):
        if (self.stackTop !=None):
            return self.stackTop.data
        else:
            return None
    def topCard(self):
        if (self.stackTop != None):
            return self.stackTop
        else:
            return None



    def pop(self):

        if(self.stackTop!=None):
            temp=self.stackTop
            self.stackTop = self.stackTop.next
            del temp
            self.nCards-=1
        else:
            print("Cannot remove from an empty stack.")

    def numOfCards(self):
        return self.nCards


    def __str__(self):
        retstr = "" + "top | \n "
        s = self.stackTop

        while (s != None):
            retstr += str(s.value) + " : " + str(s.suit) + "\n"
            s = s.next
        retstr += "| bottom"
        return retstr

        # make a copy of otherStack to this stack.*/

    def copyStack(self,otherStack):

        if (self.stackTop != None):  # if stack is nonempty, make it empty
            self.initializeStack()

        if (otherStack.stackTop == None):
            self.stackTop = None
        else:

            current = otherStack.stackTop
            # self.stackTop = new Node<Type>;  #create the node
            self.stackTop = Card(current.suit,current.value)
            self.stackTop.next = None  # set the next field of the node to NULL
            last = self.stackTop
            current = current.next
            # copy the remaining stack
            while (current != None):
                newCard = Card(current.suit,current.value)
                newCard.next = None
                last.next = newCard
                last = newCard
                current = current.next
                self.nCards += 1
            self.nCards +=1

    def isEqual(self, other):
        if(not isinstance(other,Stack)):
            return False
        if (not self.isEmpty() and not other.isEmpty() and type(self.stackTop)!=type(other.stackTop)):
            return False
        if (self.isEmpty() and other.isEmpty()):
            return True
        if (self.size() != other.size()):
            return False


        lstA = []
        lstB = []
        result = False
        thisSize = self.size()
        otherSize = other.size()

        for i in range(0, thisSize):
            lstA.append(self.top())
            self.pop()

        for i in range(0, otherSize):
            lstB.append(other.top())
            other.pop()

        self.stackTop = None
        self.nCards = 0
        for j in range(thisSize - 1, -1, -1):
            self.pushNode(Node(lstA[j]))

        for j in range(otherSize - 1, -1, -1):
            other.pushNode(Node(lstB[j]))
        i = 0
        while (not self.isEmpty() and not (other.isEmpty())):

            if (self.top() == other.top()):

                t = self.top()
                self.pop()
                o = other.top()
                other.pop()

                if (self.isEmpty() and other.isEmpty()):
                    result = True
                    break
                i+=1
            else:
                result = False
                break

        while (not other.isEmpty()):
            o = other.top()
            other.pop()

        self.stackTop = None
        self.nCards = 0

        for j in range(thisSize - 1, -1, -1):
            self.push(Node(lstA[j]))
        for j in range(otherSize - 1, -1, -1):
            other.push(Node(lstB[j]))

        return result

    def reverse(self):
        if(self.nCards == 0):
            return
        current = prev = self.stackTop
        current = current.next
        prev.next = None
        while (current != None):
            succ = current.next
            current.next = prev
            prev = current
            current = succ

        self.stackTop = prev

    def deleteInnerNode(self, loc):

        s = Stack()
        assert self.stackTop != None, "Stack is Empty"
        current = self.stackTop
        i = 0
        size = self.numOfCards()
        assert loc < size and not(self.isEmpty()), "Stack is Empty or location of deleted node is outside of stack size"
        while (i < loc and current != None):
            # print("i="+str(i))
            current = current.next
            i += 1

        n = current

        i = 0
        size = self.numOfCards()
        while (not self.isEmpty() and i < size):
            if (i != loc):
                s.push(self.stackTop.value,self.stackTop.suit)
                self.pop()

            else:
                self.pop()
            i +=1
        s.reverse()
        self.stackTop = s.stackTop
        self.nCards = s.numOfCards()
        return n


    def getInnerNode(self,loc):
        s = Stack()
        assert self.stackTop != None, "Stack is Empty"
        current = self.stackTop
        i = 0
        size = self.numOfCards()
        assert loc < size, "requested location outside of stack size"
        while (i < loc and current != None):
            current = current.next
            i += 1

        return current


    def __eq__(self,other):
            return self.isEqual(other)

    def __ne__(self,other):
        return (not self.isEqual(other))

class Deck(Stack):
    # def getCards(self):
    #     #stuff
    
    # def shuffle(self):
    #     #stuff
    def readDeck(self):
        cardFile = open("cards.txt","r")
        if cardFile.mode == 'r':
            contents = cardFile.readlines()
        for x in contents:
            word = x.split(' ')
            value = word[0]
            suit = word[1]
            self.push(value,suit)
    
    def printDeck(self):
        print(str(self))
    
    #This shuffle is not effecient because it will always return the same shuffled order, which cannot be used in a game like blackjack (Cheating!)
    def simpleShuffle(self):
        sizeOfDeck = self.numOfCards()
        halfOfDeck = sizeOfDeck/2
        stack1 = Stack()
        stack2 = Stack()
        for x in range(0, halfOfDeck):
            card = self.topCard()
            stack1.push(card.value,card.suit)
            self.pop()
        for x in range(halfOfDeck, sizeOfDeck):
            card = self.topCard()
            stack2.push(card.value,card.suit)
            self.pop()
        for x in range(0, halfOfDeck):
            card = stack1.topCard()
            self.push(card.value,card.suit)
            stack1.pop()
            card = stack2.topCard()
            self.push(card.value,card.suit)
            stack2.pop()

    #This shuffle is much more effecient for this game since the stack will almost always be unique in ordering, perfect for programs that need random sorting
    def advancedSuffle(self):
        #Fisher Yates shuffle algorithm
        s1 = Deck()
        while(self.numOfCards() > 0):
            randomNum = random.randint(0,self.numOfCards()-1)
            randomCard = self.getInnerNode(randomNum)
            s1.push(randomCard.value,randomCard.suit)
            self.deleteInnerNode(randomNum)
        self.copyStack(s1)
    
    def valueOfDeck(self):
        totalValue = 0
        s = self.stackTop
        while (s != None):
            if(s.value == "King" or s.value == "Queen" or s.value == "Jack"):
                totalValue += 10
            elif(s.value == "Ace"):
                totalValue += 1
            else:
                totalValue += int(s.value)
            s = s.next
        return totalValue

class Game:
    def __init__(self):
        self.playerWins = 0
        self.dealerWins = 0
        self.sessionNumber = 1
        self.playerDeck = Deck()
        self.dealerDeck = Deck()
        self.mainDeck = Deck()
        self.decksUsed = 0
        self.numberOfPush = 0

    def printPlayerHand(self):
        print("------------------------------------------------")
        s = self.playerDeck.stackTop
        retstr = ""
        print("Your hand: ")
        while (s != None):
            retstr += str(s.value) + " of " + str(s.suit)
            s = s.next
        print(retstr + "Total value is : " + str(self.playerDeck.valueOfDeck()))
        print("------------------------------------------------")

    def printDealerHand(self):
        print("------------------------------------------------")
        s = self.dealerDeck.stackTop
        retstr = ""
        print("Dealers hand: ")
        while (s != None):
            retstr += str(s.value) + ":" + str(s.suit)
            s = s.next
        print(retstr + "Total value is : " + str(self.dealerDeck.valueOfDeck()))
        print("------------------------------------------------")


    def handleNoCards(self):
        print("Very few cards left - time to shuffle")
        self.mainDeck.readDeck()
        self.mainDeck.advancedSuffle()

    def checkGameOutcome(self):
        if(self.playerDeck.valueOfDeck() == self.dealerDeck.valueOfDeck()):
            self.handlePush()
        elif(self.dealerDeck.valueOfDeck() > 21):
            self.handleDealerLoss()
        elif(self.playerDeck.valueOfDeck() > self.dealerDeck.valueOfDeck()):
            self.handleDealerLoss()
        else:
            self.handlePlayerLoss()
    def handlePlayerLoss(self):
        print("======== Result ========")
        print("Player lost: hand is over 21 or lower than dealers")
        print("========================")
        self.sessionNumber += 1
        self.dealerWins +=1
        self.playerDeck = Deck()
        self.dealerDeck = Deck()
        decision = input("Type q or Q to stop playing, or c or C to continue: ")
        if(str(decision) == q or str(decision) == Q):
            print("Thanks for playing Blackjack!")
            quit()
        elif(str(decision) == c or str(decision) == C):
            self.dealCards()

    def handleDealerLoss(self):
        print("======== Result ========")
        print("Dealer lost: hand is over 21 or lower than the player")
        print("========================")
        self.sessionNumber += 1
        self.playerWins +=1
        self.playerDeck = Deck()
        self.dealerDeck = Deck()
        decision = input("Type q or Q to stop playing, or c or C to continue: ")
        if(str(decision) == q or str(decision) == Q):
            print("Thanks for playing Blackjack!")
            quit()
        elif(str(decision) == c or str(decision) == C):
            self.dealCards()

    def checkPlayerLoss(self):
        if(self.playerDeck.valueOfDeck() > 21):
                self.handlePlayerLoss()

    def checkDealerLoss(self):
        if(self.dealerDeck.valueOfDeck() > 21):
                self.handleDealerLoss()

    def handlePush(self):
        print("======== Result ========")
        print("Your hand value and the dealers are equal: Push!")
        print("========================")
        self.sessionNumber += 1
        self.playerDeck = Deck()
        self.dealerDeck = Deck()
        self.numberOfPush += 1
        decision = input("Type q or Q to stop playing, or c or C to continue: ")
        if(str(decision) == q or str(decision) == Q):
            print("Thanks for playing Blackjack!")
            quit()
        elif(str(decision) == c or str(decision) == C):
            self.dealCards()

    def dealCards(self):
        while(self.mainDeck.numOfCards() > 10):
            print("======== "+ "Player: " + str(self.playerWins) + " -- Game number: " + str(self.sessionNumber) + " -- " + "Number of Push: " + str(self.numberOfPush) + " -- " + "Dealer: " + str(self.dealerWins) + " ========")
            card = self.mainDeck.topCard()
            self.playerDeck.push(card.value,card.suit)
            self.mainDeck.pop()
            card = self.mainDeck.topCard()
            self.dealerDeck.push(card.value,card.suit)
            self.mainDeck.pop()
            card = self.mainDeck.topCard()
            self.playerDeck.push(card.value,card.suit)
            self.mainDeck.pop()
            card = self.mainDeck.topCard()
            self.dealerDeck.push(card.value,card.suit)
            self.mainDeck.pop()
            self.printPlayerHand()
            if(self.playerDeck.valueOfDeck() == 21 and self.dealerDeck.valueOfDeck() != 21):
                print("Player Blackjack!!")
                self.playerWins += 1
            elif(self.dealerDeck.valueOfDeck() == 21 and self.playerDeck.valueOfDeck() != 21):
                print("Dealer Blackjack!!")
                self.dealerWins += 1
            elif(self.playerDeck.valueOfDeck() == 21 and self.dealerDeck.valueOfDeck() == 21):
                self.handlePush()

            while(self.playerDeck.valueOfDeck() <= 12):
                card = self.mainDeck.topCard()
                self.playerDeck.push(card.value,card.suit)
                self.mainDeck.pop()
                self.printPlayerHand()
            self.checkPlayerLoss()
            if(self.playerDeck.valueOfDeck() > 12 and self.playerDeck.valueOfDeck() <= 17):
                decision = input("Type s or S to stand OR h or H to hit OR q or Q to quit: ")
                if(str(decision) == h or str(decision) == H):
                    print("===== Player hits =====")
                    card = self.mainDeck.topCard()
                    self.playerDeck.push(card.value,card.suit)
                    self.mainDeck.pop()
                    self.printPlayerHand()
                elif(str(decision) == q or str(decision) == Q):
                    print("Thanks for playing Blackjack!")
                    return
                elif(str(decision) == s or str(decision) == S):
                    print("===== Player stands =====")
            self.checkPlayerLoss()
            self.printDealerHand()
            while(self.dealerDeck.valueOfDeck() < 17):
                card = self.mainDeck.topCard()
                self.dealerDeck.push(card.value,card.suit)
                self.mainDeck.pop()
                self.printDealerHand()
            self.checkGameOutcome()

        self.handleNoCards()
        self.dealCards()
game = Game()
print("======== Welcome to Blackjack! ========")
print("========  Rules of the Game  ========")
print("--------------------------")
print("===== For the player =====")
print("- If the player has 21 and the dealer is does not have 21, the player wins the game or the game session. \n- If he exceeds 21, the dealer wins, if he has 18 or more, he stands no drawing more cards. \n- If he has 12 or less, he keeps drawing card by card until he gets to a number that is above 17. \n- If the player is between 12 and 17, he can decide to hit or stand one time.")
print("--------------------------")
print("--------------------------")
print("===== For the dealer =====")
print("- Dealer will get cards if his total value is below 17. \n- Once he is at 17-21 he must stop. \n- If he goes over 21 he busts")
print("--------------------------")
decks = input("How many decks will you like to use for this game? 1 or greater: ")
while(decks <= 0):
    decks = input("How many decks will you like to use for this game? 1 or greater: ")
    game.decksUsed = decks
while(decks > 0):
    game.mainDeck.readDeck()
    decks = decks - 1
game.mainDeck.advancedSuffle()
print("Shuffling using Fisher Yates Algo...")
print("Type 'q' or 'Q' at any input to stop playing the game!")
game.mainDeck.advancedSuffle()
game.dealCards()




