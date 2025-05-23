# The Exercises here would take you out of your comfort zone, make a research on how to add an item to your list.
# Write a program to keep asking for a number until you enter a negative number. At the end, print the sum of all entered numbers.
# Write a program to ask for a name until the user enters END. Print the name each time. When you are done, print "I am done."
# Write a program to find the multiples of n, your loop should iterate 10 times.

numbers = [2, 5, 8, 3, 7]
total = 0
while True:
    number = int(input("Enter a number: "))
    numbers.insert(0, number)
    if number < 0:
        print("Negative number entered. Exiting the loop.")
        break
    total += numbers[0]
    print("Current list of numbers:", numbers)
print("The sum of all entered numbers is", total)

name = input("Enter a name: ")
while name != "END":
    print(name)
    name = input("Enter a name: ")
print("I am done.")
