function [position] = getPotPos(ar, potPin)
    position = readVoltage(ar, potPin);
end