//
//  B.cpp
//  
//
//  Created by SS D on 2017-10-22.
//

#include <iostream>
#include <cmath>

using namespace std;

int main(){
    int T;
    cin >> T;
    for (int cntT = 0; cntT < T; ++cntT) {
        int N;
        cin >> N;
        double * X = new double[N];
        double * Y = new double[N];
        double * W = new double[N];
        
        for (int cnt = 0; cnt < N; ++cnt){
            cin >> X[cnt];
            cin >> Y[cnt];
            cin >> W[cnt];
        }
        double mini = 100000000000;
        for (int i = 0; i < N; ++i) {
            double s = 0;
            
            for (int j = 0; j < N; j++){
                s += W[j] * (( fabs(X[i] - X[j]) > fabs(Y[i] - Y[j]) )? fabs(X[i] - X[j]) : fabs(Y[i] - Y[j]) );
            }
            if (s < mini){
                mini = s;
            }
        }
        cout << "Case #" << (cntT + 1) << ": " << mini << endl;
    }
    return 0;
}
