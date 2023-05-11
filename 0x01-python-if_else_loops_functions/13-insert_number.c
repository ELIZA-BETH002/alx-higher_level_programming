#include <stdlib.h>

typedef struct listint_s {
    int n;
    struct listint_s *next;
} listint_t;

/**
 * insert_node - Inserts a node with the given number into a sorted linked list.
 * @head: A pointer to a pointer to the head of the linked list.
 * @number: The number to insert into the linked list.
 *
 * Return: The address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node, *prev_node, *cur_node;

    /* Allocate memory for the new node */
    new_node = malloc(sizeof(listint_t));
    if (new_node == NULL)
        return (NULL);

    /* Initialize the new node */
    new_node->n = number;
    new_node->next = NULL;

    /* If the linked list is empty, insert the new node at the beginning */
    if (*head == NULL) {
        *head = new_node;
        return (new_node);
    }

    /* Traverse the linked list to find the position to insert the new node */
    prev_node = NULL;
    cur_node = *head;
    while (cur_node != NULL && cur_node->n < number) {
        prev_node = cur_node;
        cur_node = cur_node->next;
    }

    /* Insert the new node at the correct position */
    if (prev_node == NULL) {
        new_node->next = *head;
        *head = new_node;
    } else {
        prev_node->next = new_node;
        new_node->next = cur_node;
    }

    return (new_node);
}

