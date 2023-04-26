#include <iostream>
#include <algorithm>
using namespace std;

void find_palindromes(string strings[], int size) {
    cout << "Palindromes are: ";
    for (int i = 0; i < size; i++) {
        string str = strings[i];
        string rev_str = str;
        reverse(rev_str.begin(), rev_str.end());
        if (str == rev_str) {
            cout << str << " ";
        }
    }
    cout << endl;
}
