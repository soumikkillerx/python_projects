import random

def roll():
    min_value=1
    max_value=6
    roll=random.randint(min_value,max_value)
    return roll

while True:
    
    players=int(input("enter number of players(2-4) :  "))
    if  (4>=players>=2):
        break
    else:
        print("Invalid input")
        
        
max_score=50
current_score=0
player_score=[0 for i in range(players)]
print(player_score)
while max(player_score)<max_score:
    
    for player_index in range(players):
        print("\n player",player_index+1,"turn has started \n")
        print("your total score is ",player_score[player_index])
        
        while True:
            should_roll=input("would u like to roll (y) ?")
            if should_roll.lower()!="y":
                break
        
            value=roll()
            if value==1:
                print("you rolled a 1 ! turn down ")
                current_score=0
            else:
                current_score+=value
                print(f"you rolled {value}")
                
                
            
            print("current score is:",current_score)

        player_score[player_index]+=current_score
        print("your total score is :",player_score[player_index])


max_score=max(player_score)
wining_index=player_score.index(max_score)
print("player number",wining_index+1,"is the winner of",max_score)