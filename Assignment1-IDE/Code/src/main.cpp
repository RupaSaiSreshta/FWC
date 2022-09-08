#include <Arduino.h>
int A=1, B=0;
int D, X;
void disp_BHS(int D, int X)
{
	digitalWrite(2,D);
        digitalWrite(3,X);
}
	void setup()
{
	pinMode(2, OUTPUT);
pinMode(3,OUTPUT);
}
void loop()
{ 
	D=(!A&&B) || (A&&!B);
	X=(!A&&B);
	disp_BHS (D,X);
}
