#include <stdio.h>
#include <time.h>

int main(){
  clock_t start = clock();
  const int days[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
  int dayOfWeek = 1; //1 is monday, 2 is tuesday, 7 is sunday
  int total = 0;
  int leap;
  for(int year = 1900; year <= 2000; year++){
    int leap = (year % 4 == 0 && (year % 400 == 0 || !(year % 100 == 0)));
    for(int month = 1; month <= 12; month++){
      if(dayOfWeek == 7 && year > 1900){
        total++;
      }
      for(int day = 1; day <= days[month - 1] + (month == 2 && leap); day++){
        dayOfWeek = dayOfWeek == 7 ? 1 : dayOfWeek + 1; //adds one, otherwise loops around
      }
    }
  }
  printf("Amount of Sundays on the first is %ld\n", total);
  printf("Executed in: %.6f seconds.\n", (double)(clock() - start) / CLOCKS_PER_SEC);
}
