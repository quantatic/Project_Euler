#include <stdio.h>

int main(){
	int sum1;
	int sum2;
	for(int i = 1; i <= 100; i++){
		sum1 += i * i;
		sum2 += i;
	}
	sum2 *= sum2;
	printf("%d\n", sum2 - sum1);
}
