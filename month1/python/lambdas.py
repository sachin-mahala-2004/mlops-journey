# Exercise 1: Use map to convert a list of strings to integers
strings = ["1", "2", "3", "4", "5"]
str_to_int = list(map(int,strings))
print(str_to_int)

# Exercise 2: Use filter to get only positive numbers
numbers = [-3, -1, 0, 2, 5, -7, 8, 0, 3]
pos_num = list(filter(lambda x: x>=0 , numbers))
print(pos_num)

# Exercise 3: Use map to get string lengths
words = ["python", "is", "awesome", "for", "mlops"]
str_len = list(map(lambda x: len(x),words))
print(str_len)

# Exercise 4: Use lambda + sorted to sort by string length
words = ["banana", "apple", "kiwi", "mango", "strawberry"]
sorted_ = sorted(words,key=lambda x : len(x))
print(sorted_)

# Exercise 5: Filter students with score above 60 using filter + lambda
students = [("Alice", 85), ("Bob", 42), ("Charlie", 91), ("Dave", 38)]
filt = list(filter(lambda x:x[1]>60,students))
print(filt)

# Exercise 6: Use map to round each float to 2 decimal places
floats = [3.14159, 2.71828, 1.41421, 1.73205]
two_deci = list(map(lambda x: round(x,2),floats))
print(two_deci)

# Exercise 7: Chain map + filter — square only even numbers
numbers = list(range(1, 11))
sqr_even = list(map(lambda x:x**2,filter(lambda x:x%2==0,numbers)))
print(sqr_even)

# Exercise 8: Use lambda to sort a list of dicts by 'age'
people = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}, {"name": "Charlie", "age": 35}]
srt_by_age = sorted(people,key=lambda x: x["age"])
print(srt_by_age)

# Exercise 9: Use filter to get words that start with a vowel
words = ["apple", "banana", "orange", "grape", "umbrella", "cherry"]
words_vowels = list(filter(lambda x: x[0] in "aeiou",words))
print(words_vowels)

# Exercise 10: Use map to add index to each item as a tuple
items = ["a", "b", "c", "d"]
c=0
tuple_idx = list(map(lambda x : (items.index(x),x) ,items))
print(tuple_idx)
#or 
tuple_idx = list(map(lambda i,item: (i,item),range(len(items)),items))
print(tuple_idx)
#map() can take multiple iterables:
#map(function, iterable1, iterable2)