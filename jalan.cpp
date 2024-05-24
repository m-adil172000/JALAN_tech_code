#include <bits/stdc++.h>
using namespace std;

/*
Time complexity:  O(n)
Space complexity: O(n)
*/

void alternate(vector<int>&arr){
    int n = arr.size();
    vector<int> check(n);
    int f=0,b=n-1;
    for(int i=0; i<n; i++){
        if(arr[i]<0){
            check[f]=arr[i];
            f++;
        }
        else{
            check[b]=arr[i];
            b--;
        }
    }

    int i=0;
    while(b>=0 && f<n){
        if(i%2==0){
            arr[i]=check[b];
            b--;
        }
        else{
            arr[i]=check[f];
            f++;
        }
        i++;
    }
    while(b>=0){
        arr[i]=check[b];
        b--;
        i++;
    }
    while(f<n){
        arr[i]=check[f];
        f++;
        i++;
    }
    
}


int main(){
    
    int n;
    cout<<"Enter array size"<<endl;
    cin>>n;
    vector<int>arr(n);

    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    for(int i=0;i<n;i++){
        cout<<arr[i]<<" ";
    }

    cout<<endl;
    alternate(arr);  
    for(int i=0;i<n;i++){
        cout<<arr[i]<<" ";
    }

}
