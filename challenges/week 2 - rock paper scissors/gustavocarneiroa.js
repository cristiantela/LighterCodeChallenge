/* 
    Caracteres: 106
*/
[[,,a],[,,b]]=prompt().split(' ')
w={d:0,p:1,s:2}
v=(3+w[a]-w[b])%3
alert(v?'Jogador '+v:'Não há vencedores')
