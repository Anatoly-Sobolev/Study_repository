#include <iostream>
#include <fstream>   // Для работы с файлами
#include <string>    // Для строкового типа
#include <iomanip>   // Для форматированного вывода

using namespace std;


// Структура для хранения данных о студенте
struct Student {
    string fullName; // ФИО
    int age;         // Возраст
    double averageScore; // Средний балл
};

int main() {
    setlocale(LC_ALL, "Russian");
    ifstream inputFile("students.txt"); // Создаем объект для чтения файла
    // ifstream - класс для чтения из файлов
    // "students.txt" - имя файла (должен существовать в папке с программой)

    if (!inputFile.is_open()) { // Проверяем, удалось ли открыть файл
        // .is_open() - метод, возвращающий true если файл открыт успешно
        cout << "Ошибка открытия файла!" << endl;
        return 1; // Возвращаем код ошибки
    }

    const int MAX_STUDENTS = 100; // Максимальное количество студентов
    Student students[MAX_STUDENTS];
    int count = 0; // Счетчик реально прочитанных студентов

    // Чтение данных из файла
    while (count < MAX_STUDENTS && inputFile >> ws && !inputFile.eof()) {
        // inputFile >> ws - пропускаем начальные пробельные символы
        // !inputFile.eof() - проверяем, не достигнут ли конец файла

        // Чтение ФИО (читаем всю строку до возраста)
        char ch;
        students[count].fullName = "";

        // Читаем посимвольно, пока не встретим цифру (начало возраста)
        while (inputFile.get(ch) && !isdigit(ch) && ch != '-') {
            if (ch != '\n') {
                students[count].fullName += ch;
            }
        }

        // Возвращаем считанную цифру обратно в поток
        inputFile.putback(ch);

        // Читаем возраст и средний балл
        inputFile >> students[count].age >> students[count].averageScore;

        // Игнорируем оставшиеся символы до конца строки
        inputFile.ignore(numeric_limits<streamsize>::max(), '\n');

        count++;
    }

    inputFile.close(); // Закрываем файл

    // Вывод данных на экран
    cout << "=========================================" << endl;
    cout << "СПИСОК СТУДЕНТОВ" << endl;
    cout << "=========================================" << endl;
    cout << left << setw(30) << "ФИО"
        << setw(10) << "Возраст"
        << setw(15) << "Средний балл" << endl;
    cout << "-----------------------------------------" << endl;

    // left - выравнивание по левому краю
    // setw(n) - устанавливает ширину поля для следующего вывода

    for (int i = 0; i < count; i++) {
        cout << left << setw(30) << students[i].fullName
            << setw(10) << students[i].age
            << setw(15) << fixed << setprecision(2) << students[i].averageScore
            << endl;
        // fixed - фиксированная запись дробных чисел
        // setprecision(2) - вывод с 2 знаками после запятой
    }

    cout << "=========================================" << endl;
    cout << "Всего студентов: " << count << endl;

    return 0;
}