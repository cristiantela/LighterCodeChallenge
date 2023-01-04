<?php
// Linha acima ignorada
[$a,$b]=explode(" ", readline());
$w=['d'=>0,'p'=>1,'s'=>2];
$v=(3+$w[$a[2]]-$w[$b[2]])%3;
echo $v?"Jogador $v":"Não há vencedores";
// Linha abaixo ignorada
?>
