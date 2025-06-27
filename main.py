import gamedata
import random

print("Welcome to Higher/Lower Game ")

randceleb2 = random.choice(gamedata.celebrities)

cont=1
counter=0
while cont==1:
    randceleb1=randceleb2
    randceleb2=random.choice(gamedata.celebrities)

    print(f"Compare A: {randceleb1["name"]}, a {randceleb1["profession"]} ")
    print(f"Compare B: {randceleb2["name"]}, a {randceleb2["profession"]} ")

    userinput=input("Who has more followers, Type A or B :")



    if userinput == "A" or 'a' and randceleb1["follower_count"] > randceleb2["follower_count"]:
        print("You are correct!")
        cont=1
        counter+=1

    elif userinput=='A' or 'a' and randceleb1["follower_count"] < randceleb2["follower_count"]:
        print("You are incorrect!")
        cont=0

    elif userinput=='B' or 'b' and randceleb1["follower_count"] > randceleb2["follower_count"]:
        print("You are incorrect!")
        cont=0

    elif userinput=='B' or 'b' and randceleb1["follower_count"] < randceleb2["follower_count"]:
        print("You are correct!")
        cont=1
        counter += 1


print(f"Your total score is {counter}")
