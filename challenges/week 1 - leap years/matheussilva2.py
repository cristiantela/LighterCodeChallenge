ano = int(input("Digite o ano: "))
bisexto = (ano%4==0 and ano%100!=0) or (ano % 400 == 0)
print(f"O ano {ano} é bisexto" if bisexto else f"O ano {ano} não é bisexto")