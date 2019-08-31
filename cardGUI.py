import Card_Deck
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

game_score = 0
roundNumber = 1

def playRound(game_score, roundNumber):
    root = Tk()
    root.title("Blackjack")
    root.configure(background='green')
    root.resizable(False, False)
    mainFrame = Frame(root, bg='green', width=1500, height=1000).pack(expand='yes')
    if roundNumber == 1:
        rulesPrompt = messagebox.showinfo(message="Welcome to blackjack simulator! 21 points = 40, Bust = -5, and standing gives you your standing points. Good luck! ", title="Welcome!")
    newRoundPrompt = messagebox.showinfo(message="Current Score is %d and the current round is %d" % (game_score, roundNumber), title='Scorecard',parent=root)
    newDeck = Card_Deck.Deck()
    newDeck.shuffleDeck()
    my_hand = newDeck.deal(2)
    faceCards = {'J':10, 'Q':10, 'K':10, 'A': 11}

    def getNumCards(my_hand):
        num = len(my_hand)
        return num

    def getCardImg(index):
        card = my_hand[index]
        card_img = ImageTk.PhotoImage(Image.open(card + ".png"))
        return card_img

    def getXValue(index):
        value = index * 250
        return value

    def getPoints(hand):
        hand_score = 0
        handPoints = []
        for card in hand:
            if len(card) > 2:
                point = card[:2]
            else:
                point = card[0]
            if point in faceCards.keys():
                handPoints.append(faceCards[point])
            elif point != 'A':
                handPoints.append(int(point))
            else:
                if sum(handPoints) + faceCards['A'] > 21:
                    handPoints.append(1)
                else:
                    handPoints.append(faceCards['A'])

        hand_score = sum(handPoints)
        return hand_score

    def hit(numCards):
        numCards = getNumCards(my_hand)
        newDeck.dealMore()
        img = getCardImg(numCards)
        cardFrame = Label(mainFrame, bg='green', image=img)
        cardFrame.image = img
        cardFrame.pack()
        cardFrame.place(bordermode=INSIDE, height=250, width=250, x=getXValue(len(my_hand) - 1), y=300)

        points = getPoints(my_hand)
        if points > 21:
            for card in my_hand:
                if card[0] == 'A':
                    points = points - 10
                    if points < 21:
                        break

        pointLabel = Label(mainFrame, bg='green', font='black', text=str(points))
        pointLabel.pack()
        pointLabel.place(height=100, width=100, x=100, y=800)

        game_conditions(points)

    def stand(points):
        global game_score
        points = getPoints(my_hand)
        if points == 21:
            messagebox.showinfo(message="Congrats, you got 21!.")
            game_score += 40
        else:
            messagebox.showinfo(message="You stood with a score of %d." % points)
            game_score += points
        root.destroy()

    def game_conditions(points):
        global game_score
        if points == 21:
            messagebox.showinfo(message="Congrats, you got 21!.")
            game_score += 40
            root.destroy()
        elif points > 21:
            messagebox.showinfo(message="Unlucky! You busted.")
            game_score -= 5
            root.destroy()
        else:
            pass

    for i in range(len(my_hand)):
        img = getCardImg(i)
        cardFrame = Label(mainFrame, bg='green', image= img)
        cardFrame.image = img
        cardFrame.pack()
        cardFrame.place(bordermode=INSIDE, height=250, width=250, x=getXValue(i), y=300)

    hitButton = Button(mainFrame, text="Hit", bg='light blue', activebackground='yellow', command= lambda x= getNumCards(my_hand): hit(x))
    hitButton.pack()
    hitButton.place(height = 50, width = 50, x = 100, y= 700)

    standButton = Button(mainFrame, text="Stand", bg='light blue', activebackground='yellow', command= lambda x=getPoints(my_hand): stand(x))
    standButton.pack()
    standButton.place(height = 50, width = 50, x = 300, y = 700)

    countLabel = Label(mainFrame, bg='green', font='black', text="Count: ")
    countLabel.pack()
    countLabel.place(height=100, width= 100,  x=10, y=800)

    points = getPoints(my_hand)
    pointLabel = Label(mainFrame, bg='green', font='black', text=str(points))
    pointLabel.pack()
    pointLabel.place(height=100, width= 100,  x=100, y=800)

    root.mainloop()


if __name__ == '__main__':

    for i in range(1,6):
        playRound(game_score, roundNumber)
        roundNumber += 1

    newRoundPrompt = messagebox.showinfo(message="Your final score after 5 rounds is %d." % (game_score), title='Scorecard')