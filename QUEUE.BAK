#include<stdio.h>
#include<conio.h>
#define MAX 50
void insert();
void deletee();
void display();
int queue[MAX];
int rear=-1;
int front=-1;
main()
{	int choice;
	clrscr();
	while(1)
	{	printf("1.Insert element to queue\n2.Delete element\n3.Display elements\n4.Exit\n***Enter your choice: ");
		scanf("%d",&choice);
		switch(choice)
		{	case 1:insert();
				break;
			case 2:deletee();
				break;
			case 3:display();
				break;
			case 4:exit(0);
				break;
			default:printf("Invalid Choice");
				break;
		}
	}
}
void insert()
{	int a;
	printf("Enter the element to insert: ");
	scanf("%d",&a);
	if(rear==MAX-1)
		printf("Queue Overflow");
	if(front==-1&& rear==-1)
	{	front=0;
		rear=0;
	}
	else
		rear=rear+1;
	queue[rear]=a;
	printf("Value Inserted\n");

}
void deletee()
{	if(front==-1||front>rear)
	{	printf("Queue Underflow\n");
		return;
	}
	else
	{	printf("Element deleted from queue is:%d\n",queue[front]);
		front=front+1;
	}
}
void display()
{	int i;
	if(front==-1)
		printf("Queue is empty\n");
	else
	{	printf("Queue is: \n");
		for(i=front;i<=rear;i++)
			printf("%d",queue[i]);
		printf("\n");
	}
}