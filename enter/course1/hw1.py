#quiz1
x = int(input("what is the sum of 4*2? "))
if x != 8:
    print("Try again!")
    x = int(input("What is the sum of 4*2? "))
if x == 8:
    print("Well done!")

#quiz2
x = int(input("Guess right 3+1? "))
if x != 4:
    print("Nope!")
    x = int(input("Guess right 3+1? "))
if x == 4:
    print("Fantastic!")

#quiz3
x = input("what is the capital of Russia? ")
if x != 'Moscow':
    print("Not at all!")
    x = input("What is the capital of Russia? ")
if x == 'Moscow':
    print("Great answer!")