import sys

def use_ints():
    print("*** Using ints")
    # Create and initialize an integer
    x = 10

    # Print the value of the integer
    print("x = ", x)

    # Add two integers
    y = x + 5
    print("x + 5 = ", y)

    # Subtract two integers
    z = x - 2
    print("x - 2 = ", z)

    # Multiply two integers
    w = x * 3
    print("x * 3 = ", w)

    # Divide two integers (floating-point)
    p = x / 2
    print("x / 2 = ", p)

    # Divide two integers (floor)
    q = x // 3
    print("x // 3 = ", q)

    # Modulus (remainder) of two integers
    r = x % 3
    print("x % 3 = ", r)

    # Exponentiation of an integer
    s = x ** 2
    print("x ** 2 = ", s)

    # Increment an integer
    x += 1
    print("x after increment = ", x)

    # Decrement an integer
    x -= 1
    print("x after decrement = ", x)

    # Cast a string to an integer
    t = int("20")
    print("t = ", t)

    # Print the maximum and minimum integer values
    print("Maximum integer value:", sys.maxsize)
    print("Minimum integer value:", -sys.maxsize - 1)
    print()

def use_floats():
    print("*** Using Floats")
    # Create and initialize a float
    x = 3.14

    # Print the value of the float
    print("x = ", x)

    # Add two floats
    y = x + 2.5
    print("x + 2.5 = ", y)

    # Subtract two floats
    z = x - 1.0
    print("x - 1.0 = ", z)

    # Multiply two floats
    w = x * 2.0
    print("x * 2.0 = ", w)

    # Divide two floats
    p = x / 1.5
    print("x / 1.5 = ", p)

    # Exponentiation of a float
    s = x ** 2.0
    print("x ** 2.0 = ", s)

    # Increment a float
    x += 1.0
    print("x after increment = ", x)

    # Decrement a float
    x -= 1.0
    print("x after decrement = ", x)

    # Cast a string to a float
    t = float("3.5")
    print("t = ", t)

    # Print the largest and smallest possible finite float values
    print("Largest possible finite float value:", sys.float_info.max)
    print("Smallest possible finite float value:", sys.float_info.min)
    print()

def use_complex():
    print("*** Using complex")
    # Create and initialize a complex number
    x = 2 + 3j

    # Print the value of the complex number
    print("x = ", x)

    # Add two complex numbers
    y = x + (1 - 2j)
    print("x + (1 - 2j) = ", y)

    # Subtract two complex numbers
    z = x - (0.5 + 1j)
    print("x - (0.5 + 1j) = ", z)

    # Multiply two complex numbers
    w = x * (2 - 1j)
    print("x * (2 - 1j) = ", w)

    # Divide two complex numbers
    p = x / (1 + 2j)
    print("x / (1 + 2j) = ", p)

    # Exponentiation of a complex number
    s = x ** 2
    print("x ** 2 = ", s)

    # Increment a complex number (not supported)
    # x += 1j

    # Decrement a complex number (not supported)
    # x -= 1j

    # Cast a string to a complex number
    t = complex("2+4j")
    print("t = ", t)

    # Print the real and imaginary parts of a complex number
    print("Real part of x:", x.real)
    print("Imaginary part of x:", x.imag)
    print()

def use_seq():
    print("*** Using Sequence")
    # Create and initialize a string
    s = "hello, world"

    # Print the value of the string
    print("s = ", s)

    # Access an element in a string using an index
    print("s[0] = ", s[0])

    # Slice a string to get a substring
    print("s[1:5] = ", s[1:5])

    # Concatenate two strings
    t = "python"
    u = s + " " + t
    print("s + ' ' + t = ", u)

    # Repeat a string
    v = t * 3
    print("t * 3 = ", v)

    # Determine the length of a string
    print("len(s) = ", len(s))

    # Create and initialize a list
    lst = [1, 2, 3, 4, 5]

    # Print the value of the list
    print("lst = ", lst)

    # Access an element in a list using an index
    print("lst[0] = ", lst[0])

    # Slice a list to get a sublist
    print("lst[1:4] = ", lst[1:4])

    # Concatenate two lists
    lst2 = [6, 7, 8]
    lst3 = lst + lst2
    print("lst + lst2 = ", lst3)

    # Repeat a list
    lst4 = lst2 * 2
    print("lst2 * 2 = ", lst4)

    # Determine the length of a list
    print("len(lst) = ", len(lst))
    print()

def use_list():
    print("*** Using List")
    # Create and initialize a list
    lst = [1, 2, 3, 4, 5]

    # Print the value of the list
    print("lst = ", lst)

    # Access an element in a list using an index
    print("lst[0] = ", lst[0])

    # Slice a list to get a sublist
    print("lst[1:4] = ", lst[1:4])

    # Concatenate two lists
    lst2 = [6, 7, 8]
    lst3 = lst + lst2
    print("lst + lst2 = ", lst3)

    # Repeat a list
    lst4 = lst2 * 2
    print("lst2 * 2 = ", lst4)

    # Determine the length of a list
    print("len(lst) = ", len(lst))

    # Append an element to the end of a list
    lst.append(6)
    print("lst after append: ", lst)

    # Insert an element at a specific index
    lst.insert(2, 6)
    print("lst after insert: ", lst)

    # Remove the first occurrence of an element in a list
    lst.remove(3)
    print("lst after remove: ", lst)

    # Remove and return the last element in a list
    last_element = lst.pop()
    print("lst after pop: ", lst)
    print("Last element: ", last_element)

    # Reverse a list
    lst.reverse()
    print("lst after reverse: ", lst)

    # Sort a list in ascending order
    lst.sort()
    print("lst after sort: ", lst)

    # Clear all elements from a list
    lst.clear()
    print("lst after clear: ", lst)
    print()

def use_tuple():
    print("*** Using tuple")
    # Create and initialize a tuple
    tup = (1, 2, 3, 4, 5)

    # Print the value of the tuple
    print("tup = ", tup)

    # Access an element in a tuple using an index
    print("tup[0] = ", tup[0])

    # Slice a tuple to get a subtuple
    print("tup[1:4] = ", tup[1:4])

    # Concatenate two tuples
    tup2 = (6, 7, 8)
    tup3 = tup + tup2
    print("tup + tup2 = ", tup3)

    # Repeat a tuple
    tup4 = tup2 * 2
    print("tup2 * 2 = ", tup4)

    # Determine the length of a tuple
    print("len(tup) = ", len(tup))

    # Convert a tuple to a list
    lst = list(tup)
    print("lst = ", lst)

    # Convert a list to a tuple
    tup5 = tuple(lst)
    print("tup5 = ", tup5)
    print()

def use_string():
    print("*** Using string")
    # Create and initialize a string
    str1 = "Hello, World!"

    # Print the value of the string
    print("str1 = ", str1)

    # Access a character in a string using an index
    print("str1[0] = ", str1[0])

    # Slice a string to get a substring
    print("str1[7:12] = ", str1[7:12])

    # Concatenate two strings
    str2 = " How are you?"
    str3 = str1 + str2
    print("str1 + str2 = ", str3)

    # Repeat a string
    str4 = str2 * 2
    print("str2 * 2 = ", str4)

    # Determine the length of a string
    print("len(str1) = ", len(str1))

    # Convert a string to uppercase
    str5 = str1.upper()
    print("str1 in uppercase: ", str5)

    # Convert a string to lowercase
    str6 = str2.lower()
    print("str2 in lowercase: ", str6)

    # Replace a substring in a string
    str7 = str1.replace("World", "Universe")
    print("str1 after replace: ", str7)

    # Split a string into a list of substrings
    str8 = "apple,banana,cherry"
    lst = str8.split(",")
    print("lst = ", lst)

    # Join a list of strings into a single string
    str9 = "-".join(lst)
    print("str9 = ", str9)
    print()

def use_dict():
    print("*** Using Dictionary")
        # Create and initialize a dictionary
    dict1 = {"name": "John", "age": 30, "city": "New York"}

    # Print the value of the dictionary
    print("dict1 = ", dict1)

    # Access a value in a dictionary using a key
    print("dict1['name'] = ", dict1["name"])

    # Add a new key-value pair to a dictionary
    dict1["country"] = "USA"
    print("dict1 after adding a new key-value pair = ", dict1)

    # Update the value of a key in a dictionary
    dict1["age"] = 35
    print("dict1 after updating the value of a key = ", dict1)

    # Remove a key-value pair from a dictionary
    dict1.pop("city")
    print("dict1 after removing a key-value pair = ", dict1)

    # Determine the number of key-value pairs in a dictionary
    print("len(dict1) = ", len(dict1))

    # Convert a dictionary to a list of keys or values
    keys = list(dict1.keys())
    values = list(dict1.values())
    print("keys = ", keys)
    print("values = ", values)

    # Iterate over the keys and values in a dictionary
    for key, value in dict1.items():
        print(key, "=", value)
    print()

def use_set():
    print("*** Using set")
    # Create and initialize a set
    set1 = {"apple", "banana", "cherry"}

    # Print the value of the set
    print("set1 = ", set1)

    # Add an element to a set
    set1.add("orange")
    print("set1 after adding an element = ", set1)

    # Remove an element from a set
    set1.remove("banana")
    print("set1 after removing an element = ", set1)

    # Determine the number of elements in a set
    print("len(set1) = ", len(set1))

    # Check if an element is in a set
    print("Is 'apple' in set1? ", "apple" in set1)

    # Perform set operations such as union, intersection, and difference
    set2 = {"banana", "orange", "kiwi"}
    union = set1.union(set2)
    print("set1 union set2 = ", union)

    intersection = set1.intersection(set2)
    print("set1 intersection set2 = ", intersection)

    difference = set1.difference(set2)
    print("set1 difference set2 = ", difference)

    # Iterate over the elements in a set
    for element in set1:
        print(element)
    print()

def main():
    print("*** Different Data Types Use Cases with Specific Operators")
    use_ints()
    use_floats()
    use_complex()
    use_seq()
    use_list()
    use_tuple()
    use_string()
    use_dict()
    use_set()

if __name__ == "__main__":
    main()