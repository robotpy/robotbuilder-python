#set($autonomous = $robot.getProperty("Autonomous Command").getValue())
#if($autonomous != "None")        self.autonomousCommand = #class($autonomous)()
#else        self.autonomousCommand = None
#end
