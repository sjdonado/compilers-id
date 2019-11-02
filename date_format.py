import re

def validate(args):
  line = "".join(args)
  days_length_val = r'(\d{2})'
  months_length_val = r'(\d{2})'
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

  year_interval_val = re.match(r'^([1-9][0-9]{3})$', year)
  months_interval_val = re.match(r'^(0[1-9]|[1-9]|1[0-2])$', months)

  days_regex = None
  if year_interval_val != None and months_interval_val != None:
    # February validation
    if re.match(r'^(02)$', months) != None:
      # Leap years validation
      if re.match(r'^((\d{2}[02468][048])|(\d{2}[13579][26]))$', year) != None:
        if re.match(r'^(\d{2}[0][0])$', year)!= None:
          if re.match(r'^(([2468][048][0][0])|([13579][26][0][0]))$', year) != None:
            days_regex = '^(0[1-9]|[12][0-9])$'
          else:
            days_regex = '^(0[1-9]|[12][0-8])$'
        else:
          days_regex = '^(0[1-9]|[12][0-9])$'
      else:
        days_regex = '^(0[1-9]|[12][0-8])$'
    else:
      # 30 day months validation
      if re.match(r'^(0[469]|11)$', months) != None:
        days_regex = '^(0[1-9]|[12][0-9]|30)$'
      else:
        days_regex = '^(0[1-9]|[12][0-9]|3[01])$'

  if days_regex != None:
    return re.match(r"{}".format(days_regex), days) != None

  return False

def main():
  date_input = input('Ingresar fecha: ')
  if date_input!="exit":
    print("{}".format('Fecha valida' if validate(date_input) else 'Fecha invalida'))
  if date_input!="exit":
    main()

def test():
  assert validate(['30/09/1998']) == True, 'Should be True'
  assert validate(['01/12/2000']) == True, 'Should be True'
  assert validate(['1/12/2000']) == False, 'Should be False'
  assert validate(['01/1/2000']) == False, 'Should be False'
  assert validate(['01/01/2000']) == True, 'Should be True'
  assert validate(['31/01/2000']) == True, 'Should be True'
  assert validate(['31/02/2000']) == False, 'Should be False'
  assert validate(['31/12/2000']) == True, 'Should be True'
  
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

  assert validate(['29/02/2012']) == True, 'Should be True'
  assert validate(['29/02/1904']) == True, 'Should be True'
  assert validate(['29/02/2014']) == False, 'Should be False'

  print('Tests passed successfully')

if __name__ == '__main__':
  test()
  main()