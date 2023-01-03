### Caracteres: 113 ###
a,b=input().split()
w={'d':0,'p':1,'s':2}
v=(3+w[a[2]]-w[b[2]])%3
print(v and"Jogador "+str(v)or"Não há vencedores")
