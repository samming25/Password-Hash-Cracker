import hashlib
word=input("Enter the word to be encoded:")
hashed_word=hashlib.md5(word.encode()).hexdigest()
print(hashed_word)
