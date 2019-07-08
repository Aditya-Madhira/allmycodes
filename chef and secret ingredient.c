#include<stdio.h>
main ()
{
  int n,min,a[100],flag=0,i,j;
  printf("enter number of students");
  scanf("%d",&n);
  printf("\nenter minimum amount chef needs");
  scanf("%d",&min);
  printf("\nenter amount students used");
  for(i=0;i<n;i++)
  {
    scanf("%d",&a[i]);
  }
  for(i=0;i<n;i++)
  {
    for(j=i+1;i<n;i++)
    {
      if(a[i]>=min)
      flag=1;
      break;
    }
  }
  if(flag==1)
  {
    printf("YES");
  }
  else
  {
    printf("NO");
  }

}
