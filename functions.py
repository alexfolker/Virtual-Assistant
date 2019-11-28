import time
import sys

def task(task):
  if task == "what time is it" or task == "time":
    print("Hour is: ")
    print(time.gmtime(time.time()).tm_hour)
    print("Minute is: ")
    print(time.gmtime(time.time()).tm_min)
    print("Second is: ")
    print(time.gmtime(time.time()).tm_sec)
  elif task == "shut up":
    print("NO U")
  elif task == "hour" or task == "what hour is it":
    print("Hour is: ")
    print(time.gmtime(time.time()).tm_hour)
  elif task == "minute" or task == "what minute is it":
    print("Minute is: ")
    print(time.gmtime(time.time()).tm_min)
  elif task == "make me a sandwich":
    print("       |    ")
    print("       |    ")
    print("    | ||||  ")
    print("     |||||  ")
  elif task == "nothing":
    sys.exit()
  else:
    print("Sorry I can't do that right now")


def run():
  moodGood = ["good","Good","I am good","i am good", "i am doing good", "I am doing good", "fantastic", "i am doing well", "I am doing well", "i am fine", "I am fine"]

  moodBad = ["bad","Bad","I am bad","i am bad", "i am doing bad", "I am doing bad", "not so good", "not good"]

  name = input("What is your name?   ")
  
  print("Hello " + name)
  print("How are you?")

  mood = input()

  if mood in moodGood:
    print("Well I am good too")
  elif mood in moodBad:
    print("Well I hope that you will feel better " + name)
  else:
    print("Okie Dokie")
