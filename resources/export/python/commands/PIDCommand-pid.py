#set($command = $helper.getByName($command-name, $robot))
        super().__init__(${command.getProperty("P").getValue()}, ${command.getProperty("I").getValue()}, ${command.getProperty("D").getValue()}, ${command.getProperty("Period").getValue()})
        self.GetPIDController().SetContinuous(${command.getProperty("Continuous").getValue()})
        self.GetPIDController().SetAbsoluteTolerance(${command.getProperty("Tolerance").getValue()})
#if($command.getProperty("Limit Input").getValue())
        self.GetPIDController().SetInputRange(${command.getProperty("Minimum Input").getValue()}, ${command.getProperty("Maximum Input").getValue()})
#end
#if($command.getProperty("Limit Output").getValue())
        self.GetPIDController().SetOutputRange(${command.getProperty("Minimum Output").getValue()}, ${command.getProperty("Maximum Output").getValue()})
#end
