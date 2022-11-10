#include<stdio.h>
#include<conio.h>
void main()
{	int a[20],b[20],c[40],s1,s2,s3,i,j,k,temp;
	clrscr();
	printf("Enter the size of first array: ");
	scanf("%d",&s1);
	printf("Enter the elements of first array:\n");
	for(i=0;i<s1;i++)
		scanf("%d",&a[i]);
	printf("Array 1: ");
	for(i=0;i<s1;i++)
		printf("%d\t",a[i]);
	for(i=0;i<s1-1;i++)
	{	for(j=i+1;j<s1;j++)
		{	if(a[i]>a[j])
			{	temp=a[i];
				a[i]=a[j];
				a[j]=temp;
			}
		}
	}
	printf("\n\nEnter the size of second array: ");
	scanf("%d",&s2);
	printf("Enter the elemnts of second array:\n");
	for(i=0;i<s2;i++)
		scanf("%d",&b[i]);
	printf("Array 2: ");
	for(i=0;i<s2;i++)
		printf("%d\t",b[i]);
	for(i=0;i<s2-1;i++)
	{	for(j=i+1;j<s2;j++)
		{	if(b[i]>b[j])
			{	temp=b[i];
				b[i]=b[j];
				b[j]=temp;
			}
		}
	}
	s3=s1+s2;
	i=0;j=0;k=0;
	while(i<s1&&j<s2)
	{	if(a[i]<=b[j])
		{	c[k]=a[i];
			k++;
			i++;
		}
		else
		{	c[k]=b[j];
			k++;
			j++;
		}
	}
	while(i<s1)
	{	c[k]=a[i];
		k++;
		i++;
	}
	while(j<s2)
	{	c[k]=b[j];
		k++;
		j++;
	}
	printf("\nMerged Array: ");
	for(i=0;i<s3;i++)
		printf("\t%d",c[i]);
	getch();
}