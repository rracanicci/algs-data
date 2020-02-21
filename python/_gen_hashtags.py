from random import randrange

l = [
    "#business", "#productivity", "#sales", "#smallbusiness", "#startup",
    "#success", "#website", "#empreendedorismo", "#produtividade",
    "#ecommerce", "#fashion", "#moda", "#instafashion", "#online",
    "#onlinestore", "#sale", "#store", "#lojaonline", "#lojavirtual",
    "#promoção", "#1YearWithPromise", "#competition", "#design",
    "#giveaway", "#concurso", "#sorteio", "#news", "#win", "#winning"
]

for h in l:
    for i in range(200000):
        print (h + '_' + str(i), randrange(100, 5000))

print ('#felizanonovo', 9999)
print ('#dxctec', 8884)
print ('#c++', 8000)
print ('#python', 7500)
print ('#c#', 7000)
print ('#java', 7000)