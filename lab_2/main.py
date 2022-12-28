import json
from Car import Car
from Audi import Audi
from BMW import BMW
from Mersedes import Mersedes
from VAZ import VAZ

def write(data):
    jsonstr = json.dumps(data, indent = 4)
    open('./objects.json', 'w').write(jsonstr)
def read_from_json():
    return json.load(open('./objects.json', 'r'))

c = Car(120, "green", 250)
a = Audi(140, "red", 270, "Q7", 14)
b = BMW(100, "black", 230, "M3", 1998)
m = Mersedes(150, "white", 290, "GLE Coupe I", "S")
v = VAZ(70, "cherry", 130, "five", "good")
l = [c, a, b, m, v]
data = {
    'amount' : len(l),
    'obj' : []
}
for elem in l:
    data['obj'].append(elem.__dict__)

#print (data)
write(data)
data.clear()
l.clear()
data = read_from_json()
for elem in data['obj']:
    if elem['name'] == "Car":
        obj = Car(elem['_hp'], elem['_color'], elem['_max_speed'])
    elif elem['name'] == "Audi":
        obj = Audi(elem['_hp'], elem['_color'], elem['_max_speed'], elem['_model'], elem['_wheel_radius'])
    elif elem['name'] == "BMW":
        obj = BMW(elem['_hp'], elem['_color'], elem['_max_speed'], elem['_model'], elem['_year_realise'])
    elif elem['name'] == "Mersedes":
        obj = Mersedes(elem['_hp'], elem['_color'], elem['_max_speed'], elem['_model'], elem['_clas'])
    elif elem['name'] == "VAZ":
        obj = VAZ(elem['_hp'], elem['_color'], elem['_max_speed'], elem['_model'], elem['_condition'])
    l.append(obj)
for elem in l:
    print(elem)
    #сдано