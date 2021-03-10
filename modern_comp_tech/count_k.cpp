#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

#define SIZE 1000

int k_in(const char * str, char k){
    int count = 0;
    const char * c = str + strlen(str) - 1;  // Последний символ
    while(c != str && isspace(*c)) --c;      // Проходим последние пробелы
    while(c >= str && !isspace(*c))
        if (*c-- == k) ++count;
    return count;
}

int main(){
    char str[SIZE];
    for(;;)
    {
        printf("Введите строку (ENTER для выхода): ");
        fgets(str,SIZE,stdin);
        if (strlen(str) == 1) break;
        printf ("Кол-во букв k в последнем слове - %d\n",k_in(str,'k'));
    };
} //End main