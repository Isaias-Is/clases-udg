#include <iostream>
#include <fstream>
#include <string>
using namespace std;

struct Personaje
{
    string tipo;
    float fuerza;
    int salud;
}personajes[5];

int cont = 0;

void agregar_personaje() {
    if (cont >= 5) {
        cout << "El arreglo esta llo" << "\n";
        return;
    }

    string tipo;
    float fuerza;
    int salud;
    cout<< "tipo: ";
    cin>> tipo;
    cout<< "fuerza: ";
    cin>> fuerza;
    cout<< "salud: ";
    cin>> salud;

    personajes[cont].tipo = tipo;
    personajes[cont].fuerza = fuerza;
    personajes[cont].salud = salud;

    cont++;
}

void mostrar_personaje() {
    if (cont == 0) {
        cout << "El arreglo esta vacío" << "\n";
        return;
    }
    for (int i = 0; i < cont; i++) {
        cout << "tipo: " << personajes[i].tipo << "\n";
        cout << "fuerza: " << personajes[i].fuerza << "\n";
        cout << "salud: " << personajes[i].salud << "\n";
        cout << "\n";
    }
}

void eliminar_ultimo() {
    if (cont == 0) {
        cout << "No se puede eliminar, arrglo esta vacío" << "\n";
        return;
    }

    cont--;
}

void respaldar() {
    ofstream archivo("personajes.csv");

    if (!archivo.is_open()) {
        cout << "Error al crear el archivo" << "\n";
        return;
    }

    for (int i=0; i<cont; i++) {
        string tipo = personajes[i].tipo;
        float fuerza = personajes[i].fuerza;
        int salud = personajes[i].salud;
    
        archivo << tipo << "," << fuerza << "," << salud << "\n";
    }
    archivo.close();
}

void recuperar() {
    ifstream archivo("personajes.csv");

    if (!archivo.is_open()) {
        cout<< "Error al abrir el archivo" << "\n";
        return;
    }

    while (true) {
        string tipo;
        float fuerza;
        int salud;
        string temp;

        getline(archivo, temp, ",");
        if (archivo.eof()) break;
        tipo = temp;
        getline(archivo, temp, ",");
        fuerza = stof(temp);
        getline(archivo, temp, ",");
        salud = stoi(temp);

        personajes[cont].tipo = tipo;
        personajes[cont].fuerza = fuerza;
        personajes[cont].salud = salud;
        cont++;
    }
}

int main() {
    int op;

    while (true) {
        cout << "1) Agregar Personaje" << "\n";
        cout << "2) Mostrar Personaje" << "\n";
        cout << "3) Eliminar último" << "\n";
        cout << "4) Cantidad" << "\n";
        cout << "5) Respaldar" << "\n";
        cout << "6) Recuperar" << "\n";
        cout << "0) Salir" << "\n";
        cin >> op;

        if (op == 0) {
            cout << "Salir" << "\n";
            break;
        }

        switch (op) {
            case 1:
                agregar_personaje();
                break;
            
            case 2:
                mostrar_personaje();
                break;

            case 3:
                eliminar_ultimo();
                break;
            case 4:
                cout << "cantidad de personajes: " << cont << "\n";
                break;
            case 5:
                respaldar();
                break;
            case 6:
                recuperar();
                break;
            default:
                cout << "Opción no válida" << "\n";
        }
    }
}