void setup(){Serial.begin(115200);}
void loop(){static unsigned long last=0; unsigned long now=micros(); if(now-last>=10000){last=now; Serial.print(now);Serial.print(',');Serial.println(analogRead(A0));}}
