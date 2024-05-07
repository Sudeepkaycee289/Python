print("Welcome to my computer quiz")

playing = input("Do you want to play ? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's Play :)")
score = 0

# Quiz 1
answer = input("What does CPU stand for ? ")
if answer.lower() == "central processing unit":
    print('correct!')
    score +=1
else:
    print("Incorrect")

# Quiz 2
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score +=1
else:
    print("Incorrect")

# Quiz 3
answer = input("What is the full form of HTML? ")
if answer.lower() == "hypertext markup language":
    print('Correct!')
    score +=1
else:
    print("Incorrect")

# Quiz 4
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score +=1
else:
    print("Incorrect")

# Quiz 5
answer = input("What is the main function of an operating system? ")
if answer.lower() == "manage hardware and software resources":
    print('Correct!')
    score +=1
else:
    print("Incorrect")

# Quiz 6
answer = input("What does SSL stand for in the context of internet security? ")
if answer.lower() == "secure sockets layer":
    print('Correct!')
    score +=1
else:
    print("Incorrect")

# Quiz 7
answer = input("What does URL stand for? ")
if answer.lower() == "uniform resource locator":
    print('Correct!')
    score += 1
else:
    print("Incorrect")

# Quiz 8
answer = input("What is the purpose of DNS in computer networks? ")
if answer.lower() == "translate domain names to IP addresses":
    print('Correct!')
    score += 1
else:
    print("Incorrect")

# Quiz 9
answer = input("What does SQL stand for in database management? ")
if answer.lower() == "structured query language":
    print('Correct!')
    score += 1
else:
    print("Incorrect")

# Quiz 10
answer = input("What is the difference between HTTP and HTTPS? ")
if answer.lower() == "secure socket layer for encryption":
    print('Correct!')
    score += 1
else:
    print("Incorrect")

# Quiz 11
answer = input("What is the primary function of a router in a computer network? ")
if answer.lower() == "forward data between computer networks":
    print('Correct!')
    score += 1
else:
    print("Incorrect")

# Quiz 12
answer = input("What programming language is known for its simplicity and readability? ")
if answer.lower() == "python":
    print('Correct!')
    score += 1
else:
    print("Incorrect")

print("You got" + str(score) + "questions correct!")
print("You got" + str((score / 12)*100) + "%")
