import random

easy_words= ["apple", "train", "pilot", "house", "green"]
medium_words = ["python", "jumble", "garden", "window", "laptop"]
hard_words = ["jupitar", "cyber", "monocrome", "diamond", "milkyway"]

print("Welcome to the Guessing Game!")
print("Choose a difficulty level: easy, medium, hard")

level = input("Enter difficulty level: ").lower()

if level == "easy":
    word = random.choice(easy_words)
elif level == "medium":
    word = random.choice(medium_words)
elif level == "hard":
    word = random.choice(hard_words)
else:
    print("Invalid level selected. Defaulting to easy.")
    word = random.choice(easy_words)
    
attempts = 0
print("Guess the secret password!")

while True:
    guess = input("Enter your guess: ").lower()
    attempts += 1
    
    if guess == word:
        print(f"Congratulations! You've guessed the word '{word}' in {attempts} attempts.")
        break
    else:
        print("Incorrect guess. Try again!")
      
    hint = ""
    for i in range(len(word)):
        if i < len(guess) and guess[i] == word[i]:
            hint += guess[i]
        else:
            hint += "*"
            
    print(f"Hint: {hint}")     
print("Tata, Game over!☺")          
