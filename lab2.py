# 1- Write a Python program to reverse a string.
print(input("Enter a string to reverse: ")[::-1])

# 2. Check if a String is a Palindrome
print("axa" == "axa"[::-1])

# 3.Remove Duplicates from a String
print("".join(set(input("Enter a string to remove duplicates: "))))
 
# 4.Find the Longest Word in a String
print(max(input("Enter a string: ").split(), key=len))
 
# 5.Find Common Elements Between Two Tuples
print(set((1,2,3)).intersection(set((2,3,4))))

# 6.Find the Maximum and Minimum Value in a Dictionary
print(max({"a": 10, "b": 20, "c": 5}.values()), min({"a": 10, "b": 20, "c": 5}.values()))

# 7 Merge Two Dictionary
dict1 = {"a": 1, "b": 2} 
dict2 = {"c": 3, "d": 4} 
dict1.update(dict2)
print(dict1)

# 8- Find Common Keys in Two Dictionaries 
dict1 = {"a": 1, "b": 2, "c": 3} 
dict2 = {"b": 2, "c": 4, "d": 5} 
print(set(dict1.keys()).intersection(set(dict2.keys())))

