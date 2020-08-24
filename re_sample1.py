import re

txt = "I like tenis"
x = re.search(r'\bt\w+', txt)
print(type(x))
print(x.group())

pattern = r'^a...s$'
test_string = 'abyss'
resoult = re.search(pattern, test_string)
if resoult:
    print(resoult.group())
else:
    print('Not exists')

msg = 'Im 30 years old'
match = re.search(r'(\d{2}) years', msg)
print(match.group())
print(match.start())
print(match.end())
print(match.span())
print(match.re)
print(match.string)

msg = 'Im 40 years, name is Jiro.'
match = re.search(r'Im (\d{1,3}) years, name is (.*?)\.', msg)
print(match.groups())
print(match.group(1))
print(match.group(2))
