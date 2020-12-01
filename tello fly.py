Tello = Device(sock, tello_address)

Tello.manual_nsg('streamon')

Tello.non()
time.sleep(1)
Tello.ndirection_x(0)
time.sleep(1)
Tello.takeoff()
time.sleep(1)

Tello.go_loc_speed_nid(0, 0, 100), 50, 'n1')
time.sleep(8)
Tello.jump((80, 0, 100), 50, 0, 'n1', 'n2')
time.sleep(8)
Tello.jump((80, 0, 100), 50, 0, 'n2', 'n3')
time.sleep(8)
Tello.jump((80, 0, 100), 50, 0, 'n3', 'n4')
time.sleep(8)
Tello.jump((80, 0, 100), 50, 0, 'n4', 'n1')
time.sleep(8)




