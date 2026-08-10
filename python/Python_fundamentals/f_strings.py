# f-strings
#calling methods inside f-strings
items = [1,2,3]
print(f"items:{','.join(str(i) for i in items)}")

#number formatting
pi = 3.1415926
price = 1234567.91
ratio = 0.873

#decimal places
print(f"{price:.2f}")
print(f"{pi:.2f}")

#thousands seperator 
print(f"{price:,.2f}")

#percentage 
print(f"{ratio:.1%}")

#width and alignment 
print(f"{'left':<20}|")
print(f"{"right":>20}|")
print(f"{"center":^20}|")

#pad numbers with zeros
print(f"{42:05d}")    #pad with zeros instead of spaces 
                      #minimum width 5
                      # format as a decimal integer

#multiline f-strings
name  = "Arjun"
score = 91
grade = "A"

report = f"""
Student Report 
--------------
Name: {name}
Score: {score}
Grade: {grade}
Status: {"PASS" if score>=50 else "FAIL"}
"""
print(report)

#Exercises
# Exercise 1: Print a formatted table of products
products = [("Apple", 0.5), ("Banana", 0.3), ("Cherry", 1.2)]
# Format as:
# Product    Price
# Apple      $0.50
# Banana     $0.30
print(f"{"Product":<10}{"Price"}")
for product,price in products:
    print(f"{product:<10}${price:.2f}")
    
# Exercise 2: Format a large number with commas and 2 decimal places
revenue = 9876543.21
print(f"{revenue:,.2f}")

# Exercise 3: Print a percentage with 1 decimal place
correct = 43
total   = 50
print(f"{43/50:.1%}")

# Exercise 4: Right-align numbers in a column (width 8)
for n in [1, 25, 300, 4000]:
    print(f"{n:>8}")
    
# Exercise 7: Format elapsed time from seconds
seconds = 3724
# Expected: "1 hours, 2 minutes, 4 seconds"
hours = seconds // 3600
minutes = (seconds % 3600) // 60
seconds = seconds % 60
print(f"{hours} hours, {minutes} minutes, {seconds} seconds")

# Exercise 8: Zero-pad day, month in a date
day, month, year = 5, 3, 2024
print(f"{day:02d}/{month:02d}/{year:04d}")

# Exercise 9: Print a progress bar using f-strings
progress = 0.67
# Expected: [======    ] 67.0%
bar_length=10
filled = int(progress*bar_length)
print(f"[{'='*filled}{' '*(bar_length-filled)}] {progress:.1%}")


#ternary Expresions & tuple unpacking 
# ternary 
score = 75
result = "PASS" if score>=50 else "FAIL"
print(result) 

#In assignments
age = 20
lablel = "adult" if age>=18 else "minor"

scores= [85,42,91,38]
results= ["PASS" if score>=50 else "FAIL" for score in scores]
print(results)

#Nested ternary (keep it redable)
score = 85
grade = "A" if score>=90 else "B" if score>=75 else "C" if score>=60 else "F"
print(grade)

#Swap two variables (Python way)
a,b = 10,20
a,b = b,a      #no temp variable needed
print(a,b)

#Extend unpacking with *
numbers = [1,2,3,4,5,6,7]

*start,last = numbers
print(start)
print(last)

first , *rest = numbers
print("\n",first)
print(rest)

first , *middle, rest = numbers
print("\n",first)
print(middle)
print(rest)

