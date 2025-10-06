# Sort out the numbers in ascending order
list_of_num = [1,23,3,17,50,49,89,2]

for i in range(len(list_of_num)):
    for j in range(len(list_of_num)):
        if list_of_num[i] < list_of_num[j]:
            temp = list_of_num[i]
            list_of_num[i] = list_of_num[j]
            list_of_num[j] = temp

print(list_of_num)


# Find the largest number
numbers = [3,7,2,9,5]
largest = numbers[0]
for i in numbers:
    if i > largest:
        largest = i
print(largest)



# Find the smallest number
numbers = [4,12,7,1,9]
smallest = numbers[0]

for i in numbers:
    if i < smallest:
        smallest = i
print(smallest)



# Swap two numbers, without using third variable
a = 10
b = 5

a,b = b,a
print(a, b)






