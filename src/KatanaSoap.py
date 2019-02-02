import SOAPpy


class KatanaSoap:
    def __init__(self, ip="10.162.242.242", port="8000"):
        self.katana = SOAPpy.SOAPProxy("http://" + ip + ":" + port)

    def calibrate(self, axis=0, force=False):
        self.katana.calibrate(axis, force)

    def moveMotAndWait(self, axis, pos):
        self.katana.moveMotAndWait(axis, pos)

    def terminate(self):
        self.katana.terminate()

    def init(self):
        self.katana.init()

    def moveMot(self, enc, speed=0, accel=0, tolerance=0, rangeCheck=True):
        self.katana.moveMot(enc, speed, accel, tolerance, rangeCheck)

    def motorOff(self, axis):
        self.katana.motorOff(axis)

    def allMotorsOff(self):
        self.katana.allMotorsOff()

    def motorFreeze(self):
        self.katana.motorFreeze()

    def freezeAllMotors(self):
        self.katana.freezeAllMotors()

    def closeGripper(self):
        self.katana.closeGripper()

    def openGripper(self):
        self.katana.openGripper()

    def setMaxVelocity(self, axis, vel):
        self.katana.setMaxVelocity(axis, vel)

    def setMaxAccel(self, axis, accel):
        self.katana.setMaxAccel(axis, accel)

    def fakeCalibration(self, axis, offset):
        self.katana.fakeCalibration(axis, offset)