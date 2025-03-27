#include <iostream>
#include <string>
#include <fstream>
#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
#include <cctype>

using namespace std;

int main(){
    ifstream f("kjbible.txt");

    if (!f.is_open()){
        cout << "Error opening file" << endl;
        exit(0);
    }

    string word;
    set<string> uniqueWords;

    char zero = '0' , one = '1', two = '2', three = '3', four = '4', five = '5', six = '6', seven = '7', eight = '8', nine = '9';
    char com = ',', op = '(', cp = ')', ob = '[', cb = ']', col = ':', p = '.', sc = ';', qm = '?', em = '!' ;



    while (f >> word){
        word.erase(remove(word.begin(), word.end(), zero), word.end());
        word.erase(remove(word.begin(), word.end(), one), word.end());
        word.erase(remove(word.begin(), word.end(), two), word.end());
        word.erase(remove(word.begin(), word.end(), three), word.end());
        word.erase(remove(word.begin(), word.end(), four), word.end());
        word.erase(remove(word.begin(), word.end(), five), word.end());
        word.erase(remove(word.begin(), word.end(), six), word.end());
        word.erase(remove(word.begin(), word.end(), seven), word.end());
        word.erase(remove(word.begin(), word.end(), eight), word.end());
        word.erase(remove(word.begin(), word.end(), nine), word.end());
        word.erase(remove(word.begin(), word.end(), com), word.end());
        word.erase(remove(word.begin(), word.end(), op), word.end());
        word.erase(remove(word.begin(), word.end(), cp), word.end());
        word.erase(remove(word.begin(), word.end(), ob), word.end());
        word.erase(remove(word.begin(), word.end(), cb), word.end());
        word.erase(remove(word.begin(), word.end(), col), word.end());
        word.erase(remove(word.begin(), word.end(), p), word.end());
        word.erase(remove(word.begin(), word.end(), sc), word.end());
        word.erase(remove(word.begin(), word.end(), qm), word.end());
        word.erase(remove(word.begin(), word.end(), em), word.end());
        for(char &c : word){
            c = tolower(c);
        }
        uniqueWords.insert(word);
    }

    ofstream output("kjbibleUNIQUE.txt");

    if(output.is_open()){
        for(const string& element : uniqueWords){
            output << element << endl;
        }
        output.close();
        cout << "You should now have a file of all unqiue words in the bible" << endl;
    } else {
        cout << "error creating the output file" << endl;
        exit(0);
    }

    return 0;
}