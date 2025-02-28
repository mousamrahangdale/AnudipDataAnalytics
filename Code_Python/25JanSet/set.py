# 1
fruits = {'apple', 'banana', 'cherry'}
print('apple' in fruits)

# 2
numbers = {10, 20, 30, 40, 50}
print(len(numbers))

# 3
numbers_list = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers_list)
print(unique_numbers) 

# 4
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common_elements = set(list1) & set(list2)
print(common_elements) 

# 5
string = "programming"
unique_chars = set(string)
print(unique_chars) 

# 6
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union = set1 | set2
print(union)

# 7
A = {'a', 'b', 'c'}
B = {'b', 'c', 'd'}
intersection = A & B
print(intersection)

# 8
X = {1, 2, 3, 4}
Y = {3, 4, 5, 6}
difference = X - Y
print(difference)
