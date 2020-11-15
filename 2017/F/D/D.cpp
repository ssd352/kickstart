#include <iostream>

using namespace std;

int main(){
    // cake_array = [0, 1] + [0] * (10000 - 1)
    int cake_array[10000 + 1];
    for (int cnt = 2; cnt <= 10000; cnt++){
        cake_array[cnt] = 0;
    }
    for (int cnt = 1; cnt <= 100; cnt++)
        cake_array[cnt * cnt] = 1;
    for (int cnt = 2; cnt <= 10000; cnt++){
        if (cake_array[cnt] != 0)
            continue;
        int mini = 100000;
        for (int piece = 1; piece < cnt; piece++){
            int tmp = cake_array[piece] + cake_array[cnt - piece];
            if (mini > tmp)
                mini = tmp;
        }
        cake_array[cnt] = mini;
    }
    
    int T, N;
    cin >> T;
    for (int cnt = 0; cnt < T; cnt++){
        cin >> N;
        cout <<"Case #"<< (cnt + 1) << ": " << cake_array[N] << endl;
    }
    return 0;
}
