#set($command = $helper.getByName($command-name, $robot))
#if ($command.getProperty("Requires").getValue() != "None")
        self.Requires(Robot.#variable(${command.getProperty("Requires").getValue()}))
#else
        pass
#end
