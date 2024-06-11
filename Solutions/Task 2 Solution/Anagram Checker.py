def are_anagrams(str1, str2):
    # Convert both strings to lowercase and remove spaces
    str1_cleaned = ''.join(c.lower() for c in str1 if c.isalnum())
    str2_cleaned = ''.join(c.lower() for c in str2 if c.isalnum())

    # Check if the sorted versions of the cleaned strings are equal
    if sorted(str1_cleaned) == sorted(str2_cleaned):
        return True
    else:
        return False

# Example usage
string1 = "listen"
string2 = "Ahmed"

if are_anagrams(string1, string2):
    print(f"{string1} and {string2} are anagrams.")
else:
    print(f"{string1} and {string2} are not anagrams.")
