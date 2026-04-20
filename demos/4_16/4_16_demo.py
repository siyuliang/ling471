# Using a while loop, write code that will print the integers
# from 1 up to and including 10
# x = 1
# while x <= 10:
# # while x < 11:
#     print(x)
#     x = x + 1

# Create a list of integers from 1 up to and including 5
# and assign it to a variable
# a = [1, 2, 3, 4, 5]
# print(a)
# # Check if the number 10 is in it
# print(1 in a)

# Using a for loop, write code that will print the integers
# from 1 up to and including 10
# for i in range(1, 11):
#     print(i)
# Using a for loop, print out every character in the string 'ling471'
# s = 'ling471'
# for c in s:
#     print(c)
# Thinking activity: What would happen if you used “while True:” for a
# while loop? What about “while False:” and “for x in []”?
# i = 1
# loop = True
# while loop:
#     print('I am looping for', i, 'times')
#     i = i + 1
#     if i > 3:
#         loop = False

# while False:
#     print('Is this true?')

# for x in []:
#     print('What is for?', x)

# Create an empty dict

# # Add the pair 'a':1 to it

# Add the pair 1:'b' to it

# Check if 2 is in the dict

# Check if 'a' is in the dict

# Increase the value of 'a' to 2


# Using a for loop, modify an empty dict to have keys that are
# the integers 1 up to and including 4 and values that are the
# squares of the integers 1 up to and including 4
# (that is, 12, 22, 32, 42)


# Create a txt file with all lower case text and save it somewhere you can find
# Read that txt file in with Python
with open('lowercasetext.txt', 'r', encoding='utf-8') as f:
    s = f.read()

# Change all the text to uppercase
s_new = s.upper()

# Write the txt file back out to a new file
with open('uppercasetxt.txt', 'w', encoding='utf-8') as w:
    w.write(s_new)