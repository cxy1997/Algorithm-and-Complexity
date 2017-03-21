#include <iostream>
#include <fstream>
#include <cstring>
#include <io.h>
#include "dp.h"
#include "dfs.h"
using namespace std;
const int n = 50;
void test(const char* finname, const char* foutname)
{
    ifstream fin(finname);
    if (!fin)  //文件打开错误异常处理
	{
		cout << "无法打开文件: "<< finname <<"\n";
		return;
	}
	cout << "已打开文件：" << finname << '\n';
	ofstream fout(foutname);
    int *v = new int[n + 1];
    v[0] = 0;
    for (int i = 1; i <= n; ++i) fin >> v[i];
    fin.close();
    //int dfs_res = dfs(v, n); // dfs 复杂度太高 只能进行小数据测试
    int dp_res = dp(v, n);
    //fout << "标准答案为\t" << dfs_res << '\n';
    fout << "DP算法答案为\t" << dp_res << '\n';
	cout << "测试结果已写入" << foutname << /*",标准答案为 " << dfs_res << */", DP算法答案为 " << dp_res /*<< ", DP算法"*/;/*
	if (dp_res == dfs_res)
	{
	    cout << "正确!\n";
	    fout << "正确!";
    } else
    {
        cout << "错误!\n";
        fout << "错误!";
    }*/
    cout<<'\n';
	delete [] v;
    fout.close();
}
int main()
{
    char dir[16] = "dataset\\*.txt", finname[64] = "dataset\\", foutname[64] = "result\\";
    _finddata_t fileDir;
	long lfDir;
	if ((lfDir = _findfirst(dir, &fileDir)) == -1l)  //异常处理：找不到文件
	{
		cout << "数据集为空！\n";
		cin.get();
		return 1;
	}
	else do
    {
        strcpy(finname + 8, fileDir.name);
        strcpy(foutname + 7, fileDir.name);
        test(finname, foutname);
    } while (_findnext(lfDir, &fileDir) == 0);
	_findclose(lfDir);
	cin.get();
	return 0;
}
