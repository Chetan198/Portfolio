import random
lower=int(input("enter lower limit no"))
upper=int(input("enter upper limit no"))
random=random.randint(lower,upper)
print("You will have to choose a number between",lower,"and",upper)
chances=0
while chances<8:
    chances+=1
    guess=int(input("enter your guess"))
    if random==guess:
        print("congo!!you guessed the right no")
    elif random<guess:
        print("you guess larger no")
    elif random>guess:
        print("you guess smaller no")
    if chances == 7:
        print("\n You've run out of chances")
        print("\n The number was", random)
        print("Betterluck next time")
        break
random