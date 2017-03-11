#include <stdio.h>
#include <string.h>

int main(){
	int size = 400;
	int exp = 1000;
	int num[size];
	int sum = 0;
	memset(num, 0, sizeof(num)); //zero the array
	num[size - 1] = 1; //start at one because 2^1 is 2
	for(int i = 0; i < exp; i++){
		for(int idx = 0; idx < size; idx++){
			int tmp = num[idx] * 2;
			if(tmp >= 10){
				num[idx] = tmp % 10;
				num[idx - 1]++;
			}else{
				num[idx] = tmp;
			}
		}
	}
	for(int i = 0; i < size; i++){
		printf("%d", num[i]);
		sum += num[i];
	}
	printf("\nThe sum of all digits in 2^1000 is %d\n", sum);
}
