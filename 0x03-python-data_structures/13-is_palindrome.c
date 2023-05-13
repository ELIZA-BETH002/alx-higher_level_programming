#include <lists.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct listint_s {
    int data;
    struct listint_s *next;
} listint_t;

int is_palindrome(listint_t **head) {
    if (*head == NULL || (*head)->next == NULL) {
        return 1; // Empty list or single node list is considered a palindrome
    }

    // Find the middle of the linked list
    listint_t *slow = *head;
    listint_t *fast = *head;
    while (fast->next != NULL && fast->next->next != NULL) {
        slow = slow->next;
        fast = fast->next->next;
    }

    // Reverse the second half of the linked list
    listint_t *prev = NULL;
    listint_t *curr = slow->next;
    while (curr != NULL) {
        listint_t *next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }

    // Compare the first half with the reversed second half
    listint_t *first = *head;
    listint_t *second = prev;
    while (second != NULL) {
        if (first->data != second->data) {
            return 0; // Not a palindrome
        }
        first = first->next;
        second = second->next;
    }

    return 1; // Palindrome
}

int main() {
    // Create a sample linked list
    listint_t *head = NULL;
    listint_t *node1 = malloc(sizeof(listint_t));
    listint_t *node2 = malloc(sizeof(listint_t));
    listint_t *node3 = malloc(sizeof(listint_t));
    listint_t *node4 = malloc(sizeof(listint_t));
    listint_t *node5 = malloc(sizeof(listint_t));
    
    node1->data = 1;
    node1->next = node2;
    node2->data = 2;
    node2->next = node3;
    node3->data = 3;
    node3->next = node4;
    node4->data = 2;
    node4->next = node5;
    node5->data = 1;
    node5->next = NULL;

    head = node1;

    // Check if the linked list is a palindrome
    int result = is_palindrome(&head);
    if (result == 1) {
        printf("The linked list is a palindrome.\n");
    } else {
        printf("The linked list is not a palindrome.\n");
    }

    // Clean up the memory
    while (head != NULL) {
        listint_t *temp = head;
        head = head->next;
        free(temp);
    }

    return 0;
}
