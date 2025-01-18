 #Task 1
#check_grade = int(input('score: '))
#if check_grade >= 90:
    #print('excellent')
#elif check_grade >= 50:
   #print('pass')
#else:
    #print('fail')

#Task 2
number = [1, 2, 3, 4,5, 6,7,8,9,10]
for num in number:
    num = num ** 2
    print(num)


#Task 3
total = 0
current = 1
while current <= 100:
    total = total + current
    current = current + 1
print(total)

#task 4
student_score = {'alice' : 85, 'bob' : 75, 'charlie' : 95}
def topstudent(scores): 
    return max(scores, key=scores.get )
print(topstudent(student_score))

#task 5
student_score = {'alice' : 85, 'bob' : 75, 'charlie' : 95}
student_score['David'] = 88
print(student_score)

#task 6
set_a = { 1, 2, 3,4,5}
set_b ={ 4,5,6,7,8}

print(set_a | set_b)
print(set_a & set_b)
print(set_a - set_b)

#task 7
number = list(range(1,21))
even_number = [ num for num in number
if num % 2 == 0 ]
print(even_number)

#Task 8
class_data = {
    'Class A': {'John': 85, 'Jane': 92, 'Tom': 78},
    'Class B': {'Alex': 88, 'Chris': 79, 'Emma': 91}
}

def average_score(class_data):
    for class_name, students in class_data.items():
        avg = sum(students.values()) / len(students)
        print(f"Average score in {class_name}: {avg}")
average_score(class_data)

#Task 9
def find_divisible_numbers(numbers, divisor):
    return [num for num in numbers if num % divisor == 0]
print(find_divisible_numbers(range(1, 21), 3))

#Task 10
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for element in row:
        print(element)

#Task 11
squares = {num: num ** 2 for num in range(1, 6)}
print(squares)

#Task 12
fruits = {'apple', 'banana', 'orange'}
fruits.add('mango')
fruits.remove('banana')
if 'apple' in fruits:
    print("Apple is in the set")
print(fruits)

#Task 13
def find_first_multiple(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            return i
    return "No multiple found"
print(find_first_multiple(30))

#Task 14
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 90, 78]

def combine_lists(names, scores):
    return dict(zip(names, scores)) 
print(combine_lists(names, scores))

#Task 15
def count_frequencies(words):
    return {word: words.count(word) for word in set(words)}

print(count_frequencies(['apple', 'banana', 'apple', 'orange', 'banana', 'apple']))

#Task 16
set_1 = {1, 2, 3, 4}
set_2 = {3, 4, 5, 6}
set_3 = {5, 6, 7, 8}

print(set_1 | set_2 | set_3) 
print(set_1 & set_2 & set_3) 
print(set_1 ^ set_2)    

#Task 17
students = [{'name': 'Alice', 'grade': 85}, {'name': 'Bob', 'grade': 90}, {'name': 'Charlie', 'grade': 78}]

def average_grade(students):
    return sum(student['grade'] for student in students) / len(students)

print(average_grade(students))

#Task 18
product_prices = {'apple': 1.5, 'banana': 0.5, 'orange': 0.8}

def get_price(product):
    return product_prices.get(product, 'Product not found')

print(get_price('apple'))

#Task 19
def filter_and_sort(numbers):
    return sorted([x for x in numbers if x >= 5], reverse=True)

print(filter_and_sort([3, 8, 1, 10, 4, 7]))

#Task 20
evens = {2, 4, 6, 8, 10}
odds = {1, 3, 5, 7, 9}
if evens & odds:
    print("Common element found:", evens & odds)
else:
    print("No common elements")














