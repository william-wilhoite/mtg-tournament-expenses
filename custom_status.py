# https://stackoverflow.com/questions/4142151/how-to-import-the-class-within-the-same-directory-or-sub-directory
from time import sleep

# https://itnext.io/overwrite-previously-printed-lines-4218a9563527
def print_refresh(string):
    print(string, 
          '\t\t\t\t\t\t\t\t\t\t\t\t',
          end='\r', 
          flush = True
         )

def pause_update(n, start='', end=''):
    for i in range(n):
        print_refresh(f'{start} Waiting {n} seconds: {n-i} seconds remaining{end}')
        sleep(1)
    print_refresh(f'{start} Finished with {n} second wait{end}')
  
