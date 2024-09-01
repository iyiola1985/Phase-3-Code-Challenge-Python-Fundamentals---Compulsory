

# 1 Function: add_numbers

def add_numbers(num1, num2):
    return num1 + num2
result = add_numbers(5, 3)
print(result)

#  2 Function: is_even

def is_even(number):
    return number % 2 == 0

print(is_even(4))  # 2 can be divided by 4 : True
print(is_even(7))  # 2 cant be divided by 7: False

# 3 Function: reverse_string
def reverse_string(text):
    return text[::-1]
print(reverse_string("hello"))  # Output in reverse: "olleh"
print(reverse_string("Python")) # Output in reverse  "nohtyP"

# 4 Function: count_vowels 

def count_vowels(text):
    # Define a set of vowels (both lowercase and uppercase)
    vowels = "aeiouAEIOU"
    # Use a generator expression to count vowels
    return sum(1 for char in text if char in vowels)
print(count_vowels("Hello, World!"))  # Output: 3
print(count_vowels("Python Programming"))  # Output: 4

# 5 Function: calculate_factorial

def calculate_factorial(n):
    # Handle the base case where n is 0 or 1
    if n == 0 or n == 1:
        return 1
    # Initialize the result to 1
    result = 1
    # Loop from 2 to n to calculate the factorial
    for i in range(2, n + 1):
        result *= i
    return result

print(calculate_factorial(5))  # Output: 120
print(calculate_factorial(0))  # Output: 1
print(calculate_factorial(7))  # Output: 5040

# 6 Function: apply_decorator

def decorator_func(func):
    def wrapper(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return wrapper

def apply_decorator(func):
    # Apply the decorator to the given function
    return decorator_func(func)

@apply_decorator
def say_hello(name):
    print(f"Hello, {name}!")

# Calling the decorated function
say_hello("Alice")  # Output: Decorator Applied
                    #         Hello, Alice!
                    
                    
#  7 Sequences: Sort List of Tuples

def sort_by_age(tuples_list):
    # Sort the list of tuples by the second element (age) of each tuple
    return sorted(tuples_list, key=lambda x: x[1])
# List of tuples where each tuple contains a name and an age
people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]

# Sorting by age
sorted_people = sort_by_age(people)

print(sorted_people)  # Output: [('Bob', 25), ('Alice', 30), ('Charlie', 35)]

# 8 Sets and Dictionaries: Merge Dictionaries 
def merge_dicts(dict1, dict2):
    # Create a new dictionary to hold the merged result
    merged_dict = dict1.copy()  # Start with a copy of dict1
    
    # Iterate through dict2 and add its values to the merged_dict
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value  # Sum values for common keys
        else:
            merged_dict[key] = value  # Add new key-value pairs
    
    return merged_dict
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}

merged = merge_dicts(dict1, dict2)
print(merged)  # Output: {'a': 1, 'b': 5, 'c': 7, 'd': 5}

#  9 Object-Oriented Programming: Class Creation
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")

# Example usage
my_car = Car("Toyota", "Corolla", 2020)
my_car.display_info()











