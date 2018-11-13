classdef armSDK
    %ARMSDK Summary of this class goes here
    %   Detailed explanation goes here
    
    properties
        Property1
    end
    
    methods
        function self = armSDK(inputArg1,inputArg2)
            %ARMSDK Construct an instance of this class
            %   Detailed explanation goes here
            self.Property1 = inputArg1 + inputArg2;
        end
        
        function outputArg = method1(self,inputArg)
            %METHOD1 Summary of this method goes here
            %   Detailed explanation goes here
            outputArg = self.Property1 + inputArg;
        end
        
        function ledOn(self)
            %METHOD1 Summary of this method goes here
            %   Detailed explanation goes here
            "Turning LED on"
        end
    end
end

