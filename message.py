from sense_hat import SenseHat
import time

s = SenseHat()

while(True):
  i = input("enter a message or type 0 to exit: ")
  if i == "0":
    s.clear()
    break
  s.show_message(i)
