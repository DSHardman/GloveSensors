classdef Trial
    % Sojiro's Bayesian Optimisation results: single trial
    properties
        position
        width
        startpoint
        endpoint
        angle
        offset
        pose1
        pose2
        pose3
        R12
        R13
        score
        rank
    end

    methods
        function obj = Trial(inputrow)
            % Constructor from single line of CSV file
            obj.position = inputrow(1);
            obj.width = inputrow(2);
            obj.startpoint = inputrow(3);
            obj.endpoint = inputrow(4);
            obj.angle = inputrow(5);
            obj.offset = inputrow(6);
            obj.pose1 = inputrow(7);
            obj.pose2 = inputrow(8);
            obj.pose3 = inputrow(9);
            obj.R12 = inputrow(10);
            obj.R13 = inputrow(11);
            obj.score = inputrow(12);
            obj.rank = inputrow(13);
        end

%         function outputArg = method1(obj,inputArg)
%             %METHOD1 Summary of this method goes here
%             %   Detailed explanation goes here
%             outputArg = obj.Property1 + inputArg;
%         end
    end
end