# Program to demonstrate min(), max(), len(), list(), and list comparison

# Sample data
numbers = [5, 2, 9, 1, 7]
text = "hello"
tuple_data = (10, 20, 30)


# min() and max()
print("List:", numbers)
print("Minimum value (min):", min(numbers))
print("Maximum value (max):", max(numbers))

# len()
print("\nString:", text)
print("Length of string (len):", len(text))

# list()
print("\nTuple:", tuple_data)
print("Tuple converted to list:", list(tuple_data))

# cmp() alternative in Python 3
list1 = [1, 2, 3]
list2 = [1, 2, 4]

print("\nList1:", list1)
print("List2:", list2)

if list1 == list2:
    print("cmp result: 0 (lists are equal)")
elif list1 < list2:
    print("cmp result: -1 (list1 is smaller)")
else:
    print("cmp result: 1 (list1 is greater)")
