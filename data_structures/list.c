/* exercises 10.2-8 */
// gcc -Wall list.c
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>  // uintptr_t

typedef struct _Node
{
    int           data;
    struct _Node *np;
} Node;

static inline Node *XOR2(Node *a, Node *b)
{
    return (Node *)((uintptr_t)a ^ (uintptr_t)b);
}

static inline Node *XOR3(Node *a, Node *b, Node *c)
{
    return (Node *)((uintptr_t)a ^ (uintptr_t)b ^ (uintptr_t)c);
}

typedef struct _List
{
    /* head points to a sentinel node */
    Node *head;
    /* tail points to a sentinel node */
    Node *tail;
} List;

List *list_init(void)
/* init list with two sentinels */
{
    Node *head = calloc(1, sizeof(Node));
    Node *tail = calloc(1, sizeof(Node));
    List *list = calloc(1, sizeof(List));

    if((!head) || (!tail) || (!list))
    {
        if(head) free(head);
        if(tail) free(tail);
        if(list) free(list);

        return 0;
    }

    // head->np = tail ^ tail
    // tail->np = head ^ head

    list->head = head;
    list->tail = tail;

    return list;
}

void list_free(List *list)
{
    Node *prev = list->head;
    Node *node = XOR2(list->head->np, list->tail);
    Node *next;

    while(node != list->tail)
    {
        next = XOR2(node->np, prev);
        prev = node;

        free(node);

        node = next;
    }
    free(list->head);
    free(list->tail);
    free(list);
}

int list_search(List *list, int key)
{
    Node *prev = list->head;
    Node *node = XOR2(list->head->np, list->tail);
    Node *next;

    list->tail->data = key;
    while(node->data != key)
    {
        next = XOR2(node->np, prev);
        prev = node;

        node = next;
    }

    return node == list->tail ? 0 : 1;
}

int list_insert(List *list, int key)
/* insert a key at list end
 * the key is inserted into the sentinel node at tail
 * then create a new node between head and tail
 * the new node becomes the sentinel node at tail */
{
    Node *node = calloc(1, sizeof(Node));

    if(!node) return 0;

    list->tail->data = key;

    node->np = XOR2(list->head, list->tail);
    /* unlink tail->next with head
     * link tail->next with new created node */
    list->tail->np = XOR3(list->tail->np, list->head, node);
    /* unlink head->prev with tail
     * link head->prev with new created node */
    list->head->np = XOR3(list->head->np, list->tail, node);

    list->tail = node;

    return 1;
}

int list_delete(List *list, int key)
{
    Node *prev = list->head;
    Node *node = XOR2(list->head->np, list->tail);
    Node *next;

    list->tail->data = key;
    while(node->data != key)
    {
        next = XOR2(node->np, prev);
        prev = node;

        node = next;
    }

    if(node == list->tail)
    {
        return 0;
    }
    else
    {
        next = XOR2(node->np, prev);
        next->np = XOR3(next->np, node, prev);
        prev->np = XOR3(prev->np, node, next);

        return 1;
    }
}

void list_reverse(List *list)
{
    /* swap(a, b) == (a ^= b, b ^= a, a ^= b) */
    list->head = XOR2(list->head, list->tail);
    list->tail = XOR2(list->head, list->tail);
    list->head = XOR2(list->head, list->tail);
}

void list_print(List *list)
{
    Node *prev = list->head;
    Node *node = XOR2(list->head->np, list->tail);
    Node *next;

    while(node != list->tail)
    {
        next = XOR2(node->np, prev);
        prev = node;

        printf("%d ", node->data);

        node = next;
    }
    putchar('\n');
}

int main(int argc, char *argv[])
{
    List *list = list_init();

    list_insert(list, 1);
    list_insert(list, 2);
    list_insert(list, 3);
    list_insert(list, 4);
    list_insert(list, 5);
    list_print(list);

    list_delete(list, 4);
    list_delete(list, 2);
    list_print(list);

    printf("%d %d\n", list_search(list, 1), list_search(list, 2));

    list_reverse(list);
    list_print(list);

    list_free(list);
    return 0;
}
