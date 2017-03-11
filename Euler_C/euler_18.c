#include <stdio.h>

int max(int a, int b);

int main(){
	FILE *fp;
	int tmp;
	fp = fopen("18", "r");
	int array[15][15] = {}; //access as [y][x]
	for(int i = 0; i < 15; i++){ //y value
		for(int j = 0; j <= i; j++){ //x value
			fscanf(fp, "%d", &tmp);
			array[i][j] = tmp;
		}
	}
	for(int i = 13; i >= 0; i--){ //y value
		for(int j = 0; j <= i; j++){ //x value
			array[i][j] += max(array[i + 1][j], array[i+1][j+1]);
		}
	}

	for(int i = 0; i < 15; i++){
		for(int j = 0; j < 15; j++){
			printf("%d ", array[i][j]);
		}
		printf("\n");
	}
}	

int max(int a, int b){
	if(a > b){
		return a;
	}else{
		return b;
	}
}	
