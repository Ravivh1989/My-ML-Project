import nltk

s = "I can't do this now, because I'm so tired.  Please give me some time. @ sd  4 232"

words = nltk.word_tokenize(s)

words=[word.lower() for word in words if word.isalpha()]

print(words)

Output:
-----------------------------

['i', 'ca', 'do', 'this', 'now', 'because', 'i', 'so', 'tired', 'please', 'give', 'me', 'some', 'time', 'sd']
