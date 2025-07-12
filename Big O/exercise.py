# This code is part of a Python exercise to demonstrate Big O(n) notation.
def print_items(n):
    for i in range(n):
        print(i)
      
        
# DO NOT CHANGE THIS LINE:
print_items(10)


# This code is part of a Python exercise to demonstrate Big O(n^2) notation.
def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)
  
        
      
        
# DO NOT CHANGE THIS LINE:
print_items(10)


# This code is part of a Python exercise to demonstrate Big O(1) notation.
def print_items(n):
    print(n)

# DO NOT CHANGE THIS LINE:
print_items(10)

# This code is part of a Python exercise to demonstrate Big O(log n) notation.
def print_items(n):
    i = 1
    while i < n:
        print(i)
        i *= 2

# DO NOT CHANGE THIS LINE:
print_items(10)

# This code is part of a Python exercise to demonstrate Big O(n log n) notation.
def print_items(n):
    for i in range(n):
        j = 1
        while j < n:
            print(i, j)
            j *= 2

# DO NOT CHANGE THIS LINE:
print_items(10)