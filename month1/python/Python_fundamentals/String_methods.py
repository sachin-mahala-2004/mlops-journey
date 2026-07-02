text = "  hello, World! This is Python  "
print(text.capitalize())
print(text.strip())

print("hello".center(12,'*'))
print("Hello World".removeprefix("Hello"))

#Exercises
# Exercise 1: Clean this messy string (strip, lowercase, remove punctuation)
messy = "  Hello, WORLD!!!  "
# Expected: "hello world"
messy = "  Hello, WORLD!!!"
print(messy.strip().removesuffix("!!!").lower().replace(',',''))


## Exercise 2: Parse a CSV line manually
csv_line = "Alice,25,Engineer,Jaipur,85000"
# Extract each field into variables
name,age,profession,city,salary = csv_line.split(',')

# Exercise 3: Count how many words are in a sentence
sentence = "The quick brown fox jumps over the lazy dog"
print(len(sentence.split()))


# Exercise 4: Check if a string is a valid Python variable name
# (only letters, digits, underscores — doesn't start with digit)
def is_valid_varname(s): 
     if not s:
         return False
     if s[0].isdigit():
         return False
     
     for ch in s:
         if not (ch.isalnum() or ch == '_'):
             return False
     return True
 
print(is_valid_varname("hello"))
#OR
import keyword
def is_valid_varname(s):
    return s.isidentifier() and not keyword.iskeyword(s)

print(is_valid_varname("_hello123"))


# Exercise 5: Reverse the words in a sentence
sentence = "Hello World from Python"
# Expected: "Python from World Hello"
print(' '.join(sentence.split()[::-1]))


# Exercise 6: Truncate a string to 20 chars and add "..." if longer
text = "This is a very long description that needs truncation"
# Expected: "This is a very long ..."

if len(text)>20:
    text = text[:20]+"..."
print(text)

