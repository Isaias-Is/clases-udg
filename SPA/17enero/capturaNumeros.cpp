#include <iostream>
using namespace std;

int main() {
    int arreglo[5];
    int temp;

    for (int i=0; i<0; i++) {
        cout<< "entero: ";
        cin >> temp;
        arreglo[i] = temp;
    }
    for (int i=0; i<5; i++) {
        cout<< arreglo[i] << ".";
    }

    cin >> temp;
    return 0;
}