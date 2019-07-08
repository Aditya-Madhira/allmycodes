#include<stdio.h>
#include<math.h>
main ()
{
  int l,d,c,s,wwe,x,i;
  printf("enter number of likes to get");
  scanf("%d",&l);
  printf("enter number of days left");
  scanf("%d",&d);
  printf("enter number of likes present");
  scanf("%d",&s);
  printf("enter constant rate");
  scanf("%d",&c);
  if(l==s){
    printf("alive");
  }
  x=s+pow(c,s);
  for(i=3;i<d;i++)
  {
    s=x+pow(x,c);
    if(s>=l)
    {
      wwe=1;
      break;
    }
  }
  if(wwe==1)
  {
    printf("alive");
  }
  else if(wwe!=2)
  {
    printf("dead");
  }
}
