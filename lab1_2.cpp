#include <stdio.h>

#include <iostream>
using namespace std;

int main() {
    
    int var1, var2;
    int sum, diff, prod;

    
    cout << "Enter the value of first integer: ";
    cin >> var1;
    cout << "Enter the value of integer: ";
    cin >> var2;

    sum = var1 + var2;
    diff = var1 - var2;
    prod = var1 * var2;

    cout << "var1 = " << var1 << endl;
    cout << "var2 = " << var2 << endl;
    cout << "sum = " << sum << endl;
    cout << "difference = " << diff << endl;
    cout << "product = " << prod << endl;

    return 0;
}
