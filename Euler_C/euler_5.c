#include <stdio.h>

int solves(int input);

int main(){
	int cur = 2;
	while(1){
		if(solves(cur)){
			printf("%d\n", cur);
			break;
		}
		cur += 2;
	}
	
}

int solves(int input){
	for(int i = 1; i <= 20; i++){
		if(!(input % i == 0)){
			return 0;
		}
	}
	return 1;
}
