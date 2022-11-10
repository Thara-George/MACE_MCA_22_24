#include<stdio.h>
#include<stdlib.h>
#define SIZE 100
int stack[SIZE];
int top;
int a;
int choice;
void push();
void pop();
void print();
int main()
{       clrscr();
	top=-1;
	do
	{	 printf("1.Insert an elment\n2.Delete an element\n3.Display the elements of the stack\n4.Exit\n***Enter your choice:");
		 scanf("%d",&choice);
		 switch(choice)
		 {	case 1:push();
				break;
			case 2:pop();
				break;
			case 3:print();
				break;
			case 4:exit(0);
				break;
			default:printf("Invalid Choice\n");
				break;
		 }
	 }	 while(choice!=4);
	 return 0;
}

void push()
{	int value;
	if(top==SIZE-1)
	{	printf("The Stack is empty");
	}
	else
	{	printf("Enter the element to push into the stack:");
		scanf("%d",&value);
		printf("Element Added\n");
		top++;
		stack[top]=value;
	}
}
void pop()
{	int value;
	if(top==-1)
	{	printf("The Stack is empty\n");
	}
	else
	{	value=stack[top];
		printf("Deleted the element:%d\n",value);
		printf("Deleted\n");
		top--;
	}
}
void print()
{	if(top==-1)
	{	printf("The stack is empty\n");
	}
	else if(top>=0)
	{	printf("Elements of the stack are:\n");
		for(a=top;a>=0;a--)
		{	printf("%d\n",stack[a]);
		}
	}
}
