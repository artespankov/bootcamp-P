"""
Regexp rules

Identifiers
\d - Digit. Example file_\d\d ~ file_25
\w - Alphanumeric(incl. underscores). Example \w-\w\w\w ~ A-z_1
\s - Whitespace. Example a\sb\sc ~ a b c
\D - NON Digit. Example \D\d\d ~ F16
\W - NON Alphanumeric \W\W\W\W\W ~ *-+=)
\S - NON Whitespace \S\S ~ A1

Quantifiers
+    - 1+ times. Example \w-\w+ ~ A-b1_11
{3}  - exactly 3 times. Example \d{3} ~ 777
{2,4} - from 2 to 4 times. Example \D{2,4} ~ ABC
{3,} - 3+ times. Example \S{3,} ~ 1account
* - zero or more times. Example A*B*C* ~ DODO
? - 1 time or none. Example plurals? ~ plural

Operators
| - logical OR. Example cat|dog ~ Cat is not a lion.
. - symbol prepending the pattern(wildcard). Example .on ~ Ion
^ - starts with. Example ^\d ~ 1 is a number
$ - endswith. Example \d$ ~ one is a number 1
[^] - exclude everything matching pattern inside. Example [^\d] ~ 'home12 is the best' -> 'home is the best'.
      besides, [] - is just a grouping of patterns.
() - combine statements. Example cat(fish|nap) ~ Hello, would you like some catfish?
"""

import re

text = "My phone number is 408-77-1234"

# Search by pattern
phone = re.search(r"\d{3}-\d{2}-\d{4}", text)
phone.group()

# Compile the pattern as set of groups - allows to access each section of matched text separately
phone_patter = re.compile(r'(\d{3})-(\d{2})-(\d{4})')
results = re.search(phone_patter, text)
results.group(1)

# Logical OR
re.search(r'cat|dog', "The dog is here")

# Wildcard (prepending)
re.findall(r'.at', 'The cat in the hat sat there.')
# ['cat', 'hat', 'sat']
# starts with
re.findall(r'^\d', '1 is a number')
# ends with
re.findall(r'\d$', 'one is a number 1')

# Exclusion
test_phrase = "This is string! But it has spec symbols #!-)(). How can we remove that?"
clean = re.findall(r'[^\W]+', test_phrase)

# Grouping
text = 'Only find the hypen-words in this sentence. But you do not know how long-is the dash'
re.findall(r'[\w]+-[\w]+', text)

# Combine statements
text = 'Hello, would you like some catfish?'
text2 = 'Hello, would you like to take a catnap?'
re.search(r'cat(fish|nap)', text2)