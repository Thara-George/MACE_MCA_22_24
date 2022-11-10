#include<stdio.h>
#include<conio.h>
void main()
{	int a[50],n,i,num,pos;clrscr();
	printf("Enter the number of elements: ");
	scanf("%d",&n);
	printf("Enter the array elements: ");
	for(i=0;i<n;i++)
		scanf("%d",&a[i]);
	printf("Enter the item to be inserted:");
	scanf("%d",&num);
	printf("Enter the position where item is to be inserted:\n");
	scanf("%d",&pos);
	for(i=n;i>=pos-1;i--)
	{a[i]=a[i-1]; }
	a[pos-1]=num;
	n=n+1;
	printf("The new array is:\n");
	for(i=0;i<n;i++)
	printf("%d""	",a[i]);
	getch();
}