user_input = input("Enter a string: ")
rev_of_input = user_input[:: -1]

if user_input == rev_of_input:
    print(f"{user_input} is a Palindrome.")

else:
    print(f"{user_input} is not a Palindrome.")