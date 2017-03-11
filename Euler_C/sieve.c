/***************************************
* Alternate way to do Project Euler 10 *
***************************************/

#include <stdio.h>

void fill(int fillable[], int size, int fill);

int main(){
	static int sieve[2000000] = {};
	long sum = 0;
	int size = sizeof(sieve) / sizeof(sieve[0]);
	fill(sieve, size, 1);
	sieve[0] = 0;
	sieve[1] = 0;

	for(int i = 2; i < size; i++){
		for(int j = i * 2; j < size; j += i){
			sieve[j] = 0;
		}
	}
	for(int i = 0; i < size; i++){
		if(sieve[i]){
			//printf("%d\n", i);
			sum += i;
		}
	}
	printf("Your answer is: %ld\n", sum);
}

void fill(int fillable[], int size, int fill){
	for(int i = 0; i < size; i++){
		fillable[i] = fill;
	}
}
