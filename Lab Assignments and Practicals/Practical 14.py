# 14 Write a Python program to count the number of characters, words, and lines in the given text

print("Enter text (type 'END' on a new line to stop):")
text = ""
while True:
    line = input()
    if line == "END":
        break
    text += line + "\n"

# Remove the last newline added
text = text[:-1]

chars = len(text)
lines = 1
for char in text:
    if char == '\n':
        lines += 1

words = len(text.split())

print("\nCharacters:", chars)
print("Words:", words)
print("Lines:", lines)
