# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(x):
   if (x % 2 == 0):
      return True
   else:
      return False

print(is_even(3))  

# Read a number from the keyboard
num = input("Enter a number: ")


def read_number(num):
   if num.isdigit():
      print(f' you hit number {num} on the keyboard')
   else:
      return print('not a number')
read_number(num)





# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
def number_even(n):
   if (n % 2 == 0):
      return print("number is Even")
   else:
      return print("number is odd")

number_even(3)