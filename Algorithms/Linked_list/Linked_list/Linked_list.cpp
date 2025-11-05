#include <iostream>
#include <string>

using namespace std;

struct Node {
    string word;
    int pages[10];
    Node* next;
};

Node* addNode(Node* head, string newWord, int newPages[]) {
    Node* newNode = new Node;
    newNode->word = newWord;
    for (int i = 0; i < 10; ++i) {
        newNode->pages[i] = newPages[i];
    }
    newNode->next = nullptr;

    if (head == nullptr) {
        return newNode;
    }
    else {
        Node* current = head;
        while (current->next != nullptr) {
            current = current->next;
        }
        current->next = newNode;
        return head;
    }
}

void displayList(Node* head) {
    if (head == nullptr) {
        cout << "The list is empty." << endl << endl << endl;
        return;
    }
    Node* current = head;
    while (current != nullptr) {
        cout << "Слово: " << current->word << endl;
        cout << "Страницы: [";
        for (int i = 0; i < 10; ++i) {
            cout << current->pages[i];
            if (i < 9) {
                cout << ", ";
            }
        }
        cout << "]" << endl;
        cout << "---------------" << endl;
        current = current->next;
    }
}

void displayPagesByWord(Node* head, string searchWord) {
    if (head == nullptr) {
        cout << "Список пуст, слово '" << searchWord << "' не найдено." << endl;
        return;
    }
    Node* current = head;
    bool found = false;
    while (current != nullptr) {
        if (current->word == searchWord) {
            cout << "Страницы для слова '" << searchWord << "': [";
            for (int i = 0; i < 10; ++i) {
                cout << current->pages[i];
                if (i < 9) {
                    cout << ", ";
                }
            }
            cout << "]" << endl;
            found = true;
            break;
        }
        current = current->next;
    }
    if (!found) {
        cout << "Слово '" << searchWord << "' не найдено в списке." << endl;
    }
}

void deleteList(Node* head) {
    Node* current = head;
    Node* nextNode;
    while (current != nullptr) {
        nextNode = current->next;
        delete current;
        current = nextNode;
    }
}

Node* make_first_nodes(void) {

    setlocale(LC_ALL, "rus");

    Node* head = nullptr;

    int pages1[] = { 1, 5, 10, 15, 20, 25, 30, 35, 40, 45 };
    head = addNode(head, "hello", pages1);

    int pages2[] = { 2, 12, 22, 32, 42, 52, 62, 72, 82, 92 };
    head = addNode(head, "cat", pages2);

    int pages3[] = { 3, 13, 23, 33, 43, 53, 63, 73, 83, 93 };
    head = addNode(head, "list", pages3);

    int pages4[] = { 3, 13, 23, 33, 43, 53, 63, 73, 83, 93 };
    head = addNode(head, "C++", pages4);


    return head;


}

int main() {
    setlocale(LC_ALL, "rus");

    string word; //For input
    int pages[10];
    Node* head = make_first_nodes();




    int input;
    input = 10;
    while (input != 0) {
        cout << "Input number please" << endl << endl;
        cout << "0 - Go out of the program" << endl;
        cout << "1 - Add a note to the link list" << endl;
        cout << "2 - Display hole link list" << endl;
        cout << "3 - Find a word in the link list" << endl;
        cout << "4 - Delite the link list" << endl;

        cin >> input;
        switch (input) {
        case 0: cout << "The program is finished" << endl; break;

        case 1: cout << "Please input a word: " << endl;
            cin >> word;
            cout << "Please input 10 pages: " << endl;
            for (int i = 0; i < 10; ++i) {
                cin >> pages[i];
            }
            head = addNode(head, word, pages);
            cout << "word: \"" << word << "\" is added " << endl << endl;
            continue;

        case 2: displayList(head);  continue;


        case 3: cout << "Please input a word: ";
            cin >> word;
            displayPagesByWord(head, word);
            continue;


        case 4: deleteList(head);
            head = nullptr;

            cout << "The list was delited" << endl;
            cout << "______________________" << endl << endl;
            continue;

        default: continue;
        }



    }

    return 0;
}