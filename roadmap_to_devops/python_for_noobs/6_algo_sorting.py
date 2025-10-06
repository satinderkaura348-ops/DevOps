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
     
