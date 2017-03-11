#include <stdio.h>
#include <time.h>

int main(){
	clock_t start = clock();
	int sum = 0;
	for(int i = 0; i < 1000; i++){
		if(i % 3 == 0 || i % 5 == 0){
			sum += i;
		}
	}

	printf("%d\n", sum);
	printf("%.6f seconds to execute\n", (double)(clock() - start) / CLOCKS_PER_SEC);
}
