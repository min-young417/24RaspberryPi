#include <stdio.h>
#include <stdlib.h>
#include <wiringPi.h>
#include <unistd.h>
#include <time.h>

#define PIR_D 2
#define BUZZER 15

int main(void){
	int pir_val;
	
  	if(wiringPiSetup()==-1)  
    	return -1;
	
	pinMode(PIR_D,INPUT);
	pinMode(BUZZER,OUTPUT);
	
	for(int i=0;i<20;i++){	
    	pir_val = digitalRead(PIR_D);
		if(pir_val == 1){
			printf("PIR Detected !! \n");
            digitalWrite(BUZZER,pir_val);
        }else{
			printf("PIR Not detect !! \n");
            digitalWrite(BUZZER,pir_val);
        }
        sleep(1);
	}
	digitalWrite(BUZZER,0);

	return 0;
}