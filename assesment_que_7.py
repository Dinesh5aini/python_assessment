# Write a program using functions to implement these formulae of permutations and combinations.
# Number of permutations of n objects taken r at a time: p(n, r) = n! / (n-r)!.
# Number of combinations of n objects taken r at a time is: c(n, r) = n! / (r!*(n-r)!) = p(n,r)/r!

def factorial(n):
    if n == 0 or n == 1:
        return 1  
    else:
        return n * factorial(n - 1)

def permutation(n, r):
    x = factorial(n)
    y = factorial(n - r)
    return x / y

def combination(n, r):
    x = factorial(n)
    y = factorial(n - r)
    z = factorial(r)
    return x / (y * z)

def main():
    inpt = input("What do you want to perform:\n\t 1.Permutation \n\t 2.Combination  ")
    inpt = inpt.lower()
    n = int(input("How many Objects are there: "))
    r = int(input(f"How many Objects to be taken Out of {n} Objects: "))
    if inpt == "permutation":
        a = permutation(n, r)
        print(f"Number of permutations of {n} objects taken {r} at a time is:", a)
    elif inpt == "combination":
        b = combination(n, r)
        print(f"Number of combinations of {n} objects taken {r} at a time is:", b)
    else:
        print("Wrong Choice!")

if __name__ == "__main__":
    main()
