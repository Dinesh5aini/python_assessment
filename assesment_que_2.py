#  Write a program that converts Paragraph to List
# ● Take input from the user in string form(a sentence or para)
# ● All the words in the string having more than 4 letters should be stored in a list

# Sample Input : A paragraph is defined as “a group of sentences or a single sentence that forms a unit”. Length and appearance do not determine whether a section in a paper is a paragraph.
# Sample Output : [ ‘paragraph’ , ‘defined’, ‘group’ , ‘sentences’ , ‘forms’ , ‘Length’,‘appearance’ , ‘determine’ , ‘whether’ , ‘section’ , ‘paper’ , ‘paragraph’ ]


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

