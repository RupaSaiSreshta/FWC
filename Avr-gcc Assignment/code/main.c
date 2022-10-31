#include <avr/io.h>
#include <stdbool.h>
#include <util/delay.h>
int main (void)
{
	bool A=0, B=1;
	bool D, X;
	
    DDRD   |= 0x0C;

    //equations
        
    D=(!A&&B) || (A&&!B);
	X=(!A&&B);
	
         	PORTD  |= (2<<D);
        	PORTD  |= (3<<X);
  
  return 0;

}
