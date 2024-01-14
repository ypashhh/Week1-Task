'''One approach to analysing some encrypted data where a substitution is suspected
is frequency analysis. A count of the different symbols in the message can be used
to identify the language used, and sometimes some of the letters. In English, the
most common letter is "e", and so the symbol representing "e" should appear most
in the encrypted text.
Write a program that processes a string representing a message and reports the six
most common letters, along with the number of times they appear. Case should
not matter, so "E" and "e" are considered the same.
Hint: There are many ways to do this. It is obviously a dictionary, but we will want
zero counts, so some initialisation is needed. Also, sorting dictionaries is tricky, so
best to ignore that initially, and then check the usual resources for the runes'''

message = input("Enter a string: ").lower()
words = []

for i in message:
    if (ord(i) >= 97 and ord(i) <= 122) or (ord(i) >= 65 and ord(i) <= 90):
        words.append(i)
    
freq = {}

for i in words:
    freq[i] = freq.get(i, 0) + 1

sorted_freq = sorted(freq.items(), key = lambda x : x[1], reverse = True)

for i in range(min(6, len(sorted_freq))):
    print(f"{sorted_freq[i][0]} : {sorted_freq[i][1]}")
    