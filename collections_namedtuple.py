from collections import namedtuple

S = namedtuple('Student',['name','age','grade'])
taro = S('Taro',12,3)
print(taro.name)
print(taro[0])
taro = taro._replace(name='Jiro')
print(taro.name)
print(taro._asdict())
print(taro._fields)
dect_b = {'name':'John','age':20,'grade':2}
john = S(**dect_b)
print(john)

paul = S._make(['Paul',15,2])
print(paul)