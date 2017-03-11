#include <stdio.h>
#include <time.h>
#include <math.h>

int sumDivisors(int input);
int result;

int main(){
  int abundant[6965] = {};
  int nonAbundant[28124] = {};
  int idx = 0;
  int sum = 0;
  clock_t start = clock();
  for(int i = 2; i < 28124; i++){ //this only works for numbers greater than 1
    if(sumDivisors(i) > i){
      abundant[idx] = i;
      idx++;
    }
  }

  for(int i = 0; i < sizeof(abundant) / sizeof(int); i++){
    for(int j = i; j < sizeof(abundant) / sizeof(int); j++){
      if(abundant[i] + abundant[j] < sizeof(nonAbundant) / sizeof(int)){
        nonAbundant[abundant[i] + abundant[j]] = 1;
      }else{
        break;
      }
    }
  }

  for(int i = 0; i < sizeof(nonAbundant) / sizeof(int); i++){
    if(!nonAbundant[i]){
      sum += i;
    }
  }

  printf("Your sum is: %d\n",  sum);
  printf("Executes in %.3fms\n", (double)(clock() - start) / CLOCKS_PER_SEC * 1000);

}

int sumDivisors(int input){
  result = 1;
  for(int i = 2; i < sqrt(input); i++){
    if(input % i == 0){
      result += i;
      result += input / i;
    }
  }
  if(sqrt(input) == (int)sqrt(input)){
    result += sqrt(input);
  }
  return result;
}
