# -----------------------------------------------------------
# STRING CONCATENATION METHODS
# -----------------------------------------------------------

print("\n--- STRING CONCATENATION ---")

# 1. Using + operator
string1 = "Hello, "
string2 = "Python!"
print("Using + :", string1 + string2)

# 2. Using f-strings
name = "Alice"
age = 30
print("Using f-string :", f"My name is {name} and I am {age} years old.")

# 3. Using join()
words = ["This", "is", "a", "list", "of", "words."]
print("Using join :", " ".join(words))

# 4. Using % operator
item = "apple"
quantity = 5
print("Using % :", "I have %d %s." % (quantity, item))

# 5. Using format()
city = "New York"
temp = 25.5
print("Using format :", "The temperature in {} is {} degrees Celsius."
      .format(city, temp))


# -----------------------------------------------------------
# STRING SLICING AND INDEXING
# -----------------------------------------------------------

print("\n--- STRING SLICING AND INDEXING ---")

my_string = "Python"
print("my_string[0] :", my_string[0])
print("my_string[3] :", my_string[3])
print("my_string[-1] :", my_string[-1])
print("my_string[-4] :", my_string[-4])


# -----------------------------------------------------------
# STRING METHODS
# -----------------------------------------------------------

print("\n--- STRING METHODS ---")

text = "   Hello World!   "
print("strip() :", text.strip())
print("upper() :", text.upper())
print("replace() :", text.replace("World", "Python"))
print("join() :", " ".join(["Python", "is", "fun"]))


# -----------------------------------------------------------
# TUPLE CREATION
# -----------------------------------------------------------

print("\n--- TUPLE CREATION ---")

my_tuple = ("apple", 1, 3.14, True)
print("Tuple :", my_tuple)

another_tuple = "hello", 5, False
print("Tuple without brackets :", another_tuple)

empty_tuple = ()
print("Empty Tuple :", empty_tuple)

single_element_tuple = ("single_item",)
print("Single element tuple :", single_element_tuple)


# -----------------------------------------------------------
# TUPLE MODIFICATION (IMMUTABLE)
# -----------------------------------------------------------

print("\n--- TUPLE MODIFICATION ---")

original_tuple = (1, 2, 3)
print("Original tuple :", original_tuple)

# Convert to list to modify
temp_list = list(original_tuple)
temp_list[0] = 4
new_tuple = tuple(temp_list)

print("Modified tuple :", new_tuple)


# -----------------------------------------------------------
# TUPLE ACCESS
# -----------------------------------------------------------

print("\n--- TUPLE ACCESS ---")

access_tuple = ("a", "b", "c", "d")

print("access_tuple[0] :", access_tuple[0])
print("access_tuple[2] :", access_tuple[2])
print("access_tuple[-1] :", access_tuple[-1])
print("access_tuple[-3] :", access_tuple[-3])


# -----------------------------------------------------------
# TUPLE SLICING
# -----------------------------------------------------------

print("\n--- TUPLE SLICING ---")

slice_tuple = (10, 20, 30, 40, 50)

print("slice_tuple[1:4] :", slice_tuple[1:4])
print("slice_tuple[:3] :", slice_tuple[:3])
print("slice_tuple[2:] :", slice_tuple[2:])
