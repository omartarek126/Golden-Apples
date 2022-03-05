import random
print("The rules of this game are simple..."
"\nYou have 3 bags, each bag contains 10 objects, you can take 1 to 5 objects from only one bag each turn, then it's the computer's turn to play, the last player to take the last object from the last bag wins. Can you beat the computer?\nCreated and coded by Omar Tarek.")
again=True
while(again):
  bag=["",10,10,10]
  winner=""
  turn=0
  print("--------------------------------------------------")
  print("Bag 1:",bag[1],"Objects ","Bag 2:",bag[2],"Objects ","Bag 3:",bag[3],"Objects")
  while(bag[1]>0 or bag[2]>0 or bag[3]>0):
    flag=False
    while(flag==False):
      while True:
        try:
         humanobj=int(input("Enter the number of objects you want to withdraw "))
         humanbag=int(input("Enter the bag you want to withdraw from "))
        except ValueError:
         print("Not a Number! Try again.")
         continue
        else:
         break 
      flag=True
      if(humanobj>5 or humanobj<1):
        print("Enter a valid number of objects(1-5)")
        flag=False
      if(humanbag<1 or humanbag>3 and flag==True):
        print("Enter a valid bag number(1-3)")
        flag=False
      if(humanbag<=3 and humanbag>=1 and flag==True):
        if(humanobj>bag[humanbag]): 
          print("You cannot remove this number")
          flag=False
    bag[humanbag]=bag[humanbag]-humanobj
    print("--------------------------------------------------")
    print("You took:",humanobj,"objects from bag:",humanbag)
    print("Bag 1:",bag[1],"Objects ","Bag 2:",bag[2],"Objects ","Bag 3:",bag[3],"Objects")
    print("--------------------------------------------------")
    turn+=1
    if(bag[1]==0 and bag[2]==0 and bag[3]==0):
      winner="human"
      break
    computerobj=random.randint(1,5)
    computerbag=random.randint(1,3)
    while(computerobj>bag[computerbag]):
      if(bag[computerbag]!=0):
        while(computerobj>bag[computerbag]):
          i=computerobj
          i-=1
          computerobj=random.randint(1,i)
      else:
        computerbag=random.randint(1,3)
    if(turn==1):
      computerbag=humanbag
      computerobj=5
      bagtouse=humanbag
    elif(turn==2 and 0<bag[bagtouse]<=5):
      computerbag=bagtouse
      computerobj=bag[bagtouse]
    elif(bag[1]>7 and bag[2]==1 and bag[3]==0):
      computerbag=1
      computerobj=bag[1]%7
    elif(bag[2]>7 and bag[1]==1 and bag[3]==0):
      computerbag=2
      computerobj=bag[2]%7
    elif(bag[1]>7 and bag[3]==1 and bag[2]==0):
      computerbag=1
      computerobj=bag[1]%7
    elif(bag[3]>7 and bag[1]==1 and bag[2]==0):
      computerbag=3
      computerobj=bag[3]%7
    elif(bag[2]>7 and bag[3]==1 and bag[1]==0):
      computerbag=2
      computerobj=bag[2]%7
    elif(bag[3]>7 and bag[2]==1 and bag[1]==0):
      computerbag=3
      computerobj=bag[3]%7
    elif(bag[1]+bag[2]<=11 and bag[1]==6 and bag[2]>1and bag[3]==0):
      computerbag=2
      computerobj=bag[2]
    elif(bag[1]+bag[2]<=11 and bag[2]==6 and bag[1]>1and bag[3]==0):
      computerbag=1
      computerobj=bag[1]
    elif(bag[2]+bag[3]<=11 and bag[2]==6 and bag[3]>1and bag[1]==0):
      computerbag=3
      computerobj=bag[3]
    elif(bag[2]+bag[3]<=11 and bag[3]==6 and bag[2]>1and bag[1]==0):
      computerbag=2
      computerobj=bag[2]
    elif(bag[1]+bag[3]<=11 and bag[1]==6 and bag[3]>1and bag[2]==0):
      computerbag=3
      computerobj=bag[3]
    elif(bag[1]+bag[3]<=11 and bag[3]==6 and bag[1]>1and bag[2]==0):
      computerbag=1
      computerobj=bag[1]
    elif(bag[1]==6 and bag[2]==1 and bag[3]==0):
      computerbag=1
      computerobj=5
    elif(bag[2]==6 and bag[1]==1 and bag[3]==0):
      computerbag=2
      computerobj=5
    elif(bag[1]==6 and bag[3]==1 and bag[2]==0):
      computerbag=1
      computerobj=5
    elif(bag[3]==6 and bag[1]==1 and bag[2]==0):
      computerbag=3
      computerobj=5
    elif(bag[2]==6 and bag[3]==1 and bag[1]==0):
      computerbag=2
      computerobj=5
    elif(bag[3]==6 and bag[2]==1 and bag[1]==0):
      computerbag=3
      computerobj=5
    elif(6>bag[1]>2 and 6>bag[2]>2 and bag[3]==0):
      rem=bag[1]-2
      computerbag=1
      computerobj=rem
    elif(6>bag[3]>2 and 6>bag[2]>2 and bag[1]==0):
      rem=bag[2]-2
      computerbag=2
      computerobj=rem
    elif(6>bag[3]>2 and 6>bag[1]>2 and bag[2]==0):
      rem=bag[3]-2
      computerbag=3
      computerobj=rem
    elif(bag[1]==2 and bag[2]>2 and bag[3]==0):
      rem=bag[2]-2
      computerbag=2
      computerobj=rem
    elif(bag[2]==2 and bag[1]>2 and bag[3]==0):
      rem=bag[1]-2
      computerbag=1
      computerobj=rem
    elif(bag[1]==2 and bag[3]>2 and bag[2]==0):
      rem=bag[3]-2
      computerbag=3
      computerobj=rem
    elif(bag[3]==2 and bag[1]>2 and bag[2]==0):
      rem=bag[1]-2
      computerbag=1
      computerobj=rem
    elif(bag[3]==2 and bag[2]>2 and bag[1]==0):
      rem=bag[2]-2
      computerbag=2
      computerobj=rem
    elif(bag[2]==2 and bag[3]>2 and bag[1]==0):
      rem=bag[3]-2
      computerbag=3
      computerobj=rem
    elif(bag[1]<=5 and bag[2]==0 and bag[3]==0):
      computerbag=1
      computerobj=bag[1]
    elif(bag[2]<=5 and bag[1]==0 and bag[3]==0):
      computerbag=2
      computerobj=bag[2]
    elif(bag[3]<=5 and bag[2]==0 and bag[1]==0):
      computerbag=3
      computerobj=bag[3]
    elif(bag[1]<=10 and bag[1]!=6 and bag[2]==0 and bag[3]==0):
      computerbag=1
      computerobj=bag[1]%6
    elif(bag[2]<=10 and bag[2]!=6 and bag[1]==0 and bag[3]==0):
      computerbag=2
      computerobj=bag[2]%6
    elif(bag[3]<=10 and bag[3]!=6 and bag[2]==0 and bag[1]==0):
      computerbag=3
      computerobj=bag[3]%6
    elif(bag[1]+bag[2]<=10 and bag[1]>=bag[2]and bag[2]>1and bag[3]==0):
      rem=bag[2]-1
      computerbag=2
      computerobj=rem
    elif(bag[1]+bag[2]<=10 and bag[2]>=bag[1]and bag[1]>1and bag[3]==0):
      rem=bag[1]-1
      computerbag=1
      computerobj=rem
    elif(bag[2]+bag[3]<=10 and bag[2]>=bag[3]and bag[3]>1and bag[1]==0):
      rem=bag[3]-1
      computerbag=3
      computerobj=rem
    elif(bag[2]+bag[3]<=10 and bag[3]>=bag[2]and bag[2]>1and bag[1]==0):
      rem=bag[2]-1
      computerbag=2
      computerobj=rem
    elif(bag[1]+bag[3]<=10 and bag[1]>=bag[3]and bag[3]>1and bag[2]==0):
      rem=bag[3]-1
      computerbag=3
      computerobj=rem
    elif(bag[1]+bag[3]<=10 and bag[3]>=bag[1]and bag[1]>1and bag[2]==0):
      rem=bag[1]-1
      computerbag=1
      computerobj=rem
    elif(bag[1]+bag[2]<=10and bag[1]<=5 and bag[1]>bag[2]and bag[2]==1and bag[3]==0):
      rem=bag[1]-1
      computerbag=1
      computerobj=rem
    elif(bag[1]+bag[2]<=10and bag[2]<=5 and bag[2]>bag[1]and bag[1]==1and bag[3]==0):
      rem=bag[2]-1
      computerbag=2
      computerobj=rem
    elif(bag[2]+bag[3]<=10and bag[2]<=5 and bag[2]>bag[3]and bag[3]==1and bag[1]==0):
      rem=bag[2]-1
      computerbag=2
      computerobj=rem
    elif(bag[2]+bag[3]<=10and bag[3]<=5 and bag[3]>bag[2]and bag[2]==1and bag[1]==0):
      rem=bag[3]-1
      computerbag=3
      computerobj=rem
    elif(bag[1]+bag[3]<=10and bag[1]<=5 and bag[1]>bag[3]and bag[3]==1and bag[2]==0):
      rem=bag[1]-1
      computerbag=1
      computerobj=rem
    elif(bag[1]+bag[3]<=10and bag[3]<=5 and bag[3]>bag[1]and bag[1]==1and bag[2]==0):
      rem=bag[3]-1
      computerbag=3
      computerobj=rem
    elif(bag[1]+bag[2]<=20 and bag[1]!=6and bag[1]>bag[2]and bag[3]==0):
      computerbag=1
      computerobj=bag[1]%6
    elif(bag[1]+bag[2]<=20 and bag[2]!=6and bag[2]>bag[1]and bag[3]==0):
      computerbag=2
      computerobj=bag[2]%6 
    elif(bag[2]+bag[3]<=20 and bag[2]!=6and bag[2]>bag[3]and bag[1]==0):
      computerbag=2
      computerobj=bag[2]%6 
    elif(bag[2]+bag[3]<=20 and bag[3]!=6and bag[3]>bag[2]and bag[1]==0):
      computerbag=3
      computerobj=bag[3]%6 
    elif(bag[1]+bag[3]<=20 and bag[1]!=6and bag[1]>bag[3]and bag[2]==0):
      computerbag=1
      computerobj=bag[1]%6
    elif(bag[1]+bag[3]<=20 and bag[3]!=6and bag[3]>bag[1]and bag[2]==0):
      computerbag=3
      computerobj=bag[3]%6
    bag[computerbag]=bag[computerbag]-computerobj
    print("Computer took:",computerobj,"objects from bag:",computerbag)
    print("Bag 1:",bag[1],"Objects ","Bag 2:",bag[2],"Objects ","Bag 3:",bag[3],"Objects")
    print("--------------------------------------------------")
  if(winner=="human"):
    print("Congratulations,You won")
  else:
    print("Hard luck, Computer won\nOr in other words, my code won ;)")
  print("Done")
  play=input("Play Again? Enter y, else enter n ")
  print("--------------------------------------------------")
  if(play=="n"):
    again=False
  