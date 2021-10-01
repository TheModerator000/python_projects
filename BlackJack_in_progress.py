import random
# first we need to give the code our values for cards
card_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
bank = 500
# next you have to define your first card's value. In this case, your first cards
# is a random number from our card values list
first_card = random.choice(card_values)
dealer_first_card = random.choice(card_values)

play_again = 'yes'

while play_again == 'yes':
  print("you have: ", bank, "in your bank")
  bet = int(input("How much is your bet?"))

  print("Your first card is: ", first_card)
  print("The Dealer's first card is: ", dealer_first_card)
  sum = first_card
  dealer_sum = dealer_first_card
  turn = "hit"
  dealer_turn = "hit"

# currently this code creates an inifite loop!

  while turn == "hit":
    sum += random.choice(card_values)
    dealer_sum += random.choice(card_values)
    print("You currently have: ", sum, " and the dealer has: ", dealer_sum)

    if sum < 21:
        turn = input("what do you want to do?")
    else:
        turn = "bust"

    if sum > 21 and dealer_sum < 21:
        print("You went over 21!")
        bank -= bet
    elif sum == 21:
      print("Black Jack!")
      bank += bet * 2
    else:
        print("You stopped at: " , sum, "and the dealer had: ", dealer_sum)
        bank -= bet/2

    if dealer_sum > 21:
        print("The dealer bust!")
    elif dealer_sum == 21:
        print("The house always wins")

  print("you have: ", bank, "in your bank")
  if bank <= 0:
      print("Better luck next time!") + exit()
  else:
      play_again = input("Want to play again? ")
