def count_vowels(string):
    vowel = 'aeiou'
    count = 0
    for char in string.lower():
        if char in vowel:
            count += 1
    return count

sentence = "Hello, World!"
print(count_vowels(sentence))  # Output: 3
