p=prompt
x=p()
y=p()
t=0

for(i=x;i<=y;i++)
  t+=!!(!(i%4)&&(i%100||!(i%400)))

alert(t);