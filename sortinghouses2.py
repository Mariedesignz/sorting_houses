import constant 
import random 
import json
# Meets conditon to read data from an external file
with open("questions.json", "r") as read_file:
        Defaultquestions = json.load(read_file)
 # Meets second requiremnt to create and pull information from a dictionary       
question_1 = Defaultquestions["Q1"]
question_2 = Defaultquestions["Q2"]       

# created a constant to make code DRY
# imported random so questions will be asked in random orders

# This code is my variable for the four houses. Starting at zero adding one for each answer
gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

# created a function to return the value of the answer plus one
def q1():
    gryffindor = 0
    ravenclaw = 0
    hufflepuff = 0
    slytherin = 0

    q1_answer = input(question_1 + " \na) yes \nb) no \nc) maybe \nd) get lost\n")
    if q1_answer == "a":
        gryffindor += 1
    elif q1_answer == "b":
        ravenclaw += 1
    elif q1_answer == "c":
        hufflepuff += 1
    elif q1_answer == "d":
        slytherin += 1
    else: 
        print(constant.DU)
    return gryffindor, ravenclaw, hufflepuff, slytherin

gryffindor, ravenclaw, hufflepuff, slytherin = q1()
print(f"gryffindor score = {gryffindor}")
print(f"ravenclaw score = {ravenclaw}")
print(f"hufflepuff score = {hufflepuff}")
print(f"slytherin score = {slytherin}")


def q2():
    gryffindor = 0
    ravenclaw = 0
    hufflepuff = 0
    slytherin = 0

    q2_answer = input(question_2 + "\na) brave \nb) timid \nc)superstar \nd)best of the best\n")
    if q2_answer == "a":
        gryffindor += 1
    elif q2_answer == "b":
        ravenclaw += 1
    elif q2_answer == "c":
        hufflepuff += 1
    elif q2_answer == "d":
        slytherin += 1
    else: 
        print(constant.DU)
    return gryffindor, ravenclaw, hufflepuff, slytherin
gryffindor, ravenclaw, hufflepuff, slytherin = q2()
print(f"gryffindor score = {gryffindor}")
print(f"ravenclaw score = {ravenclaw}")
print(f"hufflepuff score = {hufflepuff}")
print(f"slytherin score = {slytherin}")   
# my thrid function that meets the condition
def q3(): 
    gryffindor = 0
    ravenclaw = 0
    hufflepuff = 0
    slytherin = 0

    q3_answer = input("If you see a deatheater, what will you do? \na) fight \nb)run \nc) get help \nd)run like crazy\n")
    if q3_answer == "a":
        gryffindor += 1
    elif q3_answer == "b":
        ravenclaw += 1
    elif q3_answer == "c":
        hufflepuff += 1
    elif q3_answer == "d":
        slytherin += 1
    else: 
        print(constant.DU)
    return gryffindor, ravenclaw, hufflepuff, slytherin
gryffindor, ravenclaw, hufflepuff, slytherin = q2()
print(f"gryffindor score = {gryffindor}")
print(f"ravenclaw score = {ravenclaw}")
print(f"hufflepuff score = {hufflepuff}")
print(f"slytherin score = {slytherin}")   

    
   

def q4():
    gryffindor = 0
    ravenclaw = 0
    hufflepuff = 0
    slytherin = 0

    q4_answer = input("Given the choice, would you rather invent a potion that would guarantee you? \na) glory \nb) wisdom \nc) love \nd) power\n") 
    if q4_answer == "a":
        gryffindor += 1
    elif q4_answer == "b":
        ravenclaw += 1
    elif q4_answer == "c":
        hufflepuff += 1
    elif q4_answer == "d":
        slytherin += 1
    else: 
        print(constant.DU)
    return gryffindor, ravenclaw, hufflepuff, slytherin
gryffindor, ravenclaw, hufflepuff, slytherin = q4()
print(f"gryffindor score = {gryffindor}")
print(f"ravenclaw score = {ravenclaw}")
print(f"hufflepuff score = {hufflepuff}")
print(f"slytherin score = {slytherin}")   

def q5():
    gryffindor = 0
    ravenclaw = 0
    hufflepuff = 0
    slytherin = 0


    q5_answer = input("How would you like to be known to history? \na) The Wise \nb) The good \nc) The bold \nd) The great\n")
    if q5_answer == "a":
       gryffindor += 1
    elif q5_answer == "b":
       ravenclaw += 1
    elif q5_answer == "c":
       hufflepuff += 1
    elif q5_answer == "d":
        slytherin += 1
    else: 
        print(constant.DU)
    return gryffindor, ravenclaw, hufflepuff, slytherin
gryffindor, ravenclaw, hufflepuff, slytherin = q5()
print(f"gryffindor score = {gryffindor}")
print(f"ravenclaw score = {ravenclaw}")
print(f"hufflepuff score = {hufflepuff}")
print(f"slytherin score = {slytherin}")   

def q6():
    gryffindor = 0
    ravenclaw = 0
    hufflepuff = 0
    slytherin = 0

    q6_answer = input("What kind of instrument most pleases the ear? \na) Violin \nb) Drums \nc) Piano \nd Trumpet\n")
    if q6_answer == "a":
        gryffindor += 1
    elif q6_answer == "b":
        ravenclaw += 1
    elif q6_answer == "c":
        hufflepuff += 1
    elif q6_answer == "d":
        slytherin += 1
    else: 
        print(constant.DU)
    return gryffindor, ravenclaw, hufflepuff, slytherin
gryffindor, ravenclaw, hufflepuff, slytherin = q6()
print(f"gryffindor score = {gryffindor}")
print(f"ravenclaw score = {ravenclaw}")
print(f"hufflepuff score = {hufflepuff}")
print(f"slytherin score = {slytherin}")  

def q7():
    gryffindor = 0
    ravenclaw = 0
    hufflepuff = 0
    slytherin = 0

    q7_answer = input("Which of the following do you find most difficult to deal with? \na) Hunger \nb) Cold \nc) Bordedom \nd) Being ignored\n")
    if q7_answer == "a":
        gryffindor += 1
    elif q7_answer == "b":
        ravenclaw += 1
    elif q7_answer == "c":
        hufflepuff += 1
    elif q7_answer == "d":
        slytherin += 1
    else: 
        print(constant.DU)
    return gryffindor, ravenclaw, hufflepuff, slytherin
gryffindor, ravenclaw, hufflepuff, slytherin = q7()
print(f"gryffindor score = {gryffindor}")
print(f"ravenclaw score = {ravenclaw}")
print(f"hufflepuff score = {hufflepuff}")
print(f"slytherin score = {slytherin}")  

def q8():
    gryffindor = 0
    ravenclaw = 0
    hufflepuff = 0
    slytherin = 0

    q8_answer = input("Which would you rather be? \na) Trusted \nb) Liked \nc) Envied \nd) Imitated\n")
    if q8_answer == "a":
       gryffindor += 1
    elif q8_answer == "b":
       ravenclaw += 1
    elif q8_answer == "c":
        hufflepuff += 1
    elif q8_answer == "d":
        slytherin += 1
    else: 
        print(constant.DU)
    return gryffindor, ravenclaw, hufflepuff, slytherin
gryffindor, ravenclaw, hufflepuff, slytherin = q8()
print(f"gryffindor score = {gryffindor}")
print(f"ravenclaw score = {ravenclaw}")
print(f"hufflepuff score = {hufflepuff}")
print(f"slytherin score = {slytherin}")  

def q9():
    gryffindor = 0
    ravenclaw = 0
    hufflepuff = 0
    slytherin = 0

    q9_answer = input("Which road tempts you most? \na) The wide, sunny, grassy lane \nb) The narrow, dark, lantern-lit alley \nc The cobbled street lined with ancient buildings \nd) None\n")
    if q9_answer == "a":
        gryffindor += 1
    elif q9_answer == "b":
        ravenclaw += 1
    elif q9_answer == "c":
        hufflepuff += 1
    elif q9_answer == "d":
        slytherin += 1
    else: 
        print(constant.DU)
    return gryffindor, ravenclaw, hufflepuff, slytherin
gryffindor, ravenclaw, hufflepuff, slytherin = q9()
print(f"gryffindor score = {gryffindor}")
print(f"ravenclaw score = {ravenclaw}")
print(f"hufflepuff score = {hufflepuff}")
print(f"slytherin score = {slytherin}") 

def q10():
    gryffindor = 0
    ravenclaw = 0
    hufflepuff = 0
    slytherin = 0

    q10_answer = input("If you could have any power, which would you choose? \na) The power to read minds \nb) The power of invisibility \nc) The power of superhuman strength \nd) The power to change the past\n")
    if q10_answer == "a":
        gryffindor += 1
    elif q10_answer == "b":
        ravenclaw += 1
    elif q10_answer == "c":
        hufflepuff += 1
    elif q10_answer == "d":
        slytherin += 1
    else: 
        print(constant.DU)
    return gryffindor, ravenclaw, hufflepuff, slytherin
gryffindor, ravenclaw, hufflepuff, slytherin = q10()
print(f"gryffindor score = {gryffindor}")
print(f"ravenclaw score = {ravenclaw}")
print(f"hufflepuff score = {hufflepuff}")
print(f"slytherin score = {slytherin}") 


if gryffindor > ravenclaw and gryffindor > hufflepuff and gryffindor > slytherin:
    print("Congrulations GRYFFINDOR is your house!")
elif ravenclaw > gryffindor and ravenclaw > hufflepuff and ravenclaw > slytherin:
    print("Congrulations RAVENCLAW is your house!")
elif hufflepuff > gryffindor and hufflepuff > slytherin:
    print("Congrulations HUFFLEPUFF is your house!")
elif slytherin > gryffindor and slytherin > ravenclaw and slytherin > hufflepuff:
    print("Congrulations SLYTHERIN is your house!") 

   
 

