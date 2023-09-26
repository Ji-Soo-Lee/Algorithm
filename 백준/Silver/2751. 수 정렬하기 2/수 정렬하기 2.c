#include<stdio.h>
#include<stdlib.h> // for qsort
#define MAX 1000000

int compare(int *a, int*b);

int main(void) {
int n, i;
int arr[MAX] = {0};

scanf("%d", &n);

for (i = 0; i < n; i++) {
    scanf("%d", &arr[i]);
}

qsort(arr, n, sizeof(int), (int(*)(const void *, const void*)) compare);

for (i = 0; i < n; i++) {
    printf("%d\n", arr[i]);
}

return 0;
}

int compare(int *a, int*b) {
    return *a - *b; // ascending
    // return *b - *a; // descending
}
