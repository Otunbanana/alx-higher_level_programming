#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
* is_palindrome - checks if a singly linked list is a palindrome
* @head: pointer to the head of the list
* Return: 1 if palindrome, 0 otherwise
*/
int is_palindrome(listint_t **head)
{
listint_t *slow, *fast, *prev_slow, *mid_node;
int is_palindrome = 1;

if (*head == NULL || (*head)->next == NULL)
return (1);

slow = fast = *head;

while (fast != NULL && fast->next != NULL)
{
fast = fast->next->next;

prev_slow = slow;

slow = slow->next;
}

if (fast != NULL)
{
mid_node = slow;
slow = slow->next;
}

prev_slow->next = NULL;
prev_slow = NULL;
while (slow != NULL)
{
fast = slow->next;
slow->next = prev_slow;
prev_slow = slow;
slow = fast;
}

while (*head != NULL && prev_slow != NULL)
{
if ((*head)->n != prev_slow->n)
{
is_palindrome = 0;
break;
}

*head = (*head)->next;
prev_slow = prev_slow->next;
}

slow = NULL;
while (prev_slow != NULL)
{
fast = prev_slow->next;
prev_slow->next = slow;
slow = prev_slow;
prev_slow = fast;
}

if (mid_node != NULL)
{
prev_slow = slow;
slow = slow->next;
prev_slow->next = mid_node;
mid_node->next = slow;
}

return (is_palindrome);
}
