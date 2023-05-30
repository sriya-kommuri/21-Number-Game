import sys

def save():
    zzz=0
    file1=open("D:\Python\Class\gamerecord.txt","r")
    name=input("Enter your name: ")
    st=file1.read()
    words=st.split() #converting the data into a list
    for i in range(len(words)):
        if name==words[i]: #checking if the user exists
            file1=open("D:\Python\Class\gamerecord.txt","w")
            b=int(words[i+1]) #changing the char into a int for incrementing
            b+=1 #incrementing the score if the user is also existed
            c="%s"%b #changing the int into char 
            words[i+1]=c #the words[i+1] is the score which is already there
            string=""
            string=' '.join(words)  #joining the elements in a list with a space
            string=string+'\n' #if there is a new input it'll go next line
            file1.write(string) #writing into the file
            file1.close()
            zzz=1
        
    if zzz==0: #for new player
        file1=open("D:\Python\Class\gamerecord.txt","a")
        c=1
        l=[]
        l.append(c) #appending score into list
        file1.write(name) #writing the name into file
        file1.write(' {}\n'.format(l[0])) #writing integer as string into file because we can't write int into the file
        file1.close()
 
def scores(): #to print scores
    file1=open("D:\Python\Class\gamerecord.txt","r")
    st=file1.read() #reading all data into variable
    words=st.split() #splitting the data and storing them in a file
    print("\n--SCORES--")
    for i in range(0,len(words),2): #skipping one element because we r already printing it down
        print(words[i],"  ",words[i+1])
    file1.close()

def nearestMultiple(num):
    if num>=4:
        near=num+(4-(num%4)) #like if num=5,6,7 then near=8,if num=9,10,11,then near=12,i.e we get 4 multiple at last
    else:
        near=4
    return near

def lose1():
    print ("\n\nYOU LOSE !")
    print("Better luck next time !")
    scores()
    sys.exit(0)

def check(xyz):
    i=1
    while i<len(xyz): #checking if the numbers entered are consecutive
        if (xyz[i]-xyz[i-1])!=1:
            return False
        i+=1
    return True

def start1():
    xyz=[]
    last=0
    while True:
        print("Enter 'F' to take the first chance")
        print("Enter 'S' to take the second chance")
        chance=input('>')
        
        if chance=="F":
            while True:
                if last==20:
                    lose1()
                else:
                    print("\nYour Turn")
                    print("\nHow many numbers do you wish to enter?")
                    inp=int(input(">"))
                    
                    if inp>0 and inp<=3: #checking if given input is more than 0 and less than 3
                        comp=4-inp
                    else:
                        print("Wrong input. You are disqualifies from the game")
                        lose1()
                        
                    i,j=1,1
                    
                    print("Now enter the values")
                    while i<=inp:
                        a=input(">")
                        a=int(a)
                        xyz.append(a)
                        i+=1 #taking input of the numbers
                    
                    last=xyz[-1] #storing last digit of the input or last digit in list
                    
                    if check(xyz)==True: #checking if the inputs we gave are consecutive are not
                        if last==21:
                            lose1()
                        else:
                            while j<=comp: #if we give 1 input, computer will give 3, like that 2 & 2, 3 & 1
                                xyz.append(last+j) #computer giving consecutive integers as inputs
                                j+=1
                            print("Order of inputs after com[uter's turn are: ")
                            print(xyz) #printing list
                            last=xyz[-1] #again storing last digit 
                    else:
                        print("\nYou did not input consecutive integers")
                        lose1()
        
        elif chance=="S":
            comp=1
            last=0
            while last<20:
                j=1
                while j<=comp: #the computer gives the inputs
                    xyz.append(last+j) 
                    j+=1
                print("Order of inputs after computer's turn is:")
                print(xyz) #printing list after it's inputs
                if xyz[-1]==20:
                    lose1();
                    
                else:
                    print("\nYour turn")
                    print("How many numbers do you wish to enter?")
                    inp=input(">")
                    inp=int(inp) #converting into int
                    i=1
                    print("Enter your values")
                    while i<=inp:
                        xyz.append(int(input('>')))
                        i+=1
                    last=xyz[-1]
                    if check(xyz)==True: #checking if we entered consecutive integers
                        near=nearestMultiple(last)
                        comp=near-last
                        if comp==4:
                            comp=3 #this comp traces back to line 115
                        else:
                            comp=comp
                    else:
                        print("\nYou did not input consecutive integers")
                        lose1()
                            #return
            print("\nCongratulations !!!")     
            print("YOU WON !")
            anss=input("Do you want to save your game score(Yes/No): ")
            if anss=='Yes':
                save()
                scores()
                sys.exit(0)
            else:
                sys.exit(0)
        else:
            print("Wrong choice")

game=True 
while game==True:
    print("\nPlayer 2 is computer")
    print("Do you want to play the 21 number game? (Yes / No)")
    ans=input('>')
    if ans=="Yes":
        start1()
    else:
        print("Do you want to quit the game?(Yes / No)")
        nex=input(">")
        if nex=="Yes":
            print("You are quitting the game....")
            sys.exit(0)
        elif nex=="No":
            print("Continuing...")
        else:
            print("Wrong choice")
            