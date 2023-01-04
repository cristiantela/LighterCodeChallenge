#include <stdio.h>
int main(){
char a,b,c,*d[]={"Jogador %d","Não há ganhador"};
scanf("%*2c%c%*s %*2c%c",&a,&b);
c=(a-=b)%5;
printf(d[a?0:1],c>0|!c&b-'d'?1:2);
}
