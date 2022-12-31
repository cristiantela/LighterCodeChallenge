p,j=input().split()
print("Não há ganhador" if p==j else f"Jogador {int({'pedra': 'tesoura','papel':'pedra','tesoura':'papel'}[p]!=j)+1}")