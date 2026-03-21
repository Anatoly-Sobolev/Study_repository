#include <iostream>
#include <cstring>
#include <cctype>

using namespace std;
void calculateSumAndProduct(int a, int b, int* sum, int* product) {
    *sum = a + b;
    *product = a * b;
}

void countVowelsAndConsonants(const char* str, int* vowels, int* consonants) {
    *vowels = 0;
    *consonants = 0;

    const char* vowelChars = "aeiouyAEIOUY";
    for (int i = 0; str[i] != '\0'; i++) {
        char c = str[i];

        if (isalpha(c)) {
            if (strchr(vowelChars, c) != nullptr) {
                (*vowels)++;
            }
            else {
                (*consonants)++;
            }
        }
    }
}

void findMinMax(const int* arr, int size, int* minVal, int* maxVal) {
    if (size <= 0) {
        *minVal = 0;
        *maxVal = 0;
        return;
    }

    *minVal = arr[0];
    *maxVal = arr[0];

    for (int i = 1; i < size; i++) {
        if (arr[i] < *minVal) {
            *minVal = arr[i];
        }
        if (arr[i] > *maxVal) {
            *maxVal = arr[i];
        }
    }
}

int main() {
    setlocale(LC_ALL, "Russian");
    int x = 5, y = 7;
    int sum, product;

    calculateSumAndProduct(x, y, &sum, &product);
    cout << "Числа: " << x << " и " << y << endl;
    cout << "Сумма: " << sum << endl;
    cout << "Произведение: " << product << endl << endl;

    const char* text = "Hello World!";
    int vowels, consonants;

    countVowelsAndConsonants(text, &vowels, &consonants);
    cout << "Текст: \"" << text << "\"" << endl;
    cout << "Гласных: " << vowels << endl;
    cout << "Согласных: " << consonants << endl << endl;

    int arr[] = { 3, 8, 1, 9, 4, 6, 2, 7, 5 };
    int size = sizeof(arr) / sizeof(arr[0]);
    int minVal, maxVal;

    findMinMax(arr, size, &minVal, &maxVal);

    cout << "Массив: ";
    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    cout << "Минимальный элемент: " << minVal << endl;
    cout << "Максимальный элемент: " << maxVal << endl;

    return 0;
}