

print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
print("Okay! let's play :)")
score = 0

answer = input("what does CPU stand for? ")
if answer.lower()  == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")   

answer = input("What does GPU stand for? ").lower()
if answer  == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")   

answer = input("What does RAM stand for? ")
if answer.lower()  == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")   

answer = input("What does PSU stand for ? ")
if answer.lower()  == "power supply":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")     


print(f'You got {score} questions correct!')   
print(f'You got {(score/4)*100}%')      