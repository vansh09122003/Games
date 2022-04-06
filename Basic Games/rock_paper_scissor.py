import random

def get_input():
    a=int(input("Enter following index to play"))
    if a<1 or a>3:
        print("Please enter a valid index")
        start()
    else:
        return a

dic1={1:"Rock",2:"Paper",3:"Scissor"}
print(dic1)
p1=get_input()
com=random.randrange(1,4)
print("Computer is "+dic1[com])
if com==p1:
    print("Draw")
elif p1==1 and com==2:
    print("Computer Wins")
elif p1==2 and com==3:
    print("Computer Wins")
elif p1==3 and com==1:
    print("Computer Wins")
elif p1==3 and com==2:
    print("Player Wins")
elif p1==2 and com==1:
    print("Player Wins")
elif p1==1 and com==3:
    print("Player Wins")
    
