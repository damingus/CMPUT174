import random 

class Card:
    # Initializes our card class with a rank and color
    # rank: an integer between 1-4
    # color - a string (“R”, “B”, “G”, or “Y”) 
    def __init__(self, rank, color):
        self.rank = rank
        self.color = color

    # returns the rank of a card
    def get_rank(self):
        return self.rank

    def get_color(self):
        return self.color

    def display(self):
        print("|" + str(self.rank) + self.color + "|")

class Deck:
    # Initialize our deck class, by generating all the different possible cards we could have in our 16 card deck
    def __init__(self):
        self.card_list = []
        self.color_list = ["R", "B", "G", "Y"]
        
        for index in range(len(self.color_list)):
            for i in range(1,5):
                self.card_list.append(Card(i, self.color_list[index]))
         
    # Randomly shuffle the deck of cards
    def shuffle(self):
        random.shuffle(self.card_list)

    # Return a value from the top of the deck, remember to remove it from the deck as well.
    def deal(self):
        player_cards = []
        for index in range(0,4):
            dealt_card = self.card_list[index]
            player_cards.append(dealt_card)
            #dealt_card.display() 
            self.card_list.pop(index) # remove top card
        
        return player_cards
    
    # Display the remaining cards in the deck,
    def display(self):
        print("This is the rest of the deck")
        for card in self.card_list:
            card.display()

class Player:
    # Initializes a player with a way of keeping track of cards in their hand.  
    def __init__(self):
        self.player_hand = []

    # Add a card to the player’s hand
    def add(self, card):
        self.player_hand.append(card)
    
    # Returns the sum of all the cards of a particular color in the player’s hand.
    def colored_cards(self, color):
        # lists storing all the values of cards per colour
        red_cards = []
        blue_cards = []
        green_cards = []
        yellow_cards = []

        # obtain the rank of each element in self.player_hand using the get_rank method, based on the return value of the get_color method
        for index in range(len(self.player_hand)):
            if self.player_hand[index].get_color() == 'R':
                red_cards.append(self.player_hand[index].get_rank())

            elif self.player_hand[index].get_color() == 'B':
                blue_cards.append(self.player_hand[index].get_rank())

            elif self.player_hand[index].get_color() == 'G':
                green_cards.append(self.player_hand[index].get_rank())

            else:
                yellow_cards.append(self.player_hand[index].get_rank())
            
        # condtional statements that return the sum of the desired color of cards within the player hand 
        if color == 'R':
            sum_of_cards = sum(red_cards)
        elif color == 'B':
            sum_of_cards = sum(blue_cards)
        elif color == 'G':
            sum_of_cards = sum(green_cards)
        elif color == 'Y':
            sum_of_cards = sum(yellow_cards)
        else:
            sum_of_cards = 0
        
        print("The sum of", color, "cards in the player's hand is:", str(sum_of_cards))
        
    # display the player's hand
    def display(self):
        print("This is the player hand")
        for card in self.player_hand:
            card.display()
        print("\n")

            
def main():
    # create the deck
    deck = Deck()
    # shuffle the deck
    deck.shuffle()
    # create player hand
    player_hand = Player()

    # deal the deck into empty list
    player_cards = deck.deal()
    
    # add elements of empty list into player_hand
    for index in range(len(player_cards)):
        player_hand.add(player_cards[index]) 
    
    # use the display() method from class Player to display the player hand
    player_hand.display() 
    # Use the display9) method from class Deck to display the remaining cards
    deck.display()

    # get color of cards to sum
    get_color = str.upper(input("Select a color (R, G, B, Y): "))

    # return the sum of the cards of the particular color
    player_hand.colored_cards(get_color)
main()



    
    
    
    


