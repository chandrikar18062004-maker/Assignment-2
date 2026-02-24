#palindrome checker
#taking input from user
text = input("Enter word/number: ")

print("Original:", text)

#convert to lowercase to handle case
text_lower = text.lower()

#reverse the text using loop
reverse = ""

for i in range(len(text_lower) - 1, -1, -1):
    reverse = reverse + text_lower[i]

print("Reversed:", reverse)

#check if original and reversed are same
if text_lower == reverse:
    print("Result: PALINDROME")
else:
    print("Result: NOT PALINDROME")