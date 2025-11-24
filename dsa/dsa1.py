# List and Arrays
my_list = [3, 45, 6, 1, 6, 8, -9]
minVal = my_list[0]

for i in my_list:
    if i < minVal:
        minVal = i

print("Minimum value in the list is:", minVal)

# Find the maximum value in the list
maxVal = my_list[0]
for i in my_list:
    if i > maxVal:
        maxVal = i