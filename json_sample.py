#json
import json

members = {
    'ClassA': [
        {
            'Name':'Taro',
            'age':18,
            'height':175
        },
        {
            'Name':'Hanako',
            'age':17,
            'height':160
        }
    ]
}

str_json = json.dumps(members)
#print(str_json)
#print(type(str_json))
str_json_2 = '{"ClassA": [{"Name": "Taro", "age": 18, "height": 175}, {"Name": "Hanako", "age": 17, "height": 160}]}'

#dict_json = json.loads(str_json_2)
#print(dict_json)
#print(type(dict_json))


