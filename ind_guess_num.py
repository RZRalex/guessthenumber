import random as randomlib
random = randomlib.randint(1,100)
print('Guess a number between 1 and 100')
while True:
    guess = int(input())
    if guess < random:
        print('Too low, try again')
    elif guess > random:
        print('Too high, one more time')
    else:
        print ("Hey that's right!")
        break



