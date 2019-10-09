import re

pattern = '^good' # Metacharacter ^ (start of a strings)
ma = re.match(pattern, 'good morning to people. good night')
print(ma)

pattern = 'all$' # metacharacter $ (end of a string)
ma = re.search(pattern, 'good morning to people. good night to all')
print(ma)

pattern = '[abc]' # Metacharacter character class. Any string which has either a or b or c
ma = re.findall(pattern, 'hello guys. a treat to watch')
print(ma)

pattern = '[^abc]' # Match everything except a or b or c
ma = re.search(pattern, 'hello guys. a treat to watch')
print(ma)

pattern = '[5-9]' # range within the character class
ma = re.findall(pattern, 'hello guys. a 945 treat to watch')
print(ma)

pattern = 'abe*d' # metacharacter * 0 or more occurences
ma = re.match(pattern, 'abeeeeeee')
print(ma)

pattern = 'abe+d' # metacharacter + 1 or more occurences
ma = re.match(pattern, 'abed')
print(ma)

pattern = 'abe?d' # metacharacter ? 0 or 1 occurence
ma = re.match(pattern, 'abd')
print(ma)

pattern = 'com|xyz' # Metacharacter either com or xyz
ma = re.search(pattern, 'hellocomfgd')
print(ma)

pattern = '(gmail|yahoo)\.com$' # Metachaaracter () -> group multiple rules
# . metacharacter that indicates a single character. \ escapes the regular expression meta char meaning
ma = re.search(pattern, 'mehul@yahoo.com')
print(ma)

pattern = 'a{2,4}' # Metachaaracter {min, max}
ma = re.findall(pattern, 'aaaaabcaaaab')
print(ma)

# common regular expression sequences
pattern = '\Agood' # should start with good
ma = re.search(pattern, 'good morning')
print(ma)

pattern = r'\ba'
ma = re.search(pattern, 'good mornina')
print(ma)

pattern = r'\d+'
ma = re.findall(pattern, 'good mornina. Gr8 8798')
print(ma)

msg = 'good      morning to              all'
pattern = r'\s+'
print(re.split(pattern, msg))

pattern = r'\w+'
email = 'mehul_chopra.25@gmail.com'
ma = re.findall(pattern, email)
print(ma)

# mobile numbers (8, 10)
pattern = r'^\d{8,10}$'
ma = re.match(pattern, '9875645698786')
print(ma)

pattern = r'^[a-z][a-z0-9]*(\$|@)$'
ma = re.match(pattern, 'mehul987686kjhgjAER@')
print(ma)

msg = 'good      morning to              all'
pattern = r'\s+'
m = re.sub(pattern, ' ', msg)
print(m)