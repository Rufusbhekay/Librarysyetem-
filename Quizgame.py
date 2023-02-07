playing = input("Welcome: Would you like to take quiz: ")

if playing != "yes":
    print ("bye")
    quit()

score = 0

answer = input("what does L stand for: ") 
if answer.lower() == "learn":
    print("correct!")
    score += 1
else: 
    print("incorrect")

answer = input("what does G stand for: ") 
if answer.lower() == "game":
    print("correct!")
    score += 1
else: 
    print("incorrect")

answer = input("what does J stand for: ") 
if answer.lower() == "jump":
    print("correct!")
    score += 1
else: 
    print("incorrect")

answer = input("what does U stand for: ") 
if answer.lower() == "under":
    print("correct!")
    score += 1
else: 
    print("incorrect")

answer = input("what does S stand for: ") 
if answer.lower() == "sun":
    print("correct!")
    score += 1
else: 
    print("incorrect")

print(f"You have got" + str(score) + "questions Correctly")
print(f"You got" + str((score/5) * 100 ) + "%")



