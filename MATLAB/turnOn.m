function [] = turnOn(ar, LEDpin)
    writeDigitalPin(ar, LEDpin, 1);
end