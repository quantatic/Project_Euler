#include <stdio.h>
#include <math.h>



int main(){
	long int start = 600851475143, max = 0, running = 1;
	for(int i = 2; i < start; i++){
		if(start % i == 0){
			printf("%d\n", i);
			start /= i;
			if(i > max){
				max = i;
			}	
			i--;
		}
	}
	printf("Max: %d\n", start);
}
