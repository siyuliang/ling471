import math
import statistics
import re
import nltk
import tiktoken

nltk.download('punkt')
nltk.download('punkt_tab')

print(math.sin(1))
print(math.sin(-1))
print(math.cos(math.pi))
print(math.sqrt(1))
try:
    print(math.sqrt(-1))
except:
    print('Sqrt can\'t handle complex components')
print(math.pow(4, 2))
print(math.log(10))
print(math.floor(3.14))

a = list(range(1, 11))
print(statistics.mean(a))
print(statistics.median(a))
print(statistics.stdev(a))
print(sum(a) / len(a))

# ----REGEX ACTIVITY----

s = 'The passcode is 8675309. Please remember it.'
p = re.findall(r'\d+', s)[0]
print(f'Just the passcode {p}')

p = re.sub('\d+', '555-5555', s)
print(f'Changed {p}')
# All words that start with "p"
p = re.findall(r'p\w+', s)
print(f'All words that start with "p" {p}')

# First word of each sentence
p = re.findall(r'[A-Z]\w+', s)
print(f'First word of each sentence {p}')

# Delete "Please" and capitalize "remember"
p = re.sub('Please r', 'R', s)
print(p)
print(s.replace('Please r', 'R'))

p = re.sub(r'\.', '!', s)
print(p)

# ----TOKENIZATION ACTIVITY----
s = 'Here is some simple text to work with.'
print(nltk.tokenize.word_tokenize(s))

s = '[hɪɹ iz sʌm tɛkst ɹɪʔn̩ juzɪ̃ŋ ði a͡ɪ pʰi eɪ]'
s = "Some people write money as $2.44, but others write it as 2.44$."
s = 'here is some more lovely 🥺🥰🫰 text to look at, but I don\'t like it 😤😤😡😡'
s = "Dr. Nefario's email is test@example.com, and he paid $2.99 for café 😊"
s = "This is a state-of-the-art system."
print(s.split())
print(nltk.tokenize.wordpunct_tokenize(s))
print(nltk.tokenize.word_tokenize(s))

enc = tiktoken.get_encoding("cl100k_base")
tokens = enc.encode(s)
print(tokens)
print([enc.decode([t]) for t in tokens])