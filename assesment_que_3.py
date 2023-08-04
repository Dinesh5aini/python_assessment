# Raining like cats and dogs
# ● Take user input in the form of a string.
# ● Return True if in the string "cat" and "dog" appear the same number of times in the given string


inpt=input("[WRITE A SENTENCE]:")

cat=inpt.lower().count("cat")
dog=inpt.lower().count("dog")

if cat>0 or dog>0:
    if cat == dog:
        print("True")
    else:
        print("False")
else:
    print("False")