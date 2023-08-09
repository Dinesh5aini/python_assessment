
# Filter
# ● Create a function even_filter with one parameter. This function will return a
# list which will contain only odd values.
# ● Create a function odd_filter with one parameter. This function will return a
# list which will contain only even values.
# ● Call the function even_filter and pass a list of numbers as an argument.
# ● Call the function odd_filter and pass a dictionary as an argument.
# ● NOTE: The list and dictionary must be user define


list1=[]
list2=[]
list3=[]
dict1={}

def createList(size):
    print("[ENTER INTEGERS]:")
    for i in range(size):
        t=int(input())
        list1.append(t)
    return list1

def createDict(size1):
    print("[ENTER INTEGERS]:")
    for key in range(size1):
        dict1[key]=int(input())
    return dict1

def enven_filter(list1):
    for i in list1:
        if i%2!=0:
            list2.append(i)
        else:
            continue
    return list2

def odd_filter(dict1):
    for key in dict1:
        if (dict1[key]%2==0):
            temp=dict1[key]
            list3.append(temp)
        else:
            continue
    return list3

size=int(input("Enter size of list:"))
x=createList(size)

size1=int(input("Enter size of dictionary:"))
y=createDict(size1)

even=enven_filter(x)
odd=odd_filter(y)

print("Call of enven filter:",even)
print("Call of odd filter:",odd)