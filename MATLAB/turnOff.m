function [] = turnOff(ar, LEDpin)
    writeDigitalPin(ar, LEDpin, 0);
end