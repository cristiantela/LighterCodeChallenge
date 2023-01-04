package main

import (
  "bufio"
  "fmt"
  "os"
  "strings"
  "strconv"
)

func main() {
  // Linhas acima ignoradas
  // Caracteres: 277
  i,_:=bufio.NewReader(os.Stdin).ReadString('\n')
  i=strings.Replace(i, "\n", "", -1)
  p:=strings.Split(i, " ")
  w:=make(map[string]int)
  w["d"] = 0
  w["p"] = 1
  w["s"] = 2
  
  v:=(3+w[p[0][2:3]]-w[p[1][2:3]])%3
  a:="Jogador "
  if v!=0 {
    a=a+strconv.Itoa(v)
  } else {
    a="Não há vencedores"
  }
  fmt.Println(a)
  //Linha abaixo ignorada
}
