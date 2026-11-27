#define ALLOW_PID 1
#include <stdlib.h>
#include <string.h>
#include <math.h>
volatile long count=0; volatile byte prevAB=0; volatile bool bad=false;
const int8_t table[16]={0,1,-1,0,-1,0,0,1,1,0,0,-1,0,-1,1,0};
byte ab(){return (digitalRead(2)<<1)|digitalRead(3);}
void tick(){byte next=ab();if((prevAB^next)==3)bad=true;count+=table[(prevAB<<2)|next];prevAB=next;}
void initEncoder(){pinMode(2,INPUT_PULLUP);pinMode(3,INPUT_PULLUP);prevAB=ab();attachInterrupt(digitalPinToInterrupt(2),tick,CHANGE);attachInterrupt(digitalPinToInterrupt(3),tick,CHANGE);}
long readCount(){noInterrupts();long n=count;interrupts();return n;}

const byte STBY=6, IN1=7, IN2=8, PWM=9;
bool configured=false, active=false, pid=false, modeSet=false, gainsSet=false, targetSet=false;
float cpr=0, limitAngle=0, ref=0,kp=0,ki=0,kd=0,integ=0,wf=0,oldq=0;
int signEnc=1, ceiling=0, openPwm=0, applied=0; long origin=0;
unsigned long last=0, started=0, heartbeat=0; byte cycles=0;
char buf[100]; byte len=0; bool overflow=false;
void halt(){digitalWrite(STBY,LOW);analogWrite(PWM,0);digitalWrite(IN1,LOW);digitalWrite(IN2,LOW);active=false;integ=0;applied=0;}
void drive(int p){p=constrain(p,-ceiling,ceiling);if((p>0)!=(applied>0))analogWrite(PWM,0);digitalWrite(IN1,p>0);digitalWrite(IN2,p<0);analogWrite(PWM,abs(p));applied=p;}
bool number(char* s,float &v){if(!s||!*s)return false;char* end;v=strtod(s,&end);return *end==0&&isfinite(v);}
void command(char* s){
 if(!strcmp(s,"STOP")){halt();Serial.println(F("#ACK STOP"));return;}
 if(!strcmp(s,"KEEP")){heartbeat=micros();return;}
 if(active){halt();Serial.println(F("#ERR active"));return;}
 char* cmd=strtok(s,",");if(!cmd)return;
 float a,b,c,d; bool ok=false;
 if(!strcmp(cmd,"CONFIG")){
  configured=false;modeSet=false;gainsSet=false;targetSet=false;
  if(number(strtok(NULL,","),a)&&number(strtok(NULL,","),b)&&number(strtok(NULL,","),c)&&number(strtok(NULL,","),d)&&!strtok(NULL,",")&&a>=1&&a<=1000000&&(b==1||b==-1)&&c>=1&&c<=100&&c==floor(c)&&d>0&&d<=PI){cpr=a;signEnc=b;ceiling=c;limitAngle=d;origin=readCount();noInterrupts();bad=false;interrupts();configured=true;openPwm=0;ref=0;ok=true;}
 }else if(!strcmp(cmd,"MODE")){char* m=strtok(NULL,",");if(m&&!strtok(NULL,",")&&(!strcmp(m,"OPEN")||(ALLOW_PID&&!strcmp(m,"PID")))){pid=!strcmp(m,"PID");modeSet=true;ok=true;}}
 else if(!strcmp(cmd,"PWM")&&configured&&number(strtok(NULL,","),a)&&!strtok(NULL,",")&&fabs(a)<=ceiling&&a==floor(a)){openPwm=a;ok=true;}
 else if(!strcmp(cmd,"SETPOINT")&&configured&&number(strtok(NULL,","),a)&&!strtok(NULL,",")&&fabs(a)<limitAngle*.8){ref=a;targetSet=true;ok=true;}
 else if(!strcmp(cmd,"GAINS")&&number(strtok(NULL,","),a)&&number(strtok(NULL,","),b)&&number(strtok(NULL,","),c)&&!strtok(NULL,",")&&a>0&&a<=10&&b>=0&&b<=10&&c>=0&&c<=10){kp=a;ki=b;kd=c;gainsSet=true;ok=true;}
 else if(!strcmp(cmd,"START")&&!strtok(NULL,",")&&configured&&modeSet&&(!pid||(gainsSet&&targetSet))){float q=signEnc*(readCount()-origin)*2*PI/cpr;if(fabs(q)<limitAngle*.8&&!bad){oldq=q;wf=0;integ=0;started=heartbeat=last=micros();active=true;digitalWrite(STBY,HIGH);ok=true;}}
 Serial.println(ok?F("#ACK"):F("#ERR"));
}
void setup(){pinMode(STBY,OUTPUT);pinMode(IN1,OUTPUT);pinMode(IN2,OUTPUT);pinMode(PWM,OUTPUT);halt();initEncoder();Serial.begin(115200);last=micros();}
void loop(){
 unsigned long now=micros();
 if(active&&(now-heartbeat>500000UL||now-started>5000000UL||bad)){halt();Serial.println(F("#FAULT timeout/encoder"));}
 for(byte i=0;i<32&&Serial.available();i++){char ch=Serial.read();if(ch=='\n'){if(!overflow){buf[len]=0;command(buf);}else halt();len=0;overflow=false;}else if(ch!='\r'){if(len<sizeof(buf)-1&&!overflow)buf[len++]=ch;else overflow=true;}}
 now=micros();unsigned long elapsed=now-last;if(elapsed<10000)return;last=now;
 if(!configured)return;
 if(active&&elapsed>20000){halt();Serial.println(F("#FAULT timing"));}
 float dt=elapsed*1e-6;long n=signEnc*(readCount()-origin);float q=n*2*PI/cpr;wf=.2*(q-oldq)/dt+.8*wf;oldq=q;float e=ref-q;
 if(active){if(fabs(q)>=limitAngle){halt();Serial.println(F("#FAULT travel"));}else if(pid){float cand=integ+e*dt;float lim=ceiling/255.;float raw=kp*e+ki*cand-kd*wf;if(!((raw>lim&&e>0)||(raw< -lim&&e<0)))integ=cand;drive(round(255*constrain(kp*e+ki*integ-kd*wf,-lim,lim)));}else drive(openPwm);}
 if(++cycles>=4){cycles=0;if(Serial.availableForWrite()>=48){Serial.print(now);Serial.print(',');Serial.print(n);Serial.print(',');Serial.print(q,6);Serial.print(',');Serial.print(wf,6);Serial.print(',');Serial.print(ref,6);Serial.print(',');Serial.print(applied);Serial.print(',');Serial.println(e,6);}}
}
