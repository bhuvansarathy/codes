#remove vowels in the string 
text = input("Enter text: ")
result = ""

for i in text:
    if i not in "aeiouAEIOU":
        result += i

print(result)
