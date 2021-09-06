#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * check_cycle - function that checks if a singly linked list has a cycle in it
 * @list: linked list.
 * Return: 0 if list doesn't have a cycle, 1 if it does.
 */

int check_cycle(listint_t *list)
{
	while (list)
	{
		if (list->next >= list)
			return (1);
		list = list->next;
	}

	return (0);
}
