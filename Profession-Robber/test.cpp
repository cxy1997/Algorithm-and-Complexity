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
    if (!fin)  //�ļ��򿪴����쳣����
	{
		cout << "�޷����ļ�: "<< finname <<"\n";
		return;
	}
	cout << "�Ѵ��ļ���" << finname << '\n';
	ofstream fout(foutname);
    int *v = new int[n + 1];
    v[0] = 0;
    for (int i = 1; i <= n; ++i) fin >> v[i];
    fin.close();
    //int dfs_res = dfs(v, n); // dfs ���Ӷ�̫�� ֻ�ܽ���С���ݲ���
    int dp_res = dp(v, n);
    //fout << "��׼��Ϊ\t" << dfs_res << '\n';
    fout << "DP�㷨��Ϊ\t" << dp_res << '\n';
	cout << "���Խ����д��" << foutname << /*",��׼��Ϊ " << dfs_res << */", DP�㷨��Ϊ " << dp_res /*<< ", DP�㷨"*/;/*
	if (dp_res == dfs_res)
	{
	    cout << "��ȷ!\n";
	    fout << "��ȷ!";
    } else
    {
        cout << "����!\n";
        fout << "����!";
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
	if ((lfDir = _findfirst(dir, &fileDir)) == -1l)  //�쳣�����Ҳ����ļ�
	{
		cout << "���ݼ�Ϊ�գ�\n";
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
