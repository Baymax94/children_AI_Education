#include <Servo.h>    // 声明调用Servo.h库
Servo myservo;        // 创建一个舵机对象
Servo myservo1;        // 创建一个舵机对象
int posx = 60;          // 变量pos用来存储舵机位置
int posy = 60;          // 变量pos用来存储舵机位置
int c = 0;
void setup() { 
  Serial.begin(9600);
    myservo.attach(9);  // 将引脚9上的舵机与声明的舵机对象连接起来
    myservo1.attach(8);  // 将引脚9上的舵机与声明的舵机对象连接起来
    myservo.write(posx); 
    myservo1.write(posy);// 给舵机写入角度
} 

void loop() {
  while(Serial.available()>0)//当有信号的时候
  {
    char val=Serial.read();
    Serial.println(val);
     if(val=='0'){ 
    //左上
    if(posx -3>=0){
      posx = posx -3;
          c = 1;
    }
    if(posy -2>=0){
      posy = posy -2;
          c = 1;
    } 
   }else if(val=='1'){
    //右上
    if(posx +3<=120){
      posx = posx +3;
          c = 1;
    }
    if(posy -2>=0){
      posy = posy -2;
          c = 1;
    } 
   }else if(val=='2'){
    //左下
    if(posx -3>=0){
      posx = posx -3;
          c = 1;
    }
    if(posy +2<=120){
      posy = posy +2;
          c = 1;
    } 
   }else if(val=='3'){
    //右下
    if(posx +3<=120){
      posx = posx +3;
          c = 1;
    }
    if(posy +2<=120){
      posy = posy +2;
          c = 1;
    } 
   }else if(val=='4'){
    //上
    if(posy -2>=0){
      posy = posy -2;
          c = 1;
    } 
   }else if(val=='5'){
    //左
    if(posx -3>=0){
      posx = posx -3;
          c = 1;
    }
   }else if(val=='6'){
    //右
    if(posx +3<=120){
      posx = posx +3;
          c = 1;
    } 
   }else if(val=='7'){
    //下
    if(posy +2<=120){
      posy = posy +2;
          c = 1;
    } 
   }
   if(c ==1){
    Serial.println("dong");
    myservo.write(posx); 
    myservo1.write(posy);// 给舵机写入角度   
   }
  c = 0;
   Serial.println(posx);
   Serial.println(val);
  }
 
}    
