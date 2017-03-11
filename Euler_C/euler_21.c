#include <stdio.h>
#include <time.h>
#include <math.h>

int sumDivisors(int input);
double mySqrt;

int main(){
  clock_t start = clock();

  int sum = 0;
  int b;
  for(int a = 2; a < 10000; a++){
    b = sumDivisors(a);
    if(a != b && a == sumDivisors(b)){
      sum += a;
    }
  }

  printf("Sum of all amicable numbers under 10000 is: %d\n", sum);
  printf("Executes in %.3fms\n", (double)(clock() - start) / CLOCKS_PER_SEC * 1000);
}

int sumDivisors(int input){
  int result = 1;
  mySqrt = sqrt(input); //create a variable to avoid having to calculate this multiple times
  for(int i = 2; i < mySqrt; i++){
    if(input % i == 0){
      result += i;
      result += input / i;
    }
  }
  if(mySqrt == (int)mySqrt){
    input += mySqrt;
  }
  return result;
}
