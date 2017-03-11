//used https://www.cs.cmu.edu/~adamchik/15-121/lectures/Sorting%20Algorithms/sorting.html for sorting algorithm (used bubble sort)

#include <stdio.h>
#include <string.h>
#include <time.h>

int main(){
  clock_t start = clock();
  int sum = 0;
  FILE * input = fopen("/home/quantatic/Desktop/C/euler/p022_names.txt", "r");
  char c;
  char names[5163][12] = {}; //calculated that the maximum names size is 13 (12 + 1) through some simple tests, and calculated that there are 5163 names through similar means
  char tmp[sizeof(names[0]) / sizeof(char)];


    for(int i = 0; i < sizeof(names) / sizeof(sizeof(names[0])); i++){
      for(int j = 0; (c = fgetc(input)) != ',' && c != EOF; j++){
        if(c == '\"'){ //move back one to avoid throwing the index off
          j--;
        }else{
          names[i][j] = c; //if not quotes, add it to the string
        }
      }
    }

    int keepGoing = 1; //one replaces a boolean true in C
    while(keepGoing){
      keepGoing = 0;
      for(int i = 0; i < sizeof(names) / sizeof(names[0]) - 1; i++){ //bubble sort baby!
        if(strcmp(names[i], names[i + 1]) > 0){
          keepGoing = 1; //if we make any changes, now we can't exit
          memcpy(tmp, names[i], sizeof(names[i])); //switch the two strings, using an intermediary temporary variable
          memcpy(names[i], names[i + 1], sizeof(names[i + 1]));
          memcpy(names[i + 1], tmp, sizeof(tmp));
        }
      }
    }

    for(int i = 0; i < sizeof(names) / sizeof(names[0]); i++){
      for(int j = 0; names[i][j] != '\0'; j++){
        sum += (names[i][j] % 32) * (i + 1); //we mod it by 32 in order to convert it from character to alphabetical number
      }
    }

    printf("The sum using the formula given is: %d\n", sum);
    printf("Executes in %.6fs\n", (double)(clock() - start) / CLOCKS_PER_SEC);
  }
