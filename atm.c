#include<stdio.h>
#include<stdlib.h>
#define x 0.50
#include<time.h>
main ()
{
  int n,w;
  float left,final;
  srand (time(NULL));
  w=rand()%1000;
  printf("your bank account is %d",w);

  printf("\nenter amount you want to withdraw");
  scanf("%d",&n);
  left=w-n;
  final=left-x;
  if((n<=w)&&(n%5==0))
  {
    printf("\nyour transanction is succesfull");
    printf("\nthe amount left in your account is %f",final);
  }
  else
  {
    printf("your transanction cannot be completed");
  }
}
