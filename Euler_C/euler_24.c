//https://en.wikipedia.org/wiki/Permutation
#include <math.h>
#include <time.h>
#include <stdio.h>
#include <string.h>

char permutationArray[3628801][11] = {};

int main(){
  clock_t startTime = clock();
  long tot = 1; //used to increment through array
  char permutations[11] = "0123456789"; //the string that we will manipulate, of size 11 for the \0 character
  int sizePermutations = sizeof(permutations) / sizeof(char) - 1; //used multiple times throughout the program
  int kIdx; //used in algorithm
  int lIdx; //see above
  while(1){
    strcpy(permutationArray[tot], permutations);
    tot++;
    kIdx = -1;
    lIdx = -1;
    for(int k = 0; k < sizePermutations; k++){
      if(permutations[k] < permutations[k + 1]){
        kIdx = k;
      }
    }
    if(kIdx == -1){ //if we can't find a K, thus we are at the end of the generation
      break;
    }
    for(int l = kIdx; l < sizePermutations; l++){
      if(permutations[kIdx] < permutations[l]){
        lIdx = l;
      }
    }
    char tmp = permutations[lIdx]; //temporary variable for switching
    permutations[lIdx] = permutations[kIdx];
    permutations[kIdx] = tmp;
    for(int i = kIdx + 1; i < ceil((sizePermutations + kIdx + 1) / 2.0); i++){ //find the maximum index that we want to use(not even a little sketchy, I promise!)
      //printf("Swapping %d and %d\n", sizeof(permutations) / sizeof(char) - i + kIdx, i);
      char tmp = permutations[i];
      permutations[i] = permutations[sizePermutations - i + kIdx];
      permutations[sizePermutations - i + kIdx] = tmp;
    }
  }
  printf("The 1 millionth term is %s!\n", permutationArray[1000000]); //we did it!
  printf("Executes in %.3fms in %ld steps\n", (double)(clock() - startTime) / CLOCKS_PER_SEC * 1000, tot - 1);
}
