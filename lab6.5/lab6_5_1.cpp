#include <iostream>
using namespace std;

void find_common_elements(int list1[], int size1, int list2[], int size2) {
    cout << "Common elements are: ";
    for (int i = 0; i < size1; i++) {
        for (int j = 0; j < size2; j++) {
            if (list1[i] == list2[j]) {
                cout << list1[i] << " ";
                break;
            }
        }
    }
    cout << endl;
}
