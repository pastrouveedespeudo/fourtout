from operator import attrgetter, itemgetter

lines = ['15', 'education', 'economie', 'animation', 'campus', 'education', 'animation']

nmbre_tag = lines[0]

dico = {}

for i in lines[1:]:
    dico[i] = 0





for cle, valeur in dico.items():
    for i in lines[1:]:
        if cle == i:
            dico[i] += 1

a = sorted(dico.values())
a = a[::-1]



b = sorted(dico.items(), key=itemgetter(1), reverse=True)

c = []
for i in b:

    c.append(str(i[0]))
    c.append(str(i[1]))



a = ''
for i in c:
    try:
        i = int(i)
    except:
        pass
    a += i
    a += ' '
print(a)












    
