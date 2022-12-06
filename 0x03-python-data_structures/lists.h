#ifndef LISTS_H
#define LISTS_H

#include <stdio.h>
#include <stdlib.h>

int is_palindrome(listint_t **head);

size_t print_listint(const listint_t *h);

listint_t *add_nodeint_end(listint_t **head, const int n);

void free_listint(listint_t *head);

int main(void);
