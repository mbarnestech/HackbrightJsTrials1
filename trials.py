"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items:
        print(item)


def get_all_evens(nums):
    even = []
    for num in nums:
        if num % 2 == 0:
            even.append(num)
        return even

def get_odd_indices(items):
    result = []
    for i in range(len(items)):
        if i % 2 != 0:
            result.append(items[i])
    return result

def print_as_numbered_list(items):
    i = 1
    for item in items:
        print(f"{i}, {item}")
        i += 1

def get_range(start, stop):
    nums = []
    for num in range(start, stop):
        nums.append(num)
    return nums

def censor_vowels(word):
    char = []
    for letter in word:
        if letter in "aeiou":
            char.append("*")
        else:
            char.append(letter)
    return ''.join(char)

def snake_to_camel(string):
    camelCase = []
    for word in string.split('_'):
        camelCase.append(f'{word.upper()[0]}{word[1:]}')
    return ''.join(camelCase)

def longest_word_length(words):
    longest = len(words[0])
    for word in words:
        if longest <len(word):
            longest = len(word)
    return longest

def truncate(string):
    result = []
    
    for char in string:
        if len(result) == 0 or char != result[len(result) -1]:
            result.append(char)

    return ''.join(result)


def has_balanced_parens(string):
    parens = 0
    for char in string:
        if char == "(":
            parens += 1
        elif char == ")":
            parens -= 1
        if parens < 0:
            return False 
    return parens == 0

def compress(string):

    compressed = []
    currChar = ''
    charCount = 0

    for char in string:
        if char != currChar:
            compressed.append(currChar)
        
            if charCount > 1:
                compressed.append(str(charCount))
            
            currChar = char
            charCount = 0
        
        charCount += 1

    compressed.append(currChar)

    if charCount > 1:
        compressed.append(string(charCount))
    
    return ''.join(compressed)
