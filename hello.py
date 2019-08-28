#print ('Python is both a pretty snake and a programming language')
my_name = "Hi, I'm Mozart1893. What's your name please?"
Welcome = "You're Welcome"
choose_number = "Kindly choose a number between 1000 and 1999"

print(my_name)
your_name = input ("First name: ")
print(Welcome + your_name)
print(choose_number)
x = input ("Choose a random number: ")
x = int(x)
if x < 1000:
    print("Error!!! The number must be more that 1000 and between 1000 and 1999")
elif x > 1999:
    print("Error!!! The number must be less that 1999 and between 1000 and 1999")
elif x < 1893:
    print("You almost got the magic number, your number is lower, Thanks for trying...")
elif x == 1893:
    print("Congrats!!! You got the magic number right, Thanks for trying...")
elif x > 1893:
    print("You almost got the magic number, your number is higher, Thanks for trying...")
