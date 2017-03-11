#include <stdio.h>
#include <math.h>

int isPrime(int input);

int main(){
	long sum = 0;
	for(int i = 2; i < 2000000; i++){
		if(isPrime(i)){
			sum += i;
			//printf("%d\n", i);
		}
	}
	printf("Your answer is: %ld\n", sum);
}

int isPrime(int input){
	for(int i = 2; i < (int)sqrt(input) + 1; i++){
		if(input % i == 0){
			return 0;
		}
	}
	return 1;
}
