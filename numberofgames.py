#finding number of single games customer wants to buy
print("1-uncharted($10)  2-cyberpunk2077($20)  3-god of war($35)   4-sims4($23)")
print("enter the number of notes given")
num=int(input())
notes=[]
print("enter the note values")
for i in range(num):
    x=int(input())
    notes.append(x)
total=sum(notes)
print("enter your game number")
choice=int(input())
if choice==1:
    a=total/10
    a=int(a)
    print("you can buy",a,"games")
if choice==2:
    a=total/20
    a=int(a)
    print("you can buy", a, "games")
if choice==3:
    a=total/35
    a=int(a)
    print("you can buy", a, "games")
if choice==4:
    a=total/23
    a=int(a)
    print("you can buy", a, "games")





