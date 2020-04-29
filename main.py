import replit
import time
from login import login
def loading(msg, t, finish):
  i = 0
  while i < 101:
    time.sleep(t)
    replit.clear()
    f = 100 - i
    print(msg)
    print("|" * i + "-" * f)
    print()
    i = i + 1
  print(finish)

def boot():
  loading('Loading DogeOS...', 0.03, 'DogeOS v0.1 Loaded!')
  loaded = True
boot()

login()