import sys
squares_list = [x**2 for x in range(1000000)]
squares_gen = (x**2 for x in range(1000000))

print(sys.getsizeof(squares_list))
print(sys.getsizeof(squares_gen))
