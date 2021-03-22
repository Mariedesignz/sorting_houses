# This code is my variable for the four houses. Starting at zero adding on for each answer
gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

# varaible houses contains an empty list




q1_answer = input("Will you break the rules to help a friend? \na) yes \nb no \nc) maybe \nd) get lost")
if q1_answer == "a":
    gryffindor += 1
elif q1_answer == "b":
    ravenclaw += 1
elif q1_answer == "c":
    hufflepuff += 1
elif q1_answer == "d":
    slytherin += 1
else: 
    print("Sorry, I don't understand that answer.")        


q2_answer = input("How do you describe yourself? \na) brave \nb) timid \nc)superstar \nd)best of the best")
if q2_answer == "a":
    gryffindor += 1
elif q2_answer == "b":
    ravenclaw += 1
elif q2_answer == "c":
    hufflepuff += 1
elif q2_answer == "d":
    slytherin += 1
else: 
    print("Sorry, I don't understand that answer.")   

q3_answer = input("If you see a deatheater, what will you do? \na) fight \nb)run \nc) get help \d)run like crazy")
if q3_answer == "a":
    gryffindor += 1
elif q3_answer == "b":
    ravenclaw += 1
elif q3_answer == "c":
    hufflepuff += 1
elif q3_answer == "d":
    slytherin += 1
else: 
    print("Sorry, I don't understand that answer.")

q4_answer = input("Given the choice, would you rather invent a potionthat would guarantee you? \na) glory \b) wisdom \nc) love \nd) power") 
if q4_answer == "a":
    gryffindor += 1
elif q4_answer == "b":
    ravenclaw += 1
elif q4_answer == "c":
    hufflepuff += 1
elif q4_answer == "d":
    slytherin += 1
else: 
    print("Sorry, I don't understand that answer.")

q5_answer = input("How would you like to be known to history? \na) The Wise \nb) The good \c) The bold \nd) The great")
if q5_answer == "a":
    gryffindor += 1
elif q5_answer == "b":
    ravenclaw += 1
elif q5_answer == "c":
    hufflepuff += 1
elif q5_answer == "d":
    slytherin += 1
else: 
    print("Sorry, I don't understand that answer.")

q6_answer = input("What kind of instrument most pleases the ear? \na) Vilon \nb) Drums \nc) Piano \nd Trumpet")
if q6_answer == "a":
    gryffindor += 1
elif q6_answer == "b":
    ravenclaw += 1
elif q6_answer == "c":
    hufflepuff += 1
elif q6_answer == "d":
    slytherin += 1
else: 
    print("Sorry, I don't understand that answer.")

q7_answer = input("Which of the following do you find most difficult to deal with? \na) Hunger \nb) Cold \nc) Bordedom \nd) Being ignored")
if q7_answer == "a":
    gryffindor += 1
elif q7_answer == "b":
    ravenclaw += 1
elif q7_answer == "c":
    hufflepuff += 1
elif q7_answer == "d":
    slytherin += 1
else: 
    print("Sorry, I don't understand that answer.")

q8_answer = input("Which would you rather be? \na) Trusted \nb) Liked \nc) Envied \nd) Imitated")
if q8_answer == "a":
    gryffindor += 1
elif q8_answer == "b":
    ravenclaw += 1
elif q8_answer == "c":
    hufflepuff += 1
elif q8_answer == "d":
    slytherin += 1
else: 
    print("Sorry, I don't understand that answer.")

q9_answer = input("Which road tempts you most? \na) The wide, sunny, grassy lane \nb) The narrow, dark, lantern-lit alley \nc The cobbled street lined with ancient  buildings \nd) None")
if q9_answer == "a":
    gryffindor += 1
elif q9_answer == "b":
    ravenclaw += 1
elif q9_answer == "c":
    hufflepuff += 1
elif q9_answer == "d":
    slytherin += 1
else: 
    print("Sorry, I don't understand that answer.")

q10_answer = input("If you could have any power, which would you choose? \na) The power to read minds \nb) The power of invisibility \nc) The power of superhuman strength \nd) The power to chnage the past")
if q10_answer == "a":
    gryffindor += 1
elif q10_answer == "b":
    ravenclaw += 1
elif q10_answer == "c":
    hufflepuff += 1
elif q10_answer == "d":
    slytherin += 1
else: 
    print("Sorry, I don't understand that answer.")

if gryffindor > ravenclaw and gryffindor > hufflepuff and gryffindor > slytherin:
    print("Congrulations GRYFFINDOR is your house!")
elif ravenclaw > gryffindor and ravenclaw > hufflepuff and ravenclaw > slytherin:
    print("Congrulations RAVENCLAW is your house!")
elif hufflepuff > gryffindor and hufflepuff > slytherin:
    print("Congrulations HUFFLEPUFF is your house!")
elif slytherin > gryffindor and slytherin > ravenclaw and slytherin > hufflepuff:
    print("Congrulations SLYTHERIN is your house!")    
 


