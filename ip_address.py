#!/usr/local/bin/python3
import re

def validate(args):
  line = "".join(args)
  octet = r'(([0-9])|([1-9][0-9])|(1([0-9]{2}))|(2([0-4][0-9]|5[0-5])))'
  return re.match(fr'{octet}\.{octet}\.{octet}\.{octet}$', line)

def main():
  exit = False
  while exit == False:
    input_line = input('Ingresar dirección ip: ')
    print('{}'.format('Dirección ip valida' if validate(input_line) else 'Dirección ip invalida'))
    if input('¿Salir? [Y/n]: ') == 'Y':
      exit = True

def test():
  assert validate(['4.20.109.3']) is not None, 'Should not be None'
  assert validate(['122.122.255.0']) is not None, 'Should not be None'
  assert validate(['4.1.10.41']) is not None, 'Should not be None'
  assert validate(['124.20.255.255']) is not None, 'Should not be None'

  assert validate(['267.0.109.3']) is None, 'Should be None'
  assert validate(['1.01.255.0']) is None, 'Should be None'
  assert validate(['0.0.289.299']) is None, 'Should be None'
  assert validate(['198.0.299.299']) is None, 'Should be None'

  print('Tests passed successfully')

if __name__ == '__main__':
  test()
  main()