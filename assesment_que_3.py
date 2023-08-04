inpt=input("[WRITE A SENTENCE]:")

cat=inpt.count("cat" or "CAT" or "Cat")
dog=inpt.count("dog" or "DOG" or "Dog")

if cat>0:
    if cat == dog:
        print("True")
    else:
        print("Number of cat and dogs are not matched!")
