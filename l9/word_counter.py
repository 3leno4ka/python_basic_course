import re
from collections import defaultdict

with open('text.txt', 'r') as f_read:
    text = ''
    for line in f_read:
        text += line

words = re.split(r' |\,|\.|\n|’', text)

dict_text = defaultdict(int)
for key in words:
    if key != '':
        dict_text[key] += 1

qty_of_repeating_words = 0
for item in dict_text.items():
    if item[1] > 1:
        qty_of_repeating_words += 1
print(text)
print(f'Quantity of repeating words: {qty_of_repeating_words}')
print('Top 5 words:')
for item in sorted(dict_text.items(), key=lambda x: x[1])[:-6:-1]:
    print(f'{item[0]}: {item[1]}')
