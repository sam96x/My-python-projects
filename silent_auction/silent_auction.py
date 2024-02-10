import os

bidders = {}
  
next_input = "áno"
while next_input == "áno":
  name_input = input("Aké je Vaše meno?: ")
  bid_input = int(input("Aká je vaša ponuka v eurách?: "))
  
  bidders[name_input] = bid_input
  
  next_input = input("Sú nejaký ďalší záujemcovia? áno alebo nie: ")
  
  if next_input == "nie":
    os.system("clear")

def max_bid(bidders):
  max_bid = 0
  winner = ""
  
  for key in bidders:
    if bidders[key] > max_bid:
      max_bid = bidders[key]
      winner = key
  print(f"Víťazom je {winner} s cenou {max_bid} eur.") 

max_bid(bidders)