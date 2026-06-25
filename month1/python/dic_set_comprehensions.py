# Dict Comprehension
# Syntax 
# result = {key_expr: value_expr for item in iterable}
# result = {key_expr: value_expr for item in iterable if condition}

#Examples 
names = ['alice', 'bob', 'charlie']
lengths = {name:len(name) for name in names}
print(lengths)

#swap keys and values
original = {"a": 1, "b": 2, "c": 3}
swapped = {v:k for k,v in original.items()}
print(swapped)


# Filter a dict — keep only items where value > 2
scores = {"alice": 85, "bob": 42, "charlie": 91, "dave": 38}
passed = {name: score for name, score in scores.items() if score >= 50}


# Create a dict from two lists
keys   = ["name", "age", "city"]
values = ["Arjun", 20, "Jaipur"]
person = {k:v for k,v in zip(keys,values)}
print(person)

## set comprehension
# syntax 
# result = {expresssion for item in iterable}

numbers = [1,1,2,2,3,3,4]
unique = { n for n in numbers}
print(unique)
# {1,2,3,4}

# Get unique first letters
words = ["apple","avocado","banana","blueberry","cherry"]
first_letters = {word[0] for word in words }
print(first_letters)


#Exercises
print('\n\n-------------------------------------------------------------------------------\n\n')

print("Exercise 1: Create a dict mapping each number to its cube, for 1 to 10")
mapping = {k:pow(k,3) for k in range(1,11)}
print(mapping)


print("Exercise 2: From scores dict, create a dict of ONLY failing students (<50)")
scores = {"alice": 85, "bob": 42, "charlie": 91, "dave": 38, "eve": 55}
failed_stu = {student:score for student,score in scores.items() if score < 50}
print(failed_stu)


print("Exercise 3: Swap keys and values of this dict")
original = {"python": 1, "java": 2, "javascript": 3}
swap = {v:k for k,v in original.items()}
print(swap)


print(" Exercise 4: Create a dict from this list of tuples")
pairs = [("name", "Arjun"), ("age", 20), ("city", "Jaipur")]
dic = {t[0]:t[1] for t in pairs}
print(dic)


print("# Exercise 5: Count character frequency in a string using dict comprehension")
text = "hello"
dic = {x:text.count(x) for x in text}
print(dic)


print("# Exercise 6: Get the unique lengths of these words")
words = ["cat", "dog", "elephant", "ant", "bee", "butterfly"]
unique = {len(x) for x in words }
print(unique)



print("# Exercise 7: From two lists, create a dict only where the value is not None")
keys   = ["a", "b", "c", "d"]
values = [1, None, 3, None]
dic = {k:v for k,v in zip(keys,values) if v is not None}
print(dic)



print("# Exercise 8: Normalize scores to 0-1 range")
scores = {"alice": 80, "bob": 60, "charlie": 100}
max_score = max(scores.values())
dic = {k:v/100 for k,v in scores.items()}
print(dic)