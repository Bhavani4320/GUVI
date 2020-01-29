import random
n = random.randint(1, 99)
g = int(input("Enter an integer from 1 to 99: "))
while n != "guess":
    print
    if g < n:
        print ("guess is low")
        g = int(input("Enter an integer from 1 to 99: "))
    elif g > n:
        print ("guess is high")
        g = int(input("Enter an integer from 1 to 99: "))
    else:
        print ("you guessed it!")
        break
    print("!!!!!!!!game over!!!!!!!!!")




