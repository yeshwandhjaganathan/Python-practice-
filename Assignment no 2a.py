# ===========================================
# PYTHON LIST – CREATION, MODIFICATION, ACCESS
# ===========================================

print("\n---- LIST: CREATION ----")

# 1. Creating Lists
empty_list = []
print("Empty list:", empty_list)

numbers = [1, 2, 3, 4, 5]
print("Numbers list:", numbers)

fruits = ["apple", "banana", "cherry"]
print("Fruits list:", fruits)

mixed_list = [10, "hello", 3.14, True]
print("Mixed list:", mixed_list)

nested_list = [1, [2, 3], 4]
print("Nested list:", nested_list)


print("\n---- LIST: MODIFICATION ----")

my_list = [10, 20, 30, 40, 50]

my_list[0] = 15
print("After modifying index 0:", my_list)

my_list.append(60)
print("After append:", my_list)

my_list.insert(1, 25)
print("After insert index 1:", my_list)

another_list = [70, 80]
my_list.extend(another_list)
print("After extend:", my_list)

my_list.remove(20)
print("After remove 20:", my_list)

popped_item = my_list.pop()
print("After pop:", my_list)
print("Popped item:", popped_item)

del my_list[0]
print("After deleting index 0:", my_list)

my_list.clear()
print("After clear:", my_list)


print("\n---- LIST: ACCESS ----")

my_list = ["a", "b", "c", "d", "e"]

print("my_list[0] =", my_list[0])
print("my_list[2] =", my_list[2])

print("my_list[-1] =", my_list[-1])
print("my_list[-3] =", my_list[-3])

print("my_list[1:4] =", my_list[1:4])
print("my_list[:3] =", my_list[:3])
print("my_list[2:] =", my_list[2:])
print("my_list[:] =", my_list[:])

print("\nIterating through list:")
for item in my_list:
    print(item)


# ===========================================
# PYTHON DICTIONARY – CREATION, MODIFICATION, ACCESS
# ===========================================

print("\n==== DICTIONARY: CREATION ====")

my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print("Dictionary:", my_dict)

my_dict2 = dict(name="Bob", age=25, city="London")
print("Dict using constructor:", my_dict2)

list_of_tuples = [("fruit", "apple"), ("color", "red")]
my_dict3 = dict(list_of_tuples)
print("Dict from list of tuples:", my_dict3)

keys = ["a", "b", "c"]
my_dict4 = dict.fromkeys(keys, 0)
print("Dict from keys:", my_dict4)


print("\n==== DICTIONARY: ACCESS ====")

print("Name:", my_dict["name"])
print("Age (using get):", my_dict.get("age"))
print("Unknown key:", my_dict.get("occupation", "Not Found"))


print("\n==== DICTIONARY: MODIFICATION ====")

my_dict["occupation"] = "Engineer"
print("After adding occupation:", my_dict)

my_dict["age"] = 31
print("After updating age:", my_dict)

del my_dict["city"]
print("After deleting city:", my_dict)

removed_age = my_dict.pop("age")
print("After pop age:", my_dict)
print("Removed age:", removed_age)

removed_item = my_dict.popitem()
print("After popitem:", my_dict)
print("Removed (key, value):", removed_item)

another_dict = {"email": "alice@example.com", "age": 32}
my_dict.update(another_dict)
print("After update:", my_dict)


# ===========================================
# PYTHON SETS – OPERATIONS
# ===========================================

print("\n==== SET OPERATIONS ====")

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

union_set = set_a | set_b
print("Union:", union_set)

intersection_set = set_a & set_b
print("Intersection:", intersection_set)

diff_set = set_a - set_b
print("Difference (A - B):", diff_set)

sym_diff_set = set_a ^ set_b
print("Symmetric Difference:", sym_diff_set)

set_a.add(5)
print("Set A after adding 5:", set_a)

set_a.discard(1)
print("Set A after discarding 1:", set_a)


# ===========================================
# CONDITIONAL STATEMENTS PROGRAM
# PERFORMANCE CATEGORY PROGRAM
# ===========================================

print("\n==== PERFORMANCE CATEGORY PROGRAM ====")

def get_performance_category():
    while True:
        try:
            score_str = input("Enter a score between 0 and 10: ")
            score = int(score_str)

            if 0 <= score <= 10:
                if score > 7:
                    print("Performance Category: Above Average")
                elif 4 <= score <= 7:
                    print("Performance Category: Average")
                else:
                    print("Performance Category: Below Average")
                break
            else:
                print("Invalid input. Enter score 0–10.")
        except ValueError:
            print("Invalid input. Enter an integer.")

# Run function
# (Remove comment to enable interactive use)
# get_performance_category()

print("\nAll concepts executed successfully! 🎉")
