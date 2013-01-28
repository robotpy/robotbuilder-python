#set($subsystem = $helper.getByName($subsystem-name, $robot))
        super().__init__(${subsystem.getProperty("P").getValue()}, ${subsystem.getProperty("I").getValue()}, ${subsystem.getProperty("D").getValue()})
        self.GetPIDController().SetAbsoluteTolerance(${subsystem.getProperty("Tolerance").getValue()})
        self.GetPIDController().SetContinuous(#truefalse(${subsystem.getProperty("Continuous").getValue()}))
#if($subsystem.getProperty("Limit Input").getValue())
        self.GetPIDController().SetInputRange(${subsystem.getProperty("Minimum Input").getValue()}, ${subsystem.getProperty("Maximum Input").getValue()})
#end
#if($subsystem.getProperty("Limit Output").getValue())
        self.GetPIDController().SetOutputRange(${subsystem.getProperty("Minimum Output").getValue()}, ${subsystem.getProperty("Maximum Output").getValue()})
#end
