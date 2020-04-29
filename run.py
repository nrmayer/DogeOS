import getpass
import calculator
from clss import *
def run(user):
  print('Welcome,', user)
  while True:
    cmd = input('>>>')
    if cmd == 'help':
      print('''calculator : Allows you to use a calculator.
      passchange : Changes your password
      signout : signs out of your account
      ''')
    elif cmd.lower() == 'calculator':
      calculator.calculate()
    elif cmd.lower() == 'passchange':
      cls = eval(user)
      old = getpass.getpass('Old Password: ')
      if old == cls().dict['Password']:
        new = getpass.getpass('New Password:')
        cls().dict["Password"] = new
        print('Password successfully changed')
      else:
        print('Old password incorrect.')
    elif cmd.lower() == 'signout':
      import login
      login.login()
    