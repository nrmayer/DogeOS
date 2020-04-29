import getpass
from run import run

def login():
  from clss import user1
  from clss import user2
  from clss import user3
  usr = input('Username: ')
  pswrd = getpass.getpass('Password: ')
  if usr == 'user1':
    if pswrd == user1.dict['Password']:
      run('user1')
    else:
      print('Incorrect password')
      login()
  elif usr == 'user2':
    if pswrd == user2.dict['Password']:
      run('user2')
    else:
      print('Incorrect password')
      login()
  elif usr == 'user3':
    if pswrd == user3.dict['Password']:
      run('user3')
    else:
      print('Incorrect password')
      login()
  else:
    print('Username not recognized. Try user1, user2, or user3.')
    login()