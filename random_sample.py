import random

n = random.randint(0,5)
n = random.random()
print(n)

list_a = [1,5,6,7,4,2,5,5,8]
random.shuffle(list_a)
print(list_a)

# random.randrange
a = random.randrange(0, 20, 2)
a = random.randrange(0, 30, 3)
print(a)

#choice

list_a = ['apple', 'banan', 'grape']
print(random.choice(list_a))

#choices
list_b = random.choices(list_a, k=10)
print(list_b, type(list_b))

#sample
list_b = random.sample(list_a, k=3)
print(list_b,type(list_b))

#gauss
print(random.gauss(0,2))
print(random.normalvariate(0,1))

#seed
random.seed(1)
for x in range(10):
    print(random.random())