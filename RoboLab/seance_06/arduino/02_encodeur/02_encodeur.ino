volatile long count=0; volatile byte prevAB=0; volatile bool bad=false;
const int8_t table[16]={0,1,-1,0,-1,0,0,1,1,0,0,-1,0,-1,1,0};
byte ab(){return (digitalRead(2)<<1)|digitalRead(3);}
void tick(){byte next=ab();if((prevAB^next)==3)bad=true;count+=table[(prevAB<<2)|next];prevAB=next;}
void initEncoder(){pinMode(2,INPUT_PULLUP);pinMode(3,INPUT_PULLUP);prevAB=ab();attachInterrupt(digitalPinToInterrupt(2),tick,CHANGE);attachInterrupt(digitalPinToInterrupt(3),tick,CHANGE);}
long readCount(){noInterrupts();long n=count;interrupts();return n;}
void setup(){Serial.begin(115200);initEncoder();}
void loop(){static unsigned long last=0;unsigned long now=micros();if(now-last>=10000){last=now;Serial.print(now);Serial.print(',');Serial.println(readCount());}}
