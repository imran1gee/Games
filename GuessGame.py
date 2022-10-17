import random
print("Guess number from 1 to 100")
guess = int(input("What is your guess?:   "))
correct_number = random.randint(1,100)
number_attempt = 1;

while guess != correct_number:
  number_attempt +=1
  if guess>correct_number:
    print("Please guess lower number")
    guess = int(input("What is your guess?:   "))
  else:
       print("Please guess upper number")
       guess = int(input("What is your guess?:   "))
    
print(f"your guess is correct, {correct_number}. It took {number_attempt} attempts")