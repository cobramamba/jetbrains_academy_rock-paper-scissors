text = input()
words = text.split()
print(words)
for word in words:
    # finish the code here
    if 'www.' in word.lower() or 'http://' in word.lower() or 'https://' in word.lower():
        print(word)
