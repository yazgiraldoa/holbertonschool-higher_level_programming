#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - function that checks if singly linked list is palindrome
 * @head: head pointer of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	int i = 0, j = 0, len = 0, mid_len = 0, first_time = 0;
	int is_even = 0;
	listint_t *aux = *head;
	int array[99999];

	if (*head == NULL)
		return (1);

	len = listint_len(*head);

	if (len % 2 == 0)
		mid_len = len / 2, is_even = 1;
	else
		mid_len = (len + 1) / 2;

	for (i = 0; aux; )
	{
		if (i < mid_len)
		{
			if (is_even == 1 || i != (mid_len - 1))
				array[i] = aux->n;
			i++;
		}
		else
		{
			if (first_time == 0)
			{
				first_time = 1, j = i - 1;
				if (is_even == 0)
					j--;
			}
			if (aux->n != array[j])
				return (0);
			j--;
		}
		aux = aux->next;
	}
	return (1);
}

/**
 * listint_len - function that returns the number of elements
 * in a linked listint_t list.
 * @h: list
 * Return: number of elements in the list
 */

int listint_len(listint_t *h)
{
	int i = 0;

	while (h != NULL)
	{
		h = h->next;
		i++;
	}
	return (i);
}
