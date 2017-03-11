#include <stdio.h>
#include <string.h>

int isPalindrome(int input);

int main(){
	int max = 0;
	for(int i = 1; i <= 999; i++){
		for(int j = 1; j <= 999; j++){
			if(isPalindrome(i * j)){
				printf("%d\n", i * j);
				if(i * j > max){
					max = i * j;
				}
			}
		}
	}
	printf("Max is: %d\n", max);
	return 0;
}

int isPalindrome(int input){
	int comp = 0;
	int copy = input;
	while(copy > 0){
		comp = comp * 10 + copy % 10;
		copy /= 10;
	}
	return comp == input;
}
