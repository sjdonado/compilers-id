#!/usr/local/bin/python3
import re

def validate(args):
  line = "".join(args)

  days_length_val = r'(\d{1,2})'
  months_length_val = r'(\d{1,2})'
  year_length_val = r'(\d{4})'

  groups = re.search(r"^{}/{}/{}$".format(
      days_length_val,
      months_length_val,
      year_length_val
    ), line)
    
  if (groups == None):
    return False

  days = groups.group(1)
  months = groups.group(2)
  year = groups.group(3)

  days_interval_val = re.match(r'^(0[1-9]|[1-9]|[12][0-9]|3[01])$', days)
  months_interval_val = re.match(r'^(0[1-9]|[1-9]|1[0-2])$', months)
  year_interval_val = re.match(r'^([1-9][0-9]{3})$', year)

  return days_interval_val != None and months_interval_val != None and year_interval_val != None

def main():
  date_input = input('Ingresar fecha: ')
  print("{}".format('Fecha valida' if validate(date_input) else 'Fecha invalida'))

def test():
  assert validate(['30/09/1998']) == True, 'Should be True'
  assert validate(['01/12/2000']) == True, 'Should be True'
  assert validate(['1/12/2000']) == True, 'Should be True'
  assert validate(['01/1/2000']) == True, 'Should be True'
  assert validate(['01/01/2000']) == True, 'Should be True'
  assert validate(['31/01/2000']) == True, 'Should be True'
  
  assert validate(['01/12/2000 10/09/1900']) == False, 'Should be False'
  assert validate(['01/12/2000 \n 10/09/1900']) == False, 'Should be False'
  assert validate(['']) == False, 'Should be False'
  assert validate(['20122000']) == False, 'Should be False'
  assert validate(['2012/2000']) == False, 'Should be False'
  assert validate(['20/122000']) == False, 'Should be False'
  assert validate(['20/12/2000/']) == False, 'Should be False'
  assert validate(['/20/12/2000/']) == False, 'Should be False'

  assert validate(['40/12/2000']) == False, 'Should be False'
  assert validate(['0/12/2000']) == False, 'Should be False'
  assert validate(['01/13/2000']) == False, 'Should be False'
  assert validate(['01/1/100']) == False, 'Should be False'
  assert validate(['01/1/0']) == False, 'Should be False'

  print('Tests passed successfully')

if __name__ == '__main__':
  test()
  main()