#include <iostream>
#include <string>
using namespace std;

int main() {
    // declare variables
    string name;
    float labGrade, midtermGrade, finalGrade, lastScore;

    // prompt the user to enter the student's name and grades
    cout << "Enter the student's name: ";
    cin >> name;
    cout << "Enter the lab grade (out of 100): ";
    cin >> labGrade;
    cout << "Enter the midterm grade (out of 100): ";
    cin >> midtermGrade;
    cout << "Enter the final grade (out of 100): ";
    cin >> finalGrade;

    // calculate the last score based on the given percentages
    lastScore = labGrade * 0.25 + midtermGrade * 0.35 + finalGrade * 0.4;

    // print the name, grades, and last score
    cout << "Name: " << name << endl;
    cout << "Lab: " << labGrade << endl;
    cout << "Midterm: " << midtermGrade << endl;
    cout << "Final: " << finalGrade << endl;
    cout << "Last Score: " << lastScore << endl;

    return 0;
}