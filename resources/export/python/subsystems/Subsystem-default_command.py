#set($subsystem = $helper.getByName($subsystem-name, $robot))
#if ($subsystem.getProperty("Default Command").getValue() != "None")
        self.SetDefaultCommand(#class($subsystem.getProperty("Default Command").getValue())())
#else
        pass
#end
