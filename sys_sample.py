import sys

print(sys.version)
print(sys.path)

print(sys.argv)

#stdout

#with open('tmp.txt', mode='w') as fh:
#    sys.stdout =fh
#    print('A'*100)

#sizeof
list_a = [x for x in range(100)]
print(sys.getsizeof(list_a))

#exit

sys.exit(1)

print('A'* 100)
