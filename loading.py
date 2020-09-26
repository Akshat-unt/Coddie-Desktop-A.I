from time import sleep
import replit
import random

replit.clear()

#variabels

def loading():

  percent = 0
  loading = True
  loadingtime = random.uniform(0.1,  0.5)

  while loading == True:
      print ("""Loading...\n
      [""", percent, "%]\n")
      sleep (0.3)
      percent = percent + 4
      replit.clear()

      if percent == 100:
        replit.clear()
        print("READY!!")
        sleep (2)
        break

loading()