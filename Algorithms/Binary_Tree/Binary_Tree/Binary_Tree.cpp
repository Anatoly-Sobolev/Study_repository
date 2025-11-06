#include <iostream>
using namespace std;

struct Node {
    int value;
    Node* left;
    Node* right;
};

//Получает число узлов, и строит бинарное дерево с нужным числом узлов.
// Возвращает родительский узел
//level - это значение поля value = уровню узла (0, 1, 2...)
Node* buildPerfectlyBalancedTree(int num_nodes, int level) {
    if (num_nodes == 0) {
        return nullptr;
    }


    Node* newNode = new Node;
    newNode->value = level;
    newNode->left = nullptr;
    newNode->right = nullptr;


    int left_subtree_nodes = (num_nodes - 1) / 2;
    int right_subtree_nodes = (num_nodes - 1) - left_subtree_nodes;


    newNode->left = buildPerfectlyBalancedTree(left_subtree_nodes, level + 1);

    newNode->right = buildPerfectlyBalancedTree(right_subtree_nodes, level + 1);

    return newNode;
}

// Меняет местами все правые и левые узлы
void swapChildren(Node* node) {
    if (node == nullptr) {
        return;
    }


    if (node->left != nullptr || node->right != nullptr) {
        Node* temp = node->left;
        node->left = node->right;
        node->right = temp;
    }


    swapChildren(node->left);
    swapChildren(node->right);
}

//Выводит на экран бинарное дерево
void printTree(Node* node, int depth) {
    if (node == nullptr) {
        
        return;
    }


    for (int i = 0; i < depth; ++i) {
        cout << " ____";
    }
    cout << node->value << endl;


    printTree(node->left, depth + 1);
    printTree(node->right, depth + 1);
}

// Удаляет дерево
void freeTree(Node* node) {
    if (node == nullptr) {
        return;
    }
    freeTree(node->left);
    freeTree(node->right);

    delete node;
}


int main() {
    setlocale(LC_ALL, "rus");
    int N;
    cout << "Введите количество вершин N для дерева: ";
    cin >> N;

    if (N < 1) {
        cout << "Количество вершин должно быть не меньше 1." << endl;
        return 1;
    }


    Node* root = buildPerfectlyBalancedTree(N, 0);

    cout << "\nДерево до обмена дочерних вершин:" << endl;
    printTree(root, 0);

    swapChildren(root);

    cout << "\nДерево после обмена дочерних вершин:" << endl;
    printTree(root, 0);


    freeTree(root);

    return 0;
}