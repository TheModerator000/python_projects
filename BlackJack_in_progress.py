# Created by: Justin Brose
# Date: 10/1/21

import random

# Directions for play

print("Welcome to Black Jack!")
print("Here is how this version works: ")
print("1.) The main objective is to get the dealer's bank to 0. You can do this by beating the dealer to 21 or not 'busting'. If you 'bust' or the dealer 'bust' then credits are lost.")
print("2.) You play this game of Black Jack against the dealer. Both you and the dealer have 500 credits in your bank.")
print("3.) The dealer will deal both you and themself 2 cards. You cannot see the dealer's cards until one of you 'bust' or reach 21.")
print("4.) If you reach 21 and the dealer is under 21, then you will get 2x your bet and the dealer will lose their bet(the dealer's bet is equal to yours) and vice versa.")
print("5.) If you reach 21 and the dealer is over 21, then you get 4x your bet and the dealer loses 2x their bet and vice versa.")
print("6.) If you 'bust' and the dealer does not 'bust', you lose the amount you bet and the dealer gains the amount they bet and vice versa.")
print("7.) There are two options for this game when you are asked 'What do you want to do?'. You may 'hit'(ask for one more card) or 'stay' (keep your current value).")
print("8.) If you choose to stay and your value is closer to 21 than the dealer's, then you win 2x your bet and the dealer loses their bet and vice versa.")
print("That is all the rules for this game of Black Jack. Have Fun!")

# first we need to give the code our values for cards

card_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
bank = 500
dealer_bank = 500

# next you have to define your first card's value. In this case, your first cards
# are a random number from our card values list.

first_card = random.choice(card_values)
dealer_first_card = random.choice(card_values)

play_again = 'yes'

# Allows for the game to start again

while play_again == 'yes':
  if bank <= 0:
      print("Better luck next time!") + exit()
  if dealer_bank <= 0:
      print("How is this possible? You beat the dealer... but the house always wins :(.") + exit()
  print("you have: ", bank, "in your bank")
  print("The dealer has ", dealer_bank, "in their bank.")
  bet = int(input("How much is your bet?"))

  print("Your first card is: ", first_card)
  print("The Dealer's first card is face down.")
  sum = first_card
  dealer_sum = dealer_first_card
  turn = "hit"
  dealer_turn = "hit"

# functionality for 'hit', player, and dealer
# the bank and dealer_bank arguments allow for funds to inc and dec
# from their variables.

  while turn == "hit":
      sum += random.choice(card_values)
      dealer_sum += random.choice(card_values)
      print("You currently have: ", sum)
      print("The dealer's cards are face down.")

# the code below allows for the program to check if the bank is empty. If the
# bank is empty, then the program will close out with the message
# 'Better luck next time!'

      if bank <= 0:
          print("Better luck next time!") + exit()

# Below code displays all scenarios in the game as if functions. The program will
# evaluate each one to see if they are true and if they are then it will execute
# the assigned argument.

      elif sum < 21 and dealer_sum > 21:
          print("The dealer bust with: ",dealer_sum, "! Here is your reward", bet * 1.25)
          bank += bet * 1.25
          dealer_bank -= bet *1.25
          break

      elif sum > 21 and dealer_sum < 21:
          print("You bust, but the dealer is under with:", dealer_sum, ". Dealer wins!")
          bank -= bet
          dealer_bank += bet

      elif sum > 21 and dealer_sum > 21:
          print("No one wins this game. The dealer had: ", dealer_sum)
          bank -= bet/2
          dealer_bank -= bet/2

      elif sum == 21 and dealer_sum < 21:
          print("Black Jack! The dealer ended with: ", dealer_sum)
          print("Here is your reward: ", bet * 2)
          bank += bet * 2
          dealer_bank -= bet

      elif sum == 21 and dealer_sum > 21:
          print("Black Jack! The dealer bust with ", dealer_sum, "and you had: ", sum)
          print("Here is your reward: ", bet * 4)
          bank += bet * 4
          dealer_bank -= bet *2

      elif dealer_sum == 21 and sum > 21:
          print("You bust! The house always wins. The dealer had 21!")
          print("The house takes: ", bet, " credits.")
          bank -= bet * 2
          dealer_bank += bet * 4

      elif dealer_sum == 21 and sum < 21:
          print("The house always wins :). The dealer had 21!")
          print("The house takes: ", bet, " credits.")
          bank -= bet
          dealer_bank += bet * 2

# The code below checks to see if the round is over and asks if the player wants
# to try again.

      if sum < 21 and dealer_sum > 21:
          play_again = input("Want to play_again?")

      if sum == 21 or dealer_sum == 21 and bank != 0 or bank < 0  and dealer_bank != 0 or dealer_bank < 0:
          play_again = input("Want to play again?")
          break

# The code below checks to see if the round is still going. If it is the if
# statement gives the player the option to either say 'hit' or 'stay'. If then
# player says stay then the code will check if who is closer to 21. The play That
# is closer to 21 will be awarded points.
      if sum < 21:
          turn = input("what do you want to do?")
          if turn == "stay":
              print("You stopped at: " , sum, "and the dealer had: ", dealer_sum)
              if sum > dealer_sum:
                  print("You were closer to 21 than the dealer! You win this round.")
                  print("Your reward is: +", bet * 2)
                  play_again = input("Want to play again? ")
                  bank += bet *2
                  dealer_bank -= bet
              elif sum == dealer_sum:
                  print("No one wins this game. The dealer had: ", dealer_sum)
                  bank -= bet/2
                  dealer_bank -= bet/2
              else:
                  print("The dealer was closer to 21 than you! The house always wins! :)")
                  print("The house takes the pot: ", bet *2)
                  play_again = input("Want to play again? ")
                  bank -= bet
                  dealer_bank += bet * 2
      else:
          turn = "bust"

# This last bit of code checks if the round is complete. If so, the player can
# type in 'yes' and a new round will start.
      if sum > 21:
          play_again = input("Want to play again?")
          break
