ano1 = int(input("Digite o primeiro ano: "))
ano2 = int(input("Digite o segundo ano: "))
anos_bissextos = 0
for ano in range(ano1,ano2+1):
	bisexto = (ano%4==0 and ano%100!=0) or (ano % 400 == 0)
	if(bisexto):
		anos_bissextos += 1

print(f"Entre {ano1} e {ano2}, existem {anos_bissextos} anos bissextos")