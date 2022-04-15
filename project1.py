print("welcome to my computer quiz!")
playing=input("do you want to play? ")
if playing.lower() !="yes":
    quit()
print("okay! Let's play :)")  
score=0  
answer=input("what does cpu stands for? ")
if answer.lower()=="central processing unit":
    print('correct!')
    score+=1
else:
    print("incorrect!")
answer=input("what does Ram stands for? ")
if answer.lower()=="random access memory":
    print("correct!")
    score+=1
else:
    print("incorrect") 
answer=input("what is the full form of GUI? ")
if answer.lower()=="graphical user interface":
    print("correct!")
    score+=1
else:
    print("Incorrect!")
answer=input("what is the full form of PSU? ")
if answer.lower()=="power supply":               
 print("correct!")
 score+=1
else:
    print("incorrect")
answer=input("what does Rom stands for? ")
if answer.lower()=="read only memory":
    print("correct!")
    score+=1
else:
    print("Incorrect!") 
print("you got " + str(score) + " question correct! ") 
print("you got " + str((score/5)*100) +" %")          