#include <stdio.h>

int main(){
	int a = 1, b = 1, tmp, sum = 0;
	while(b < 4000000){
		if(b % 2 == 0){
			sum += b;
		}
		printf("%d\n", b);
		tmp = a + b;
		a = b;
		b = tmp;
	}
	printf("Sum: %d\n", sum);
}
