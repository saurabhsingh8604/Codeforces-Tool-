#include<bits/stdc++.h>
using namespace std;

int main(){
  //running the python script for testcase extraction
  system("python web.py");
  
  #ifndef ONLINE_JUDGE 
  freopen("input1.txt", "r",stdin);//r=read
  freopen("output1.txt","a",stdout);//a= append
  #endif
  int t;
  cin>> t;
  cout<< t<<"\n";
  for(int i =0 ;i < t; i++){
    int x, y, z;
    cin>> x>> y>> z;
    cout<< x<< " "<< y<< " "<< z<<"\n";
  }
  
  return 0;
}