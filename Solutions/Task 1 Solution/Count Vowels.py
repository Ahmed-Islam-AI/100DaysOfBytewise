def count_vowels(string):
    num_vowels = 0
    vowels = "aeiouAEIOU"
    for char in string:
        if char in vowels:
            num_vowels += 1
    return num_vowels

user_input = input("Enter a string: ")
vowel_count = count_vowels(user_input)
print(f"The number of vowels is: {vowel_count}")
