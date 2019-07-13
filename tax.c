#include<stdio.h>
void main ()
{
  int N,amountinslab[100],i,percentageoftax[100],rebate,num,taxpayed[100],tt[100],totalsal[10000000],result=0;
  printf("enter number of sabs");
  scanf("%d",&N);
  printf("enter amount in slab");
  for(i=0;i<N;i++)
  {
    scanf("%d",&amountinslab[i]);
  }
  printf("percentage of tax applied on each slab");
  for(i=0;i<N;i++){
    scanf("%d",&percentageoftax[i]);
  }
  printf("enter rebate value");
  scanf("%d",&rebate);
  printf("enter number of employees");
  scanf("%d",&num);
  printf("enter tax payed by each employee");
  for(i=0;i<num;i++)
  {
    scanf("%d",&taxpayed[i]);
  }
  for(i=0;i<num;i++){
    if(taxpayed[i]>0 && taxpayed[i]<amountinslab[i])
    {
      tt[i]=percentageoftax[i];
    }
    else if(taxpayed[i]>amountinslab[i] && taxpayed[i]<amountinslab[i+1])
    {
      tt[i]=percentageoftax[i];
    }
  }
  for(i=0;i<num;i++)
  {
    totalsal[i]=taxpayed[i]*100/tt[i]-rebate;
  }
  for(i=0;i<num;i++){
    result=result+totalsal[i];
  }
  printf("%d",result);
}
