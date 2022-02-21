import random
print("welcome to mastermind only one of each color")
colist=["red","green","yellow","blue","white","black"]
print("Colours: ", colist)
x=colist[random.randrange(0,5)]
y=colist[random.randrange(0,5)]
while y==x:
    y=colist[random.randrange(0,5)]
z=colist[random.randrange(0,5)]
while y==z or x==z:
    z=colist[random.randrange(0,5)]
a=colist[random.randrange(0,5)]
while a==z or a==y or a==x:
    a=colist[random.randrange(0,5)]
password=[x,y,z,a]
b=input("First colour: ")
c=input("Second colour: ")
d=input("Third colour: ")
e=input("Fourth colour: ")
scolist=[]
while b!=x or c!=y or d!=z or e!=a:
    if b==x:
        scolist.append("black")
    elif password.count(b)==1:
        scolist.append("white")
    else:
        scolist.append("none")
    if c==y:
        scolist.append("black")
    elif password.count(c)==1:
        scolist.append("white")
    else:
        scolist.append("none")
    if d==z:
        scolist.append("black")
    elif password.count(d)==1:
        scolist.append("white")
    else:
        scolist.append("none")
    if e==a:
        scolist.append("black")
    elif password.count(e)==1:
        scolist.append("white")
    else:
        scolist.append("none")
    random.shuffle(scolist)
    print(scolist)
    scolist.clear()
    b=input("First colour: ")
    c=input("Second colour: ")
    d=input("Third colour: ")
    e=input("Fourth colour: ")
else:
    print("Congrats! You have guessed the code")
