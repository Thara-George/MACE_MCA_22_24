#include<stdio.h>
#include<conio.h>
void main()
{	int a[50],pos,num,i,n;
	clrscr();
	printf("Enter the number of elements : ");
	scanf("%d",&n);
	printf("Enter the array elements : ");
	for(i=0;i<n;i++)
		scanf("%d",&a[i]);
	printf("Enter the position of the item to be deleted : ");
	scanf("%d",&pos);
	for(i=pos-1;i<n-1;i++)
		a[i]=a[i+1];
	n=n-1;
	printf("New array\n");
	for(i=0;i<n;i++)
	printf("%d""	",a[i]);
	getch();
}