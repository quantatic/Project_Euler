#include <stdio.h>

int isPrime(int input);
int main(){

	int primes[10001];
	int counter = 0;
	for(int i = 2; i < 2147483647; i++){
		if(isPrime(i)){
			primes[counter] = i;
			counter++;
		}
		if(counter > 10001){
			printf("%d\n", primes[10000]);
			return 0;
		}
	}
	return 0;
}

int isPrime(int input){
	for(int i = 2; i < input; i++){
		if(input % i == 0){
			return 0;
		}
	}
	return 1;
}
