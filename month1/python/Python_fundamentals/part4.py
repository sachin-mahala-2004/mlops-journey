# Unzip — convert pairs back to separate lists
pairs  = [('Alice', 85), ('Bob', 42), ('Charlie', 91)]
names,scores = zip(*pairs)
print(names,scores)

# Create a dict from two lists (very common pattern)
keys   = ["name", "age", "city"]
values = ["Arjun", 20, "Jaipur"]
info = dict(zip(keys,values))
print(info)

#enumerate 
# start form a different number
for i , key in enumerate(keys, start=1):
    print(f"{i}. {key}")
    
#sorted
# Sort strings
words = ["banana", "Ppple", "cherry", "date"]
print(sorted(words))             # (uppercase first!)
print(sorted(words, key=str.lower))  #case-insensitive


numbers = [3, 1, 4, 1, 5, 9, 2, 6]
asc  = sorted(numbers)             # [1, 1, 2, 3, 4, 5, 6, 9]
desc = sorted(numbers, reverse=True) # [9, 6, 5, 4, 3, 2, 1, 1]


#any() and all()

#any() --> true if at least one item is trutly
# all() → True if ALL items are truthy

numbers = [0, 1, 2, 3]
print(any(numbers))   # True  — because 1, 2, 3 are truthy
print(all(numbers))   # False — because 0 is falsy

# Exercises 
# Exercise 1: Use zip to pair questions with answers
questions = ["Capital of France?", "2 + 2?", "Color of sky?"]
answers   = ["Paris", "4", "Blue"]
for question ,answer in zip(questions,answers):
    print(f"Q: {question} | A: {answer}")

# Exercise 2: Use enumerate to print a numbered menu
menu = ["Start Game", "Load Game", "Settings", "Quit"]
for i, m in enumerate(menu,start=1):
    print(f"{i}. {m}")
    
# Exercise 3: Sort these dicts by price (cheapest first)
products = [{"name": "Phone", "price": 699}, {"name": "Laptop", "price": 999}, {"name": "Cable", "price": 9}]
sort = sorted(products,key= lambda x :x["price"])
print(sort)

# Exercise 4: Check if ALL scores are above 40 (passing)
scores = [85, 42, 91, 38, 70]
is_true = all(score>40 for score in scores)
print(is_true)

# Exercise 5: Check if ANY word in the list is longer than 10 characters
words = ["python", "programming", "is", "interesting"]
is_long = any(len(word)>10 for word in words)
print(is_long)

# Exercise 6: Use zip to calculate dot product of two vectors
v1 = [1, 2, 3]
v2 = [4, 5, 6]
dot_prod =0
for e1,e2 in zip(v1,v2):
    dot_prod = e1*e2 +dot_prod
print(dot_prod)


# Exercise 7: Use enumerate to find the index of the maximum value
numbers = [23, 67, 12, 89, 45, 34]
for i,num in enumerate(numbers):
    if num==max(numbers):
        print(i)

# Exercise 8: Sort these filenames by their extension
files = ["report.pdf", "data.csv", "model.pkl", "notes.txt", "train.py"]
# Sort alphabetically by extension
sort = sorted(files,key= lambda x: x.split('.')[1])
print(sort)

# Exercise 9: Use zip_longest (from itertools) to zip unequal lists
from itertools import zip_longest
a = [1, 2, 3]
b = ["a", "b"]
zipped_list = list(zip_longest(a,b))
print(zipped_list)

# Exercise 10: Use all + any together to check:
# "All students passed AND at least one got above 90"
scores = [55, 72, 91, 68, 83]
#assume passing mark to be 50 
is_true = any(score>90 for score in scores) and  all(s>=50 for s in scores)
print(is_true)