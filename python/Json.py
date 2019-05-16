import json
a=1212
person = {'name': 'jim', 'age': 25, 'city': a}

data = json.dumps(person)

print(type(data)) #<class 'str'>
print(data) #{"name": "jim", "age": 25, "city": "Taiwan"}
