def palindrome_strings(strings):
    result = []
    for string in strings:
        if string == string[::-1]:
            result.append(string)
    return result


strings = ["racecar", "hello", "level", "python", "radar"]
palindromes = palindrome_strings(strings)
print(palindromes)
