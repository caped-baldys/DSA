#include <bits/stdc++.h>
using namespace std;

class Node
{
public:
    int coeff;
    int pow;
    Node *next;
    Node()
    {
        coeff = 0;
        pow = 0;
        next = NULL;
    }
    Node(int c, int p)
    {
        coeff = c;
        pow = p;
        next = NULL;
    }
};

class Linkedlist
{
public:
    Node *head = NULL;
    Node *tail = NULL;
    // to add data to the list
    void append(int, int);
    // to print the list
    void printL();
};

void Linkedlist::append(int data1, int data2)
{

    Node *temp = new Node(data1, data2);
    if (head == NULL)
    {
        head = temp;
        tail = head;
    }
    else
    {

        tail->next = temp;
        tail = temp;
    }
}

void Linkedlist::printL()
{
    Node *temp = head;
    while (temp != NULL)
    {
        if (temp->next == NULL)
            cout << temp->coeff << "x"
                 << "^" << temp->pow;
        else
            cout << temp->coeff << "x"
                 << "^" << temp->pow << "+";
        temp = temp->next;
    }
}

class SolutionAdd
{
public:
    Linkedlist sol;
    void Add(Linkedlist l1, Linkedlist l2)
    {

        Node *head1 = l1.head;
        Node *head2 = l2.head;
        Node *solhead = sol.head;

        if (head1 == NULL or head2 == NULL)
        {
            if (head1 == NULL)
                solhead = head2;
            else if (head2 == NULL)
                solhead = head1;
            else
                cout << "Both polynomials are empty";
            return;
        }
        else
        {
            while (head1 != NULL and head2 != NULL)
            {
                if (head1->pow == head2->pow)
                {
                    sol.append(head1->coeff + head2->coeff, head1->pow);
                    head1 = head1->next;
                    head2 = head2->next;
                }

                else if (head1->pow > head2->pow)
                {
                    sol.append(head1->coeff, head1->pow);
                    head1 = head1->next;
                }
                else if (head2->pow > head1->pow)
                {
                    sol.append(head2->coeff, head2->pow);
                    head2 = head2->next;
                }
            }
        }
    }
};
// Driver code
int main()
{

    cout << "\n Poly 1 \n";
    Linkedlist poly1, poly2;
    poly1.append(10, 4);
    poly1.append(14, 3);
    poly1.append(13, 2);
    poly1.append(11, 1);
    poly1.printL();

    cout << "\n Poly 2 \n";
    poly2.append(23, 5);
    poly2.append(19, 4);
    poly2.append(23, 3);
    poly2.append(34, 1);
    poly2.printL();
    // append(&head1,&tail1,10,12);
    // printL(head1);
    SolutionAdd result;
    cout << "\nResult::\n";
    result.Add(poly1, poly2);
    cout << "\n";
    result.sol.printL();
}
