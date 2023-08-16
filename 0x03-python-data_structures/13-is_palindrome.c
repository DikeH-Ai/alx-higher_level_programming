#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

int is_palindrome(listint_t **head) {
	listint_t *c;
	int n = 0;
	int c_size = 1;
	int *arr = malloc(sizeof(int) * c_size);
	int *new_arr;
	int i = 0;
	int j;

	c = *head;
	listint_t *cv = *head;

	if (arr == NULL) {
		return 0;
	}

	while (c != NULL) {
		c = c->next;
		n++;
	}

	if (c_size < n) {
		new_arr = realloc(arr, sizeof(int) * n);
		if (new_arr == NULL) {
			free(arr);
			return 0;
		}
		arr = new_arr;
		c_size = n;
	}

	i = 0;
	while (cv != NULL) {
		*(arr + i) = cv->n;
		cv = cv->next;
		i++;
	}

	for (j = 0; j < n / 2; j++) {
		if (*(arr + j) != *(arr + (n - j - 1))) {
			free(arr);
			return 0;
		}
	}

	free(arr);
	return 1;
}
