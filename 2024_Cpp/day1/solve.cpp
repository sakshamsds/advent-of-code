#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

const int N = 1000;

int main() {
    ifstream infile("input.txt");
    vector<int> a, b;
    for (int i = 0; i < N; i++) {
        int x, y;
        infile >> x >> y;
        a.push_back(x);
        b.push_back(y);
    }
    infile.close();

    sort(a.begin(), a.end());
    sort(b.begin(), b.end());

    long long sum = 0;
    for (int i = 0; i < N; i++) {
        sum += abs(a[i] - b[i]);
    }
    cout << sum << "\n";
}