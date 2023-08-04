def create_dictionary(keys, values):
    dictionary = {}
    for i in range(len(keys)):
        dictionary[keys[i]] = values[i]
    return dictionary

size = int(input("Enter the size of the lists: "))

list1 = []
list2 = []
print("Enter elements for the first list:")
for i in range(size):
    element = input(f"Element {i+1}: ")
    list1.append(element)

print("\nEnter elements for the second list (must be unique):")
for i in range(size):
    element = input(f"Element {i+1}: ")
    list2.append(element)

merged_dict = create_dictionary(list1, list2)

print("\nMerged Dictionary:")
for key, value in merged_dict.items():
    print(f"{key}: {value}")
