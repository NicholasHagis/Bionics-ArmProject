int LEDpin = 11;
char state;

void setup() {
  // put your setup code here, to run once:
  pinMode(LEDpin, OUTPUT);
  Serial.begin(9600); //opens the serial port and tells it to send data at 9600 bits/sec
  while (!Serial); //tells it to wait until the serial port is open
  Serial.println("Input 1 to turn LED on, 0 to turn LED off");
}

void loop() {
  
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0) { //see's whats in the serial buffer
    
    state = Serial.read(); //reads the data from the serial monitor and stores the data
    
    if (state == '1') {
      digitalWrite(LEDpin, HIGH);
      Serial.println("LED is on");
    }
    
    if (state == '0') {
      digitalWrite(LEDpin, LOW);
      Serial.println("LED is off");
    }

  }
  
}
