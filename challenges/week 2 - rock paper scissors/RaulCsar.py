j1=input().split(" ")
j2=j1[1]
t=("pedra","papel","tesoura")
v1="Jogador 1"
v2="Jogador 2"
while j1!=" ":
    if j1[0]==j2:
        print("Não há ganhador")
    elif(j1[0]==t[0]and j2==t[1])or(j1[0]==t[1]and j2==t[2])or(j1[0]==t[2]and j2==t[0]):
        print(v2)
    else:
        print(v1)
    j1=input().split(" ")

    