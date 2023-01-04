p=prompt
i=p()
j=p()
alert(i!=j?"Jogador "+({pedra:"tesoura",papel:"pedra",tesoura:"papel"}[i]==j?1:2):"Não há ganhador")