
MAX_LINES =3
MAX_BET=100
MIN_BET=1
rows=3
cols=3
import random

symbol_count={
    'a':2,
    'b':4,
    'c':6,
    'd':8
}
symbol_values={
    'a':5,
    'b':4,
    'c':3,
    'd':2
}

def check_winnings(coloumns,lines,bet,values):
  winnings=0
  winning_lines=[]
  for line in range(lines):
    symbol=coloumns[0][line]     #check the symbol in the first row of  first coloumn only and all the symbols in the first coloumn must be same to win a bet 
    
    for coloumn in coloumns:
       symbol_check=coloumn[line]     #for looping through every single coloumn
       if symbol != symbol_check:
         break                        #if symbols are not equal then it is a loss
       else:
         winnings+=values[symbol]*bet     #this is bet on each line not total bet
         winning_lines.append(line+1)
  return winnings ,winning_lines
  
  


def slot_machine(rows,cols,symbols):
    all_symbols=[]
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    coloumns=[]      #to store coloumns values not row values and revisit the video at 24:00
    for _ in range (cols):
        coloumn=[]
        current_symbols=all_symbols[:]
        for _ in range (rows):
            value=random.choice(current_symbols)
            current_symbols.remove(value)
            coloumn.append(value)
        coloumns.append(coloumn)   
            
    return coloumns


def print_slot_machine(coloumns):
    for row in range(len(coloumns[0])):
        for i ,coloumn in enumerate(coloumns):
            if i != len(coloumns)-1:
                print(coloumn[row],end="|")
            else:
                print(coloumn[row],end="")
                
        print()






def deposit():
 while True:
    amount=input("Please enter the amount you want to deposit:$ ")
    if amount.isdigit():
      amount=int(amount)
      if amount >0:
        break
      else:
        print("enter a number greater than 0.")
    else:
      print("enter a valid deposit")
 return amount      

def get_no_of_lines():
 while True:
    lines=input("enter the number of lines to bet on (1-" + str(MAX_LINES) + "): ")
    if lines.isdigit():
      lines=int(lines)
      if MAX_LINES >=lines >=1:
        break
      else:
        print("enter a VALID NUMBER OF LINE.")
    else:
      print("enter a valid response")
 return lines 

def get_det():
 while True:
    amount=input("Please enter the bet amount:$ ")
    if amount.isdigit():
      amount=int(amount)
      if MAX_BET>=amount >=MIN_BET:
        break
      else:
        print(f"enter a number between {1}-{100}.")
    else:
      print("enter a valid BET")
 return amount  
        


def spin(balance):
 
 lines=get_no_of_lines()
 bet=get_det()
 total_bet=lines*bet
 while True:
 
    if total_bet>balance:
        print( f"insufficient funds, please try again with lesser amount or more deposits.CURRENT BALANCE--{balance}")
    else:
        break
 print( f"you betted ${bet} on line {lines} and your total bet is:{total_bet}")
 print(balance,lines)
 
 
 slot=slot_machine(rows,cols,symbol_count)
 print_slot_machine(slot)
 winnings,winning_lines=check_winnings(slot,lines,bet,symbol_values)
 print(f"you won ${winnings}")
 print(f"you won on lines:",*winning_lines)
 return winnings-total_bet






def main():
 balance=deposit()
 while True:
   print(f'current balance is ${balance}')
   answer=input("press enter to spin and q to quit")
   if answer=='q':
     break
   else:
     balance+=spin(balance)
 print(f"you are left with:${balance}")

 
main()