# 0=Black
# 1=Red
import random
import sys
import time
p1_win = 0
p2_win = 0
tries = input("How many times should I run the program?: ")
if int(tries) <= 0:
  print("Shutting down...")
else:
  while p1_win + p2_win<int(tries):
    p1cards= []
    p2cards= []
    win = []
    pokus = p1_win + p2_win
    cycle = 0
    p1cards.clear()
    p2cards.clear()
    win.clear()
    attemps = 1000
    if int(tries)<=attemps:
      print("Attemp number:", pokus)
    elif int(pokus)%attemps==0:
      print("Attemp number:", pokus)
    p1a = random.randrange(0,2)
    p1b = random.randrange(0,2)
    p1c = random.randrange(0,2)
    p1cards.append(p1a)
    p1cards.append(p1b)
    p1cards.append(p1c)
    if p1b == 0:
      p2a=1
    if p1b == 1:
      p2a=0
    p2b = p1a
    p2c = p1b
    p2cards.append(p2a)
    p2cards.append(p2b)
    p2cards.append(p2c)
    win1 = random.randrange(0,2)
    win2 = random.randrange(0,2)
    win3 = random.randrange(0,2)
    win.append(win1)
    win.append(win2)
    win.append(win3)
    while cycle<1:
      if win == p1cards:
        cycle = cycle + 1
        p1_win = p1_win + 1
      elif win == p2cards:
        cycle = cycle + 1
        p2_win = p2_win + 1
      else:
        win.pop(0)
        wingen = random.randrange(0,2)
        win.insert(2, wingen)
  print("Done")
  procenta_p1 = (p1_win/int(tries))*100
  procenta_p2 = (p2_win/int(tries))*100
  print("P1 complete:", p1_win, "which is", float(procenta_p1),"%")
  print("P2 complete:", p2_win, "which is", float(procenta_p2), "%")
  time.sleep(60)
  