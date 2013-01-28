#header()

from wpilib import IterativeRobot, Command, Scheduler, LiveWindow
from robot_map import RobotMap
from oi import OI

# The VM is configured to automatically run this class, and to call the
# functions corresponding to each mode, as described in the IterativeRobot
# documentation. If you change the name of this class or the package after
# creating this project, you must also update the manifest file in the resource
# directory.
class Robot(IterativeRobot):
    @classmethod
    def Init(self):
        """This function is run when the robot is first started up and should
        be used for any initialization code."""
        RobotMap.Init()
        from commands import *
        from subsystems import *
#@autogenerated_code("constructors", "        ")
#parse("${exporter-path}core/robot-constructors.py")
#end
        # This MUST be here. If the OI creates Commands (which it very likely
        # will), constructing it during the construction of CommandBase (from
        # which commands extend), subsystems are not guaranteed to be
        # yet. Thus, their requires() statements may grab null pointers. Bad
        # news. Don't move it.
        self.oi = OI()

        # instantiate the command used for the autonomous period
#@autogenerated_code("autonomous", "        ")
#parse("${exporter-path}core/robot-autonomous.py")
#end

    def AutonomousInit(self):
        # schedule the autonomous command (example)
        if self.autonomousCommand is not None:
            self.autonomousCommand.Start()

    def AutonomousPeriodic(self):
        """This function is called periodically during autonomous"""
        Scheduler.GetInstance().Run()

    def TeleopInit(self):
        # This makes sure that the autonomous stops running when
        # teleop starts running. If you want the autonomous to 
        # continue until interrupted by another command, remove
        # this line or comment it out.
        if self.autonomousCommand is not None:
            self.autonomousCommand.Cancel()

    def TeleopPeriodic(self):
        """This function is called periodically during operator control"""
        Scheduler.GetInstance().Run()
        LiveWindow.Run()

    def TestPeriodic(self):
        """This function is called periodically during test mode"""
        LiveWindow.Run()
