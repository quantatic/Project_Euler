#include <math.h>
#include <stdio.h>


int main(){
	for(int a = 1; a < 1000; a++){
		for(int b = 1; b < 1000; b++){
			int c = sqrt(a * a + b * b);
			if(a * a + b * b == c * c && a + b + c == 1000){
				printf("The answer is: %d\n", a * b * c);
				return 0;
			}
		}
	}
	return 0;
}
