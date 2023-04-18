#include <iostream>
#include <cmath>

using namespace std;

int calculate_sum() {
    int n;
    cout << "Enter a value for n ";
    cin >> n;

    if (n==0) {
        return 0;
    } else {
        return calculate_sum(n-1) + pow(-1,n+1)/n;
    }
}

int main() {
    int result = calculate_sum();
    cout << "Result is: " << result << endl;
    return 0;
}