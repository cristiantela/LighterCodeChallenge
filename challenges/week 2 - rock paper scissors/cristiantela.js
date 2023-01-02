[[,,a],[,,b]]=prompt().split(' ');
alert(a==b?'Não há ganhador':'Jogador '+({'sp':1,'ds':1,'pd':1}[a+b]||2))
