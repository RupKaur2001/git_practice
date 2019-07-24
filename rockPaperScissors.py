import random
print('Rock, Paper or Scissors?')
computer_choice=("Rock",'Paper','Scissors')[random.randint(0,2 )]
names_symbols={"ROCK":"ooo",'PAPER':u"\U0001F4F0","SCISSORS":u"\u2702"}
flag=0
while True:
    user_choice=input()
    
    if ((user_choice).upper() in names_symbols):
        break
    print('Please input choice again: Rock, Paper or Scissors')
print('I choose '+computer_choice)
if ((computer_choice).casefold()==user_choice.casefold()):
    flag=-1
    print("DRAW")
if user_choice.casefold()=="ROCK":
    if computer_choice.casefold()=='scissors':
        flag=1
if user_choice.casefold()=="paper":
    if computer_choice.casefold()=='rock':
        flag=1
else :
    if computer_choice.casefold()=='paper':
        flag=1
if flag==0:
    print("You won")
elif flag==1 :
    print('You lost')
print(names_symbols[computer_choice.upper()]+" v/s "+names_symbols[user_choice.upper()])