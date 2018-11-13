%Matlab automatically looks in the current working directory for classes
%and functions.
%whats even better is that we can just run the code in the command window
%and open and close the hand from there. Perhaps in future we can do some
%kinimatics in matlab and some reverse kinimatics. Once we have all the
%correct locations we would simply type arm.moveTo(angle1 , angle2, ... )

arm = armSDK(1,2)
arm.ledOn()
