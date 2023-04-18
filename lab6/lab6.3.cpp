#include <iostream>
using namespace std;

int calculate_sum(int n) {
    if (n == 0) {
        return 0;
    }
    return ((-1) * (n % 2 ? -1 : 1) * n) + calculate_sum(n - 1);
}

int main () {
    int n;
    cout << "Enter a value for n ";
    cin >> n;
    int result = calculate_sum(n);
    cout << "Result is : " << result << endl;
    return 0;
}
