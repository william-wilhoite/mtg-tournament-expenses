'''
Allows for reprinting to the same line and doing so while printing out a sleep timer.
'''
from time import sleep


# https://itnext.io/overwrite-previously-printed-lines-4218a9563527
def print_refresh(string):
  ''' Used to print status updates to oneline '''  
#  print('                                                                                               ',
#        end='\r', 
#        flush = True
#  )
  print('::: ' + string + ' :::',
        end='\r', 
        flush = True
  )


def pause_update(n, start='', end=''):
  ''' Sleeps for n seconds while printing an update '''
  for i in range(n):
    print_refresh(f'{start} Waiting {n} seconds: {n-i} seconds remaining: {end}')
    sleep(1)
  print_refresh(f'{start} Finished with {n} second wait: {end}')
  
if '__main__' == __name__:
  pause_update(7 , start = f'testing function pause_update from {__name__}:', end= f'It is working' )
  print_refresh( f'print_refresh from {__name__} also works; testing done, good job.' )
  print()


# https://stackoverflow.com/questions/4142151/how-to-import-the-class-within-the-same-directory-or-sub-directory
