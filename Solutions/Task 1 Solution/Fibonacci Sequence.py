def main():
    nterms = int(input("How many terms? "))
    n1, n2 = 0, 1

    if nterms <= 0:
        print("Please enter a positive integer")
    elif nterms == 1:
        print(f"Fibonacci sequence up to {nterms}:")
        print(n1)
    else:
        print("Fibonacci sequence:")
        count = 0
        while count < nterms:
            print(n1, end=" ")
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1

if __name__ == "__main__":
    main()
