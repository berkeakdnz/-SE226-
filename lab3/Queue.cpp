#include <iostream>
#include "Node.cpp"

using namespace std;


class Queue {
private:
    Node * front;
    Node * rear;
    int count;

public:
    Queue() {
        front = NULL;
        rear = NULL;
        count = 0;
    }

    void enqueue(int value) {
        Node* newNode = new Node(value, nullptr);
        if (front==NULL) {
            front = rear = newNode;
        } else {
            rear->next = newNode;
            rear = newNode;
        }
        count++;
    }
    void dequeue() {
        if(front == NULL) {
            cout << "Queue is empty" << endl;
        } else {
            Node* temp = front;
            front = front->next;
            delete temp;
            count--;
        }
    }

    int top() {
        if(front == NULL) {
            cout << "Queue is empty" << endl;
            return -1;
        } else {
            return front->data;
        }
    }

    bool isEmpty() {
        return front == NULL;

    }

    int size() {
        return count;
    }
};
