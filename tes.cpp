#include<bits/stdc++.h>

using namespace std;

class Node{
    public:
    //data
    int data = 0;
    //NEXT
    Node * nxt =  NULL;
};



int main()
{
    Node * head1; 
    int t , data;
    cout<<"test cases";
    cin>>t;
    int t1 = t;
    while(t!=0){
        cout<<"data: ";
        cin>>data;
        if (head1 == NULL){
            head1->data = data;
            head1->nxt = NULL;
        }
        else{
            Node *newnode = new Node;
            newnode->data = data;
            newnode->nxt = head1;
            head1 = newnode;
            
        }
       
        t--;
    }
    
   
    Node *temp;
   for(temp = head1; t1!= 0 ; temp = temp->nxt) {
        cout<<temp->data<<" ";
        t1--;
   }
    cout<<"\n"<<"END";
    free(temp);
    
}