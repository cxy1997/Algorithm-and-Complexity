#include "max.h"
int DP(int* v, int n);
int dp(int* v, int n)
{
    int res1 = DP(v, n - 1);
    v[1] = 0;
    int res2 = DP(v, n);
    return max(res1, res2);
}
int DP(int* v, int n)
{
    int res[3] = {0, v[1], 0};
    for (int i = 2; i <= n; ++i) res[i%3] = max(v[i] + res[(i - 2) % 3], res[(i - 1) % 3]);
    return res[n % 3];
}
