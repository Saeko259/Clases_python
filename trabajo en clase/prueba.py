ff = {"felipe":[
    
    {"libro":"habitos atomicos",
    "fecha":"2023-02-14",
    "estado":"prestado"},
    
    {"libro":"Club 5 am",
    "fecha":"2023-02-14",
    "estado":"prestado"},
]}

if ff.get('felipe') != None:
    diccionario = {'libro':'coyas',
               'fecha':'2023-02-14',
               'estado': 'prestado'}
    ff["felipe"].append(diccionario)

usuario = ff["felipe"]

chale = usuario[1]
if chale.get('libro') == 'Club 5 am':
    print('ti')
else:
    print('ño')

chale['estado'] = 'devuetlo'

print(chale)
print(ff)
# x = [{'epa':'hola','chao':'PES'},{'que':'culote'}]

# print(x.index({'epa':'hola','chao':'PES'}))