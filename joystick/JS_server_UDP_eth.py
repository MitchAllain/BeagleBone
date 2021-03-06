#! /usr/bin/env python

##########################################################################################
# JS_server_UDP_eth.py
#
# Identical to JS_server_UDP_USB.py except for target IP address
#
# NOTE: sends [BM, SK, BK, SW], see UDP_client_test.py for parsing example
#
# Created: March 09, 2017
#   - Mitchell Allain
#   - allain.mitch@gmail.com
#
# Modified:
#   *
#
##########################################################################################

import socket
import pygame
import time

UDP_IP = '192.168.10.2'
UDP_PORT = 9999

print "UDP IP: ", UDP_IP
print "UDP target port: ", UDP_PORT

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Initializing pygame module and joysticks...\n')
pygame.init()
pygame.joystick.init()
tm_1 = pygame.joystick.Joystick(1)
tm_1.init()
tm_0 = pygame.joystick.Joystick(0)
tm_0.init()

print('Squeeze trigger on right joystick...')
while True:
    pygame.event.pump()
    if tm_0.get_button(0) == 1:
        order = [1, 3, 0, 2]
        break
    elif tm_1.get_button(0) == 1:
        order = [3, 1, 2, 0]
        break
print('Right joystick detected.')

# print("Connected to:" + self.client_address[0])
# # Likewise, self.wfile is a file-like object used to write back
# # to the client

while True:
    pygame.event.pump()
    js = [tm_0.get_axis(0), tm_0.get_axis(1), tm_1.get_axis(0), tm_1.get_axis(1)]

    # Send: [BM, SK, BK, SW]
    sock.sendto(str([js[i] for i in order]), (UDP_IP, UDP_PORT))

    time.sleep(0.05)
