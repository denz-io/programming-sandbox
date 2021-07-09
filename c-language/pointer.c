#include <stdio.h>
void printArray(int *numPtr, int);
int theResult(int *numPtr, int);

int main(void){
    //declaration, initializations, and identifier
    int numbers[10];
    int *numPtr = numbers;
    int SIZE = 0, i = 0, result;

    do{
        printf("How many array do you want to store(1-10)?: ");
        scanf("%d", &SIZE);
    }while(SIZE > 10 || SIZE < 1);

    while(i < SIZE){
        printf("Enter number[%d]: ", i+1);
        scanf("%d", &numbers[i]);
        i++;
    }

    printf("%s%*s\n", "Test Case", 20, "Result"); //printing the table header
    printArray(numbers, SIZE); //funcation call
    result = theResult(numbers, SIZE); //assigning the value of the identifier with the return value of the function being called

    if (result == 1){
        printf("%*s", 15, "TRUE");
    }
    else{
        printf("%*s", 15, "FALSE");
    }

}

void printArray(int *numPtr, int SIZE){
    printf("[");
    int i;
    for (i=0; i<SIZE; i++){
        if (i!=SIZE-1){
            printf("%d,", numPtr[i]);
        }
        else{
            printf("%d]\t", numPtr[i]);
        }
    }
}

int theResult(int *numPtr, int SIZE){
    int count=0, i;
    for (i = 0; i < SIZE; i++){
        if (numPtr[i] == 3){
            count++;
            if (numPtr[i+1] == 3){
                return 0;
            }
        }
    }
    if (count == 3){
        return 1;
    }
    else{
        return 0;
    }
}
