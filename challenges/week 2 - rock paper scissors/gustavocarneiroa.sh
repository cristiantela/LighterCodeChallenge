# NÃO REPRODUZIR NO PRÓPRIO SH, USAR UM COMPILADOR ONLINE. EX: https://www.onlinegdb.com/online_bash_shell
#155 Caracteres
read a b 
a=${a: -3:1}
b=${b: -3:1}
declare -A w
w[d]=0
w[p]=1
w[s]=2
let v=(3+w[$a]-w[$b])%3
echo $([ "$v" != 0 ] && echo "Jogador $v" || echo "Não há vencedores")
