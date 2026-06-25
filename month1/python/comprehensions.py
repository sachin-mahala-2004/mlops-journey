# List Comprehensions 
 
# without comprehension(old way):
numbers = [1,2,3,4,5]
squares = []
for n in numbers:
    squares.append(n**2)
print(squares)

# With Comprehension( the right way )
numbers = [1,2,3,4,5]
squares = [n**2 for n in numbers]
print(squares)

## Syntax 
# result = [expression for item in iterable if condition]

# Examples -
 # -Basic
names = ["alice","bob","charlie"]
upper = [name.upper() for name in names]
print(upper)

 # -With condition - filter even numbers
numbers = [1,2,3,4,5,6,7,8]
evens = [n for n in numbers if n%2==0]
print(evens)

 # -With condition AND expression
evens_squared = [n**2 for n in numbers if n%2==0]
print(evens_squared)

 # -From a string
vowels = [ch for ch in "hello world" if ch in "aeiou"]
print(vowels)

 # -With Range 
multiples_of_3 = [n for n in range(1,31) if n%3==0]
print(multiples_of_3)

 # -Nested list comprehension (matrix flattening)
matrix = [[1,2,3],[4,5,6],[7,8,9]]
flat = [num for row in matrix for num in row]
print(flat)

#-----------------------------------------------------------------------------------------------

## Exercises ---comprehensions.py
print("\n\n------------------------Exercises----------------------------------\n\n\\")

print("Exercise 1 : Get all words longer than 4 characters from the list")
words = ['cat','elephant','dog','butterfly','ant','rhinoceros']
words_longer_than_4 = [word for word in words if len(word)>=4]
print(words_longer_than_4)

print("Exercise 2 : Convert Celsius to Fahrenheit for each value")
# Formula: F=C* 9/5 + 32
celcius = [0,20,37,100]
fahrenheit = [(c*(9/5))+32 for c in celcius]
print(fahrenheit)

print("Exercise 3: Get only the email addresses that end with @gmail.com")
emails = ["alice@gmail.com", "bob@yahoo.com", "charlie@gmail.com", "dave@hotmail.com"]
req_emails = [email for email in emails if email.endswith("@gmail.com")]
# OR 
# req_emails = [email for email in emails if "@gmail.com in email"]
print(req_emails)

print("Exercise 4: From a list of numbers, return only the ones divisible by both 2 and 3")
numbers = list(range(1,31))
div_2_3 = [num for num in numbers if num%2==0 and num%3==0]
print(div_2_3)

print("Exercise 5: Create a list of tuples (number, square) for 1 to 10")
numbers = list(range(1,10))
tples = [(num,num**2) for num in numbers]
print(tples)

print("Exercise 6: Remove all duplicates from a list and keep order")
items = [1, 2, 2, 3, 4, 4, 5, 1, 6]
seen = []
no_dupli = [num for num in items if num not in seen and not seen.append(num)]
print(no_dupli)


print("Exercise 7: Extract all numbers from a list of mixed types")
mixed = [1, "hello", 3.14, True, "world", 42, None, 7]
int_and_float = [x for x in mixed if isinstance(x,(int,float))]
print(int_and_float)


print("Exercise 8: Get the first character of each word, uppercase")
sentence = "the quick brown fox"
first_upper = [letter.upper() for word in sentence.split(' ') for letter in word[0]]
print(first_upper)


print("Exercise 10: Get all pairs (i, j) where i != j, from range(1, 4)")
lst = [(i,j) for i in range(1,4) for j in range(1,4) if i!=j]
print(lst)