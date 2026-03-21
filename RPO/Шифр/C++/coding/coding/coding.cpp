#include <iostream>
#include <string>

using namespace std;

bool isAlpha(char ch) {
    return (ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z');
}

bool isLower(char ch) {
    return ch >= 'a' && ch <= 'z';
}

string code(string line, int delta) {
    string result;

    for (char ch : line) {
        if (isAlpha(ch)) {
            char base = isLower(ch) ? 'a' : 'A';
            result += (ch - base - delta + 26) % 26 + base;
        }
        else {
            result += ch;
        }
    }

    return result;
}

string decode(const string& line, int delta) {
    return code(line, -delta);
}

int main() {
    string alfa = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    cout << "Alphabet: " << alfa << endl;

    int delta;
    cout << "Enter delta: ";
    cin >> delta;

    string line = "Hellow world!";
    string coded = code(line, delta);
    string decoded = decode(coded, delta);

    cout << "Original: " << line << endl;
    cout << "Coded: " << coded << endl;
    cout << "Decoded: " << decoded << endl;

    return 0;
}