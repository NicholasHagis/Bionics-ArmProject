clear all
ar=arduino('COM5','Nano3');
writeDigitalPin(ar, 'D11',1); %1 turns on

brightness_step = (5-0)/20; %(max voltage - min voltage)/no of itterations

time=200;
while time>0
    
    voltage=readVoltage(ar,'A2')
    
    time=time-1;
    pause(0.1);
end

