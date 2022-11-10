#include<stdio.h>
#include<stdlib.h>
void push();
void pop();
void display();
struct node
{	int val;
	struct node *next;
};
struct node *head;
void main
{	int choice=0;
	clrscr();
	do
	{	printf("1.Insert an element\n2.Delete an element\nDisplay the stack\n4.exit\n*****Enter your choice:");
		scanf("%d",&choice);
		switch(choice)
		{	case 1:push();
				break;
			case 2:pop();
				break;
			case 3:display();
				break;
			case 4:exit(0);
				break;
			default:printf("Invalid choice");
		}

	}while(choice!=4);
	getch();
}
void push()
{	int val;
	struct node *ptr=(struct node*)malloc(sizeof(struct node));
	if(ptr==NULL)
		printf("Unable to insert the element");
	else
	{	printf("Enter the value:");
		scanf("%d",&val);
		if(head==NULL)
		{	ptr->