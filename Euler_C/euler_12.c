#include <stdio.h>
#include <limits.h>
#include <math.h>

int divisors(long input);

int main(){
	long total = 0;
	for(int i = 1; i < 100000; i++){
		total += i;
		if(divisors(total) > 500){
			printf("Your answer is: %ld, with %d divisors\n", total, divisors(total));
			return 0;
		}	
	}
	return 0;
}

int divisors(long input){
	int tot = 0;
	for(int i = 1; i < ceil(sqrt(input)); i++){
		if(input % i == 0){
			tot += 2;
		}
	}
	return tot;
}

/*
1, 0, 1
3, 2, 2
6, 4, 3
10, 4, 4
15, 4, 5
21, 4, 6
28, 6, 7
36, 8, 8
45, 6, 9
*/



