import random
import constant 


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

    q1_answer = input("Will you break the rules to help a friend? \na) yes \nb) no \nc) maybe \nd) get lost\n")
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



    q2_answer = input("How do you describe yourself? \na) brave \nb) timid \nc)superstar \nd)best of the best\n")
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

q4_answer = input("Given the choice, would you rather invent a potionthat would guarantee you? \na) glory \nb) wisdom \nc) love \nd) power\n") 
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

q6_answer = input("What kind of instrument most pleases the ear? \na) Vilon \nb) Drums \nc) Piano \nd Trumpet\n")
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

q9_answer = input("Which road tempts you most? \na) The wide, sunny, grassy lane \nb) The narrow, dark, lantern-lit alley \nc The cobbled street lined with ancient  buildings \nd) None\n")
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

q10_answer = input("If you could have any power, which would you choose? \na) The power to read minds \nb) The power of invisibility \nc) The power of superhuman strength \nd) The power to chnage the past\n")
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

if gryffindor > ravenclaw and gryffindor > hufflepuff and gryffindor > slytherin:
    print("Congrulations GRYFFINDOR is your house!")
elif ravenclaw > gryffindor and ravenclaw > hufflepuff and ravenclaw > slytherin:
    print("Congrulations RAVENCLAW is your house!")
elif hufflepuff > gryffindor and hufflepuff > slytherin:
    print("Congrulations HUFFLEPUFF is your house!")
elif slytherin > gryffindor and slytherin > ravenclaw and slytherin > hufflepuff:
    print("Congrulations SLYTHERIN is your house!")    
 

