#text analysis function
#1. count words
def count_words(text):
    words = text.split()
    return len(words)

#2. count vowels
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    return count

#3. count consonants
def count_consonants(text):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch.isalpha() and ch not in vowels:
            count += 1
    return count

#4. reverse text
def reverse_text(text):
    return text[::-1]

#5. check palindrome
def is_palindrome(text):
    text_lower = text.lower()
    return text_lower == text_lower[::-1]

#6. remove vowels
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    result = ""
    for ch in text:
        if ch not in vowels:
            result += ch
    return result

#7. word frequency
def word_frequency(text):
    words = text.lower().split()
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

#8. longest word
def longest_word(text):
    words = text.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest


#9. analyze text (main function)
def analyze_text(text):
    print("   TEXT ANALYSIS   ")
    print("Words:", count_words(text))
    print("Vowels:", count_vowels(text))
    print("Consonants:", count_consonants(text))
    print("Reversed:", reverse_text(text))

    if is_palindrome(text):
        print("Palindrome: Yes")
    else:
        print("Palindrome: No")

    print("Without vowels:", remove_vowels(text))

    longest = longest_word(text)
    print("Longest word:", longest, "(", len(longest), "letters )")

    print("Word Frequency:", word_frequency(text))

text = input("Enter text: ")
analyze_text(text)