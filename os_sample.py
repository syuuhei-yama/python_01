#os
import os

print(os.name)

if os.name == 'nt':
    pass
elif os.name == 'posix:':
    pass

print(os.environ.get('LANG'))
print(os.getenv('LANG'))
os.environ['my_var'] = 'nmatusumoto'
print(os.getenv('my_var'))

#getcwd ~
print(os.getcwd())
#os.chdir('std_library')
#print(os.listdir())

os.system('ls')