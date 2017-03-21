#include <ctime>
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>
using namespace std;
const int size = 20;
const int n = 50;
int main()
{
    srand(time(NULL));
    string fname = "dataset\\dataset";
    for (int i = 1; i <= size; ++i)
    {
        char tmp[3];
        _itoa(i, tmp, 10);
        string t = fname + string(tmp) + string(".txt");
        ofstream fout(t.c_str());
        for (int j = 0; j < n; ++j) fout << rand() % 100 << '\n';
        fout.close();
    }
}
