#include <iostream>
#include <climits>

using namespace std;

int main(){
    long apsp[100][100], exp[100][100];
    double exp1[100], expn[100];
    int T;
    cin >> T;
    for (int cntT = 0; cntT < T; cntT++) {
        int N, M, P;
        cin >> N >> M >> P;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                apsp[i][j] = 11;
            }
        }
        for (int i = 0; i < N; i++) {
            apsp[i][i] = 0;
        }
        for (int cnt = 0; cnt < M; cnt++) {
            int Ui, Vi, Di;
            cin >> Ui >> Vi >> Di;
            apsp[Ui - 1][Vi - 1] = Di;
            apsp[Vi - 1][Ui - 1] = Di;
        }
        for (int k = 0; k < N; k++) {
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    if (apsp[i][j] > apsp[i][k] + apsp[k][j]){
                        apsp[i][j] = apsp[i][k] + apsp[k][j];
                        apsp[j][i] = apsp[i][j];
                    }
                    
                }
            }
        }
        
//        for (int i = 0; i < N; i++) {
//            for (int j = 0; j < N; j++) {
//                cout << apsp[i][j] << " " ;
//            }
//            cout << endl;
//        }
        
        
        for (int cnt = 0; cnt < N; ++cnt) {
            long sum = 0;
            for (int i = 0; i < N; i++) {
                // cout << "apsp[cnt][i] " << apsp[cnt][i] << " ";
                sum += apsp[cnt][i];
            }
            // cout << "sum is " << sum << endl;
            double e = sum;
            e /= (N - 1);
            exp1[cnt] = e;
            expn[cnt] = e;
        }
        
//        for (int i = 0; i < N; i++) {
//            cout << exp1[i] << " ";
//        }
//        cout << endl;
        
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                exp[i][j] = apsp[i][j];
            }
        }
        
        for (int cnt = 1; cnt < P; cnt ++) {
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    
                    double sum = 0;
                    for (int k = 0; k < N; k++) {
                        sum += exp[k][j];
                    }
                    sum /= (N - 1);
                    exp[i][j] = sum + apsp[i][j];
                }
            }
//            double sum = 0;
//            for (int i = 0; i < N; i++) {
//                sum += exp1[i];
//            }
//            sum /= (N - 1);
//            for (int i = 0; i < N; i++) {
//                expn[i] = sum - (exp1[i] / (N - 1));
//            }
        }
        
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                cout << exp[i][j] << " ";
            }
            cout << endl;
        }
        cout << "Case #" << (cntT + 1) << ": " << exp1[0]<<endl;
    }
    return 0;
}
