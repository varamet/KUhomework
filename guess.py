import random
secret = random.randint(1,10)
round = 0
guess = 0
while guess != secret :
    round +=1
    guess = int(input(f"[{round}] Guess the number : "))
    if guess > secret :
        print(f"{guess} is too much")
    if guess < secret :
        print(f"{guess} is too little")
    elif guess == secret :
        print(f"{guess} is correct")
print(f"you take {round} turns")