# 1
cubes = {i: i**3 for i in range(1, 6)}
print(cubes)

# 2
student = {'name': 'John', 'age': 22, 'grade': 'A'}
print(student['name'])
student['grade'] = 'A+'
print(student)

# 3
inventory = {'apples': 10, 'bananas': 5}
inventory['oranges'] = 7
del inventory['bananas']
print(inventory)

# 4
scores = {'Alice': 85, 'Bob': 90, 'Charlie': 88}
print('David' in scores) 

# 5
student = {'name': 'John', 'age': 22, 'grade': 'A'}
for key, value in student.items():
    print(f"{key}: {value}")

# 6
dic1 = {'a': 1, 'b': 2}
dic2 = {'c': 3, 'd': 4}
merged_dic = {**dic1, **dic2}
print(merged_dic)

# 7
squares = {i: i**2 for i in range(1, 11)}
print(squares)

# 8
even_squares = {i: i**2 for i in range(1, 11) if i % 2 == 0}
print(even_squares)

# 9
original_dic = {'a': 1, 'b': 2, 'c': 3}
reversed_dic = {value: key for key, value in original_dic.items()}
print(reversed_dic)

# 10
char_frequency = {char: 'programming'.count(char) for char in 'programming'}
print(char_frequency)

# 11
nested_dict = {i: {j: i * j for j in range(1, 4)} for i in range(1, 4)}
print(nested_dict)

# 12
keys = ['name', 'age', 'city']
values = ['Alice', 25, 'New York']
zipped_dict = {k: v for k, v in zip(keys, values)}
print(zipped_dict)
    
# 13
multiplication_table = {i: 5 * i for i in range(1, 11)}
print(multiplication_table)   

# 14
data = [('a', 10), ('b', 20), ('c', 30)]
dic_list = {key: value for key, value in data}
print(dic_list)
