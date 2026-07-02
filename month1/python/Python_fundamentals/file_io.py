#writing files 
with open("notes.txt","w") as f:
    f.write("Hello, World! \n")
    f.write("Second line\n")

#'a' - append
with open("notes.txt","a") as f:
    f.write("Third Line\n")
    
#write multiple lines at once
lines = ["Line 1","Line 2","Line 3"]
with open("notes.txt","w") as f:
    f.writelines(line+"\n" for line in lines)
    
with open("notes.txt","w") as f:
    print("Hello, World!",file=f)
    print("Second Line",file=f)

# ---------------------------------------------------------
#  Read lines
with open("notes.txt","r") as f:
    content = f.read()
print(content)

with open("notes.txt","r") as f:
    for line in f:
        print(line.strip()) 
        
with open("notes.txt","r") as f:
    lines = [line.strip() for line in f.readlines()]
    
print(lines)


#---------------------------------------------------------------------
#JSON Files
import json

#--- Writing JSON ---
config = {
    "model_name":"iris_classifier",
    "version":"1.0.0",
    "accuracy": 0.957,
    "features":["sepal_length","sepal_width","petal_length","petal_width"],
    "trained_on":"2024-01-15"
}

with open("config.json","w") as f:
    json.dump(config,f,indent=4)
    
# Reading json
import json
with open("config.json","r") as f:
    loaded_config = json.load(f)
    
print(loaded_config["model_name"])
print(loaded_config["features"])

#--- JSON from/to string (for API responses) ---
#dict -> string
json_string = json.dumps(config,indent=2)
print(json_string)
print(type(json_string))    #string

#string -> dict
parsed = json.loads(json_string)
print(parsed["accuracy"])


#-------------------------------------------------------------------------
#CSV Files

import csv
students = [
   ["Name", "Score", "Grade"],   # header
    ["Alice",  85,  "A"],
    ["Bob",    42,  "F"],
    ["Charlie", 91, "A"],
]

with open("students.csv","w",newline="") as f:
    writer = csv.writer(f)
    writer.writerows(students)
    
#--- Reading CSV
import csv
with open("students.csv","r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
        
#--- DictReader - each row is a dict ----
import csv 
with open("students.csv","r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["Name"],row["Score"])
        
#--- DictWriter - write form dicts----
import csv 
students = [
    {"Name": "Alice",   "Score": 85, "Grade": "A"},
    {"Name": "Bob",     "Score": 42, "Grade": "F"},
    {"Name": "Charlie", "Score": 91, "Grade": "A"},
]
with open("students.csv", "w", newline="") as f:
    writer = csv.DictWriter(f,fieldnames=["Name","Score","Grade"])
    writer.writeheader()
    writer.writerows(students)



#Exercises 

# Exercise 1: Write a list of 5 student names to students.txt, one per line
list_students= ["Arjun", "Arun", "Avinash", "Abhishek", "Aarav"]
with open("student.txt","w") as f:
    f.writelines(line +"\n" for line in list_students)
    
    
# Exercise 2: Read students.txt and print each name uppercase
with open("student.txt","r") as f:
    for line in f.readlines():
       print(line.strip().upper())
  
# Exercise 3: Append 3 more names to students.txt
list_students_append = ["Aditya", "Aron","Mr. White"]
with open("student.txt","a") as f:
    f.writelines(line+"\n" for line in list_students_append)
    
    
# Exercise 5: Write this config to config.json
config = {
    "app_name": "MLOps API",
    "version": "1.0",
    "debug": True,
    "database": {"host": "localhost", "port": 5432, "name": "mlops_db"},
    "allowed_models": ["iris", "spam", "sentiment"]
}
import json
with open("config.json","w") as f:
    json.dump(config,f,indent=4)
    
# Exercise 6: Read config.json and print only the database host and port
import json
with open("config.json", "r") as f:
    config = json.load(f) 
    
print(config["database"]["host"],config["database"]["port"])

# Exercise 7: Write predictions to predictions.csv
predictions = [
    {"id": 1, "input": [5.1, 3.5, 1.4, 0.2], "prediction": 0, "confidence": 0.97},
    {"id": 2, "input": [6.7, 3.0, 5.2, 2.3], "prediction": 2, "confidence": 0.89},
    {"id": 3, "input": [5.8, 2.7, 4.1, 1.0], "prediction": 1, "confidence": 0.76},
]
import csv
with open("predictions.csv","w",newline="") as f:
    writer = csv.DictWriter(f,fieldnames=["id","input","prediction","confidence"])
    writer.writeheader()
    writer.writerows(predictions)
    
# Exercise 8: Read predictions.csv and find avg confidence score
import csv 
with open("predictions.csv","r") as f:
    reader = csv.DictReader(f)
    avg,count= 0,0
    for row in reader:
        print(row)
        avg = float(avg) + float(row["confidence"])
        count+=1
    avg = avg/count
    
print(f"Average Confidence: {avg}")


# Exercise 9: Write a function that loads a JSON config with a fallback default
import os
import json
def load_config(path, default=None):
    # If file exists → load and return it
    if os.path.exists(path):
        with open(path,"r") as f:
            return json.load(f)
    # If not → return default
    else:
        return default
    pass

print(load_config("config.json"))


# Exercise 10: Write a simple logger function that appends timestamped
# log entries to app.log
import datetime
def log(message, level="INFO"):
    # Format: [2024-01-15 10:30:45] [INFO] message
    pass