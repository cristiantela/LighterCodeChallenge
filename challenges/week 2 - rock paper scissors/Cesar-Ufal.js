p=prompt()
a=p[2]
b=p[a=='s'?10:8]
c=a+b
alert(a==b?"Não há ganhador":"Jogador "+(c=="dp"||c=="ps"||c=="sd"?"2":"1"))
