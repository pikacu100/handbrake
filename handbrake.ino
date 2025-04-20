
const int potPin = A7;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int potValue = analogRead(potPin);

  Serial.println(potValue);

  delay(50);
}
