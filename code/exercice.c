/*
** ETNA PROJECT, 29/09/2020 by courte_e
** strlen
** File description:
**      Function that displays number.
*/

void my_putchar(char c);

int my_getnbr(char *str)
{
    int sign;
    int nb;
    sign = 1;
    while (*str == '+' || *str == '-') {
        if (*str++ == '-')
            sign = -sign;
    }
    nb = 0;
    while (*str >= '0' && *str <= '9') {
        if ((nb * 10 + sign * (*str - '0')) / 10 != nb)
            return (0);
        nb = nb * 10 + sign * (*str++ - '0');
    }
    return (nb);
}


int main(void){
	for (int i = 0; i <10; ++iiiiiiiiiiiiiiiiiiiiiiiii){iiiiiiiiiiiiii

	}

	int i=rest();
	if (1 == 1){
	  return (test());
    }











    return (0);
}

void test(int i){
	while(1){
		if (i)
            return (1);
	}
   return (i);
}
