'''
5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
Once 'done' is entered, print out the largest and smallest of the numbers.
If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number.
Enter 7, 2, bob, 10, and 4 and match the output below.
'''


'''
Invalid input
Maximum is 10
Minimum is 2
'''

'''
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    print(num)

print("Maximum", largest)
'''


largest = None
smallest = None
#print('Before:', largest)
while True:
    snum = input("Enter a number: ")
    #BreakOut
    if snum == "done" :
        break
    #Error Detection
    try:
        inum = int(snum)
    except:
        print('Invalid input')
    #Smallest value
    for smnum in snum:
        if smallest is None or inum < smallest:
            smallest = inum
        #Largest Value
    for lnum in snum:
        if largest is None or inum > largest:
            largest = inum

#Output
print('Maximum is', largest)
print('Minimum is', smallest)
