import KatanaSoap

katana = KatanaSoap.KatanaSoap()

max_angle = 30500
min_angle = 0

def init():
    katana.calibrate()
    katana.moveMotAndWait(1, int(0.7 * max_angle))
    katana.moveMotAndWait(2, int(-0.3 * max_angle))
    katana.moveMotAndWait(3, int(-0.7 * max_angle))
    katana.moveMotAndWait(4, int(0.2 * max_angle))

def move_right():
    katana.moveMotAndWait(1, int(0.75 * max_angle))

def move_left():
    katana.moveMotAndWait(1, int(0.65 * max_angle))

def move_down():
    katana.moveMotAndWait(4, int(0.1 * max_angle))

def move_up():
    katana.moveMotAndWait(4, int(0.3 * max_angle))
