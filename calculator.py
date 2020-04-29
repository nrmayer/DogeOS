def calculate():
  while True:
    num1 = input("1st number:")
    num2 = input("2nd number:")
    operator = input("+, -, x, /:")
    try:
      int1 = int(num1)
    finally:
      pass
    try:
      int2 = int(num2)
    finally:
      pass
    if operator == '+':
      print(int1 + int2)
    elif operator == '-':
      print(int1 - int2)
    elif operator == 'x':
      print(int1 * int2)
    elif operator == '/':
      print(int1 / int2)
    else:
      print("No operation was specified")
    exit = input("Exit? (y/n)")
    if exit == 'y':
      break
    elif exit == 'n':
      pass
    else:
      print("(y/n)")
