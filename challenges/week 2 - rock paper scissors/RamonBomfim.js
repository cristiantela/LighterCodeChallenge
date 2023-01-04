[[,,a],[,,b]]=prompt().split(' ')
var[s,d,p]=['s','d','p']
alert(a==b?'Não há ganhador':'Jogador '+(a==s&&b==d||a==d&&b==p||a==p&&b==s?'2':'1'))
