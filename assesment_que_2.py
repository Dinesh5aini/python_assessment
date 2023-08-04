list1 = []
sentence = input("Enter a paragraph:")

i = 0
while i < len(sentence):
    count = 0
    start = i
    
    while i < len(sentence) and sentence[i] != " ":
        count += 1
        i += 1
        
    if count > 4:
        t = sentence[start:i]
        list1.append(t)
    
    i += 1

print(f"Here is your list in which each word contains more than 4 letters: {list1}")

