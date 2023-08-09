# Greatest Common Divisor
# ● Take a user input in a list consisting of 2 or more than 2 numeric values.
# ● Find the GCD of the numbers of the list using a user defined function.


def gcd(b, a):
    if b >= a:
        if a == 0:
            return b
        else:
            return gcd(a, b % a)  
    else:
        return gcd(a, b) 
    
def gcdOfNumbers(list1):
    gcd_holder = gcd(list1[0], list1[1])
    for i in list1[2:]:
        gcd_holder = gcd(gcd_holder, i)
    return gcd_holder

def main():
    size = int(input("Enter the size of list: "))
    print("Enter Elements to Calculate the GCD:")
    for i in range(size):
        f = int(input())
        list1.append(f)
    gcd_of_list = gcdOfNumbers(list1)

    print("The GCD of the given list is:", gcd_of_list)

if __name__ == "__main__":
    list1 = []
    main()
