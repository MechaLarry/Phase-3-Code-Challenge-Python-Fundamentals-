# function to add numbers
def add_numbers(num1, num2):
    return num1 + num2
# run
print(add_numbers(3, 5)) #output should be 8


# function to check if a number is even
def is_even(num):
    return num % 2 == 0
# run
print(is_even(4))  # Output: True
print(is_even(7))  # Output: False


# function to reverse a string
def reverse_string(text):
    return text[::-1]
# run
print(reverse_string("hello"))

# function to count vowels
def count_vowels(text):
    vowels = "aeiou"
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count
# run
print(count_vowels("Larry Mecha"))

# function to calculate fuctoral
def calculate_factorial(n):
    if n == 0:
        return 1
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial
# run
print(calculate_factorial(9))

# function to apply decorator
def decorator_func(func):
    def wrapper(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return wrapper

@decorator_func
def sample_function():
    print("Original Function Called")

def apply_decorator(func):
    return decorator_func(func)
# run
sample_function()

# function to sort a list of tuples by age in ascending order
def sort_by_age(list_of_tuples):
    return sorted(list_of_tuples, key=lambda x: x[1])
people = [("Stella", 30), ("Snappy", 25), ("Osir", 24)]
# run
print(sort_by_age(people))

# function to take 2 dictionaries/objects as input and merges them and common keys to be summed up
def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value
        else:
            merged_dict[key] = value
    return merged_dict
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
# run 
print(merge_dicts(dict1, dict2)) 

# function that prints out a car's information
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def display_info(self):
        print(f"Car Make: {self.make}")
        print(f"Car Model: {self.model}")
        print(f"Car Year: {self.year}")

        # run the block
my_car = Car("Rolls Royce", "Cullinan", 2025)
my_car.display_info()