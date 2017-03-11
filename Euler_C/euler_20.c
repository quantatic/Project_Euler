#include <stdio.h>
#include <time.h>

int main(){
  clock_t start = clock();
  int sum = 0;
  int num[158] = {}; //we can tell we need this many digits thanks to it being ~9.33x10^157
  num[sizeof(num) / sizeof(int) - 1] = 1;
  int carry10;
  int carry100;
  for(int i = 2; i <= 100; i++){
    for(int idx = 1; idx < sizeof(num) / sizeof(int); idx++){
      if(idx == 199){
        carry10 = (num[idx] * i) / 10;
        carry100 = 0;
        num[idx] = (num[idx] * (i % 10)) % 10;
      }else{
        carry10 = ((num[idx] * (i % 10) + num[idx + 1] * (i / 10)) / 10) % 10;
        carry100 = (num[idx] * (i % 10) + num[idx + 1] * (i / 10)) / 100;
        num[idx] = (num[idx] * (i % 10) + num[idx + 1] * (i / 10)) % 10;
      }
      num[idx - 1] += carry10;

      if(num[idx - 1] > 9){ //if we have an overflow in the carry digit, simply reduce and tick up next carry digit
        carry100 += num[idx - 1] / 10;
        num[idx - 1] %= 10;
      }
      num[idx - 2] += carry100;

      if(num[idx - 2] > 9){ //if we have an overflow in the carry digit, reduce and add to the next digit(no need for another variable)
        num[idx - 3] += num[idx - 2] / 10;
        num[idx - 2] %= 10;
      }
    }
  }
  for(int i = 0; i < sizeof(num) / sizeof(int); i++){
    printf("%d", num[i]);
    sum += num[i];
  }
  printf("\nThe sum of all numbers in 100! is %d\n", sum);
  printf("Executes in %.3fms\n", (double)(clock() - start) / CLOCKS_PER_SEC * 1000);
}
