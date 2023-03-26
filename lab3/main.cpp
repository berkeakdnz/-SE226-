#include <iostream>
using namespace std;
#include <new>
#include "Queue.cpp"


int main() {
    Queue q;
    q.enqueue(1);
    q.enqueue(2);
    q.enqueue(3);
    q.enqueue(4);
    q.enqueue(5);

    if(q.isEmpty()) cout<<"Queue is empty "<<endl;
    cout<<"Queue size is "<<q.size()<<endl;


    cout<<q.top()<<endl;
    q.dequeue();
    cout<<q.top()<<endl;
    q.dequeue();
    cout<<q.top()<<endl;

    cout<<"Queue size is " <<q.size()<<endl;

    return 0;
}
