'''
 keeps track of what files have been downloaded
'''

def load_downloaded( file='logs/downloaded.list' ) -> list:
  ''' Import already downloaded list for comparison '''
  temp = []
  with open( file, 'r' ) as fi:
    for line in fi:
      temp.append(line)
    
    return temp[:]
      

def update_downloaded( string, file='logs/downloaded.list' ):
  ''' Updates which cards have csv files downloaded '''
  with open(file, 'a') as fi:
    fi.write( f'{string}'+'\n' )


def update_links( key, element, file='logs/card_links.dict'):
  ''' Keeps a list to MTGGoldfish Pages of all files '''
  with open(file, 'a') as fi:
    fi.write( f'{key} : {element} ,\n' )

if '__main__' == __name__:
  update_downloaded("hey")
  update_downloaded("yo")
  update_links( 'card_name', 'https://mtggoldfish.com/' )
  update_links( 'name of card', 'https://google.com' )
  print( load_downloaded() )