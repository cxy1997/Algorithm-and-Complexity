#include "max.h"
int maxsum = 0;
int *stack;
void DFS(int* v, int SP, int n);
int dfs(int* v, int n)
{
    stack = new int[n + 1];
    stack[0] = 0;
    DFS(v, 1, n);
    delete [] stack;
    return maxsum;
}
void DFS(int* v, int SP, int n)
{
    if (SP == n + 1)
    {
        int sum = 0;
        for (int i = 1; i <= n; ++i) sum += stack[i] * v[i];
        maxsum = max(maxsum, sum);
    } else if (SP == n)
    {
        if (stack[1] == 0 && stack[SP - 1] == 0)
        {
            stack[SP] = 1;
            DFS(v, SP + 1, n);
        }
        stack[SP] = 0;
        DFS(v, SP + 1, n);
    } else
    {
        if (stack[SP - 1] == 0)
        {
            stack[SP] = 1;
            DFS(v, SP + 1, n);
        }
        stack[SP] = 0;
        DFS(v, SP + 1, n);
    }
}
