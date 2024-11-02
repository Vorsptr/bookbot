import re

f = open('books/frankenstein.txt', 'r')
full_sentence = f.read()
words = full_sentence.split()

lower_string = full_sentence.lower()

abc = ''.join(re.findall('[a-z]+', lower_string))
characters = {}

for char in abc:
    if char not in characters:
        characters[char] = 1
    else:
        characters[char] += 1
        
report = ''
report += '--- Begin report of books/frankenstein.txt ---\n'
report += f'{len(words)} words found in the document\n\n'
for key in characters:
    report += f"The '{key}' character was found {characters[key]} times\n"

report += '--- End report ---'

print(report)