int LEDpin = 11;
int potPin = A3;
float Vout;
char state;

void setup() {
  // put your setup code here, to run once:
  pinMode(LEDpin, OUTPUT);
  pinMode(potPin, INPUT);
  Serial.begin(9600); //opens the serial port and tells it to send data at 9600 bits/sec
  while (!Serial); //tells it to wait until the serial port is open
}

void loop() {
  
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0) { //see's whats in the serial buffer
    
    // Reads the potentiometer voltage
    int sensorValue = analogRead(potPin); //Outputs int 0-1023
    Vout = sensorValue * (5.0/1023.0); //Converts int value to true voltage
    String strVout = String(Vout); //Turns into a string
    int len = strVout.length(); //Length of string
    //Iterates over each letter of string and sends it as a character
    for (int i = 0; i <= len; i++) { 
      if (i == len) {
        Serial.write('\n');
        } else {
        Serial.write(strVout[i]);
        }
    }
    
    state = Serial.read(); //reads the data from the serial monitor and stores the data

    switch (state) {
      case '0':
        digitalWrite(LEDpin, LOW);
        break;
      case '1':
        digitalWrite(LEDpin, HIGH);
        break;
      case '2':
        break;
    }

  }
  
}
  
