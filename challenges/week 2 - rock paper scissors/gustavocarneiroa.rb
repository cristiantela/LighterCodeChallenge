# Caracteres: 122
require 'ostruct'
a,b = gets.chomp.split
w=OpenStruct.new({d:0,p:1,s:2})
v=(3+w[a[2]]-w[b[2]])%3
puts v!=0? "Jogador #{v}": "Não há vencedores"
