# Sort numbers (smallest ---> biggest)
numbers = [5,2,8,1,3]

for i in range(len(numbers)):
    for j in range(len(numbers)):
        if numbers[i] < numbers[j]:
            temp = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = temp
print(numbers)


# Reverse the list without using reverse function
numbers = [10, 20, 30, 40, 50]

reverse = [numbers[i] for i in range(len(numbers)-1, -1, -1)]
print(reverse)



# Task: Write code to sort this list in ascending order using bubble sort.
numbers = [9, 4, 6, 2, 8]

        


# Task: Sort the list in ascending order using selection sort.
numbers = [10, 3, 8, 4, 5]


     




# Task: Sort the list using insertion sort.
# Hint: Pick one element at a time and insert it in the correct position in the sorted part.
numbers = [10, 3, 8, 4, 5]




# Task: Create a new list that is the reverse of this list.
# Hint: Use a loop and index manipulation (don't use reverse() or [::-1] for now).
numbers = [1, 2, 3, 4, 5]






# Task 1: Find the largest number without using max().
# Task 2: Find the smallest number without using min().
numbers = [12, 7, 19, 3, 10]




# Task: Swap the two numbers without using a temporary variable.
# Hint: Use tuple assignment or arithmetic tricks.
numbers = [4, 9]





# Task: Sort the list from largest to smallest using any sorting algorithm you know.
numbers = [4, 9]





# Task: Create two sorted lists:
# 1. Even numbers sorted ascending
# 2. Odd numbers sorted ascending
numbers = [5, 2, 8, 1, 3, 6]






# Task: Count how many times each number occurs.
# Hint: Use loops and a dictionary or list.
numbers = [2, 3, 2, 4, 2, 5, 3]







# Task: Sort the words in alphabetical order without using sorted().
# Hint: Compare strings like numbers.     
words = ["banana", "apple", "grape", "orange"]




#Input a list of Numbers from user i.e take integer inputs and append to list.
#Find the smallest and Second Smallest Numbers from that list

user_input = input("Insert the numbers, separated with commas: ")
list1 = [int (i) for i in user_input.split(',')]

for i in range(len(list1)):
    for j in range(len(list1)-1):
        if list1[j] > list1[j+1]:
            list1[j],list1[j+1] = list1[j+1],list1[j]
print("Smallest number: ", list1[0])
print("Second smallest number: ", list1[1])
        






