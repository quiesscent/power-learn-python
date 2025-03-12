"""
Challenges
Write a program that accepts user input to create a list of integers. Then, compute the sum of all the integers in the list.
Create a tuple containing the names of five of your favorite books. Then, use a for loop to print each book name on a separate line.
Write a program that uses a dictionary to store information about a person, such as their name, age, and favorite color. Ask the user for input and store the information in the dictionary. Then, print the dictionary to the console.
Write a program that accepts user input to create two sets of integers. Then, create a new set that contains only the elements that are common to both sets.
Create a program that stores a list of words. Then, use list comprehension to create a new list that contains only the words that have an odd number of characters.
"""

# challenge 1
counter = 0
my_list = []
while counter <= 5:
    num = int(input("Enter nuumbers: "))
    my_list.append(num)
    counter += 1


sum = 0
for num in my_list:
    sum += num

print(f"The sum of {my_list} is {sum}")

# challenge 2
favourite_book = ("Books 1", "Books 2", "Books 3", "Books 4", "Books 5")
for book in favourite_book:
    print(book)

# challenge 3

name = input("Enter your name: ")
age = int(input("Enter your age: "))
color = input("Enter your favourite color: ")

person_details = {}
person_details["name"] = name
person_details["age"] = age
person_details["color"] = color
print(f"Your details are { person_details }")

# challenge 4

set_1 = {}
set_2 = {}

counter_1 = 0
counter_2 = 0
while counter_1 <= 5:
    num = int(input("Enter number"))
    set_1.add(num)
    counter_1 += 1

print(set_1)
while counter_2 <= 5:
    num = int(input("Enter number"))
    set_1.add(num)
    counter_2 += 1

print(set_2)

print("The union is ",  set_1 & set_2 )

# challenge 5
words = {}
counter = 0
while counter <= 5:
    word = input("Enter word: ")
    set_1.add(word)
    counter += 1

odd_length_words = [word for word in words if len(word) % 2 == 1]


"""
Assignments
Create an empty list called my_list.
Append the following elements to my_list: 10, 20, 30, 40.
Insert the value 15 at the second position in the list.
Extend my_list with another list: [50, 60, 70].
Remove the last element from my_list.
Sort my_list in ascending order.
Find and print the index of the value 30 in my_list.
"""


my_list = []

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

my_list[1] = 15

list_2 = [50, 60, 70]

my_list.extend(list_2)

my_list.pop()

my_list.sort()


index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)
