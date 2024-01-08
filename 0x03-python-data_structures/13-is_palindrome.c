#include <stddef.h>
#include "lists.h"

/**
* reverse_list - Reverses a linked list.
* @head: Pointer to the head of the list.
* Return: Pointer to the new head of the reversed list.
*/
listint_t *reverse_list(listint_t *head)
{
listint_t *prev = NULL, *next = NULL;

while (head)
{
next = head->next;
head->next = prev;
prev = head;
head = next;
}

return (prev);
}

/**
* is_palindrome - Checks if a singly linked list is a palindrome.
* @head: Pointer to the head of the list.
* Return: 1 if palindrome, 0 otherwise.
*/
int is_palindrome(listint_t **head)
{
if (!*head || !(*head)->next)
return (1);

listint_t *slow = *head, *fast = *head, *prev = NULL, *mid = NULL;
int palindrome = 1;

while (fast && fast->next)
{
prev = slow;
slow = slow->next;
fast = fast->next->next;
}

mid = fast ? (slow = slow->next) : NULL;
prev = reverse_list(prev);

while (*head && prev)
{
if ((*head)->n != prev->n)
{
palindrome = 0;
break;
}
*head = (*head)->next;
prev = prev->next;
}

*head = reverse_list(prev);

if (mid)
{
prev = *head;
*head = (*head)->next;
prev->next = mid;
mid->next = *head;
}

return (palindrome);
}
