# Question 1
# What is the capital city of Japan?g
# C. Tokyo

# Question 2
# Who wrote the play Romeo and Juliet?
# William Shakespeare

# Question 3
# What is the capital of France?
# Paris

# Question 4
# What is the capital of Germany?
# Berlin

score = 0
name = input("Question 1. What is your name? ")
print(f"Welcome {name}")
answer = input("What is the capital city of Japan? ")
if answer == "Tokyo" or answer == "tokyo":
    score = score + 5
    print("Correct! Your score is:", score)
else:
    print("Incorrect. Your score is:", score)

answer = input("Question 2. Who wrote the play Romeo and Juliet? ")
if answer == "William Shakespeare" or answer == "william shakespeare":
    score = score + 5
    print("Correct! Your score is:", score)
else:
    print("Incorrect. Your score is:", score)
    
answer = input("Question 3. What is the capital of France? ")
if answer == "Paris" or answer == "paris":
    score = score + 5
    print("Correct! Your score is:", score)
else:
    print("Incorrect. Your score is:", score)

answer = input("Question 4. What is the capital of Germany? ")
if answer == "Berlin" or answer == "berlin":
    score = score + 5
    print("Correct! Your score is:", score)
else:
    print("Incorrect. Your score is:", score)
