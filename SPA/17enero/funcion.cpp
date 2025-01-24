#include <iostream>
using namespace std;

void capturar_enteros();
void mostrar_cadena(string cadena, int n) {
    for(int i=0; i<n; i++) {
        cout<< cadena << "\n";
    }
}

struct Personaje
{
    string tipo;
    float fuerza;
    int salud;
    string nombre;
};


int main() {
    //capturar_enteros();
    //mostrar_cadena("CUCEI", 10);
    struct Personaje p01;
    p01.tipo = "Tanque Pesado";
    p01.fuerza = "360";
    p01.salud = 4500;
    p01.nombre = "Maus";

    cout << "Tipo: " << p01.tipo << "\n";
    cout << "Fuerza: " << p01.fuerza << "\n";
    cout << "Salud: " << p01.salud << "\n";
    return 0;
}

void capturar_enteros() {
    int arreglo[5];
    int temp;

    for (int i=0; i<0; i++) {
        cout<< "entero: ";
        cin>> temp;
        arreglo[i] = temp;
    }
    for (int i=0; i<5; i++) {
        cout<< arreglo[i] << ".";
    }
}