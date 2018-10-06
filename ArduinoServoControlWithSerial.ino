/* 
 by can.not.lose <not have yet>
 This example code is in the public domain.
*/

#include <Servo.h>

Servo servo1;  // create servo object to control a servo
Servo servo2;  // create servo object to control a servo
Servo servo3;  // create servo object to control a servo


// twelve servo objects can be created on most boards

int pos = 0;    // variable to store the servo position

void setup() {
  servo1.attach(8);  // attaches the servo on pin 9 to the servo object
  servo2.attach(9);  // attaches the servo on pin 9 to the servo object
  servo3.attach(10);  // attaches the servo on pin 9 to the servo object
  
    
    // initialize serial:
  Serial.begin(115200); //set serial monitor baud rate to match
    Serial.flush();
Serial.setTimeout(10000); 

    
}

int countdata = 0 ;
bool found = false ;


void extractData(String dataInput,String &cmd,int &Value)
{
   String mesg;
   mesg.concat("I received ");mesg.concat(dataInput);
}

void loop() {
         // send data only when you receive data:
        if (Serial.available() > 0) {
                // read the incoming byte:
                String incomingData = Serial.readStringUntil('\n');

                if (incomingData.startsWith("servo1"))
                {
                  String mesg ;
                  int startPos  = incomingData.lastIndexOf(',');
                  String Value =  incomingData.substring(startPos + 1);
                  int iValue = Value.toInt();                     
                  mesg.concat("I received ");mesg.concat(incomingData);mesg.concat("Exctract Value is=");mesg.concat(iValue);
                  Serial.println(mesg);
                  servo1.writeMicroseconds(iValue);
                  found = true ;
                }

                if (incomingData.startsWith("servo2"))
                {
                 String mesg ;
                  int startPos  = incomingData.lastIndexOf(',');
                  String Value =  incomingData.substring(startPos + 1);                   
                  int iValue = Value.toInt();                     
                 
                  mesg.concat("I received ");mesg.concat(incomingData);mesg.concat("Exctract Value is=");mesg.concat(iValue);
                  Serial.println(mesg);
                  servo2.writeMicroseconds(iValue);
                  found = true ;  
                }

                if (incomingData.startsWith("servo3"))
                {
                  String mesg ;
                  int startPos  = incomingData.lastIndexOf(',');
                  String Value =  incomingData.substring(startPos + 1);                   
                  int iValue = Value.toInt();                     
                 
                  mesg.concat("I received ");mesg.concat(incomingData);mesg.concat("Exctract Value is=");mesg.concat(iValue);
                  Serial.println(mesg);
                  servo3.writeMicroseconds(iValue);
                  found = true ;
                }


                if (incomingData.startsWith("Echo"))
                {
                  String mesg ;
                  int startPos  = incomingData.lastIndexOf(',');
                  String Value =  incomingData.substring(startPos + 1);                   
                  
                  mesg.concat("I received ");mesg.concat(incomingData);mesg.concat("Exctract Value is=");mesg.concat(Value);
                  Serial.println(mesg);
                  found = true ;
                }



                if (found == false )
                {
                  Serial.println("command error!!!!");
                }

        }
}
