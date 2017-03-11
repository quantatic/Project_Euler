//gcc 5.4.0

#include  <stdio.h>

int main(void)
{
    int max = 0;
    int maxLength = 0;
    for(int i = 1; i < 1000000; i++){
        long testing = i;
        int length = 0;
        //printf("%d\n", i);
        while(testing > 1){
            length++;
            if(testing % 2 == 0){
                testing /= 2;
            }else{
                testing = 3 * testing + 1;
            }
        }
        if(length > maxLength){
            maxLength = length;
            max = i;
        }
    }
    printf("The number that produces the longest chain is %d with a chain length of %d\n", max, maxLength);
	return 0;
}
