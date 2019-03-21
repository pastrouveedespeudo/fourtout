lines = ['2', 'angleterre;suisse;italie;allemagne', 'ryan;malone;arcu;+33-8884;etas-unis', 'bruce;ellison;tortor;-33-125090826;etas-unis']

lpays = lines[1].split(';')

entreprise = []

for i in lines[2:]:
    i = i.split(";")
    entreprise.append(i)

dico = {}
yo = []
for i in entreprise:
    for j in i:
        dico[j] = 0
        
        a = dict((cle,valeur+1) for (cle, valeur) in dico.items() if cle == j)
        yo.append(a)
    
doublon = ([val for i in yo for val in i.values() if val > 1])

  
a=0
X = sum([a+i for i in doublon])

num = ""

commence_par_plus = [(i[3],True) for i in entreprise if i[3][0] == "+"]



sa=[]
for i in commence_par_plus[0][0][1:]:
    if i == "-":
        break
    sa.append(i)
    




print(sa)
print(commence_par_plus)


results = ['1', '2', '3']
results = list(map(int, results))
print(results)



print(X)




























# 2 2 4
