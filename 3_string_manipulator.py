#string manipulator
#ask user for sentence
sentence=(input("Enter a sentence:"))
print("Orginal:",sentence) #it will display original sentence
print("Characters with spaces:",len(sentence)) #it will display total characters with space
print("Characters without spaces:",len(sentence)) #it will display total characters without space
print("Words:",len(sentence.split())) #it will print total words
print("UPPERCASE:",sentence.upper()) #it will display total sentence in uppercase
print("lowercase:",sentence.lower()) #it will display total sentence in lowercase
print("Title Case:",sentence.title()) #it will display the title
print("First word:",sentence.split()[0]) #it will display first word
print("Last word:",sentence.split()[-1]) #it will display last word
print("Reversed:",sentence[::-1]) #it will display sentence in reversed