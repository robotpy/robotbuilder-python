#set($subsystem = $helper.getByName($subsystem-name, $robot))
#set($component = $subsystem.getProperty("Output").getValue())
#set($name = ${helper.getByName($component, $robot).name})
#if($name)        self.#variable($name).PIDWrite(output)
#else        pass
#end
