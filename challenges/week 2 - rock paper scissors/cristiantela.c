#include <stdio.h>

void main()
{
    char a,b,w,s[7];
    scanf("%c%c%c%s %c%c%c",&w,&w,&a,&s,&w,&w,&b);
        
    printf(a==b?"Não há ganhador":"Jogador %i",((a=='s'&&b=='p')||(a=='d'&&b=='s')||(a=='p'&&b=='d'))?1:2);
}
