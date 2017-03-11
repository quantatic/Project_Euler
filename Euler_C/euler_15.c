#include <stdio.h>

int main(){
	int size = 20; //2x2 grid, 3x3 positions
	long grid[(size + 1)][(size + 1)]; //access as [x][y]
	grid[size][size] = 1;
	for(int i = size; i >= 0; i--){ //x
		for(int j = size; j >= 0; j--){ //y
			long down = i == size && j == size ? 1 : 0; //make sure the first square stays at 1
			long right = 0;
			if(j < size){
				down = grid[i][j + 1];
			}
			if(i < size){
				right = grid[i + 1][j];
			}
			grid[i][j] = down + right;
		}
	}
	printf("Ways to traverse a %dx%d grid are %ld\n", size, size, grid[0][0]);
}
