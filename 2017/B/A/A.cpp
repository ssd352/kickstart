//
//  A.cpp
//  
//
//  Created by SS D on 2017-10-22.
//

#include <iostream>

using namespace std;

int main(){
    int T;
    long modulo = 1000000007;
    cin >> T;
    for (int cntT = 0; cntT < T; ++cntT) {
        int n;
        cin >> n;
        int * k = new int[n];
        long * m2 = new long[n];
        long a = 1;
        for (int cnt = 0; cnt < n; ++cnt) {
            cin >> k[cnt];
            m2[cnt] = a;
            a *= 2;
            a %= modulo;
        }
        long s = 0;
        for (int i = 0; i < n - 1; ++i) {
            for (int j = i + 1; j < n; j++) {
                s += m2[j - i - 1] * (k[j] - k[i]);
                s %= modulo;
            }
        }
        cout << "Case #" << (cntT + 1) << ": " << s << endl;
    }
    return 0;
}
