ar = arduino('/dev/cu.usbmodem14201','Uno'); %% /dev/cu.usbmodem14201 or /dev/tty.usbmodem14201 for Ed's Mac's left port
turnOn(ar, 'D11');
position = getPotPos(ar, 'A3')