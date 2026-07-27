from itertools import chain , islice
# chain
file1_rows = ['a','b','c']
file2_rows = ['d','e','f']
all_rows = chain(file1_rows,file2_rows)

for row in all_rows:
    print(row)
    
# islice
def indefinite_ids():
    i = 0
    while True:
        yield i
        i+=1

first_5_ids = list(islice(indefinite_ids(),5))
print(first_5_ids)
        
