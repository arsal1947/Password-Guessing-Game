'''
password guessing game
Conceppts we use
    loops
    strings
    conditionals
    variables
    lists
We have three levels
easy , meduim and hard
User chooses what he wants to take
'''

import random
easy_words = ["apple","train","tiger","money","dubai"]
medium_words = ["python" , "bottle" , "monkey" , "planet" , "laptop"]
hard_words = ["elephant","diamond","umbrella","computer","mountain"]

print("Welcome to the password guessing game")
print("Choose a difficulty level: Easy , Medium and Hard")

level = input("Enter difficulty: ").strip().lower()
if level == "easy":
    secret = random.choice(easy_words)
elif level == "medium":
    secret = random.choice(medium_words)
elif level == "hard":
    secret = random.choice(hard_words)
else:
    print("Invalid choice. Defaulting to easy level")
    secret = random.choice(easy_words)
    
attempts = 0
print("\nGuess the password: ")

while True:
    guess = input("Enter the guess: ").strip().lower()
    attempts += 1
     
    if guess == secret:
        print(f"Congratulations! You guess it im {attempts} attempts")   
        break

    hint = ""
    
    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint += guess[i]
            
        else:
            hint += "_"
            
    print("Hint: ", hint)
    print("Game Over")













































































