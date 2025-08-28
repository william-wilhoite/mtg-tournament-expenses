'''
Custom functions to operate on Pandas dataframes within project
'''

import pandas as pd
import datetime as dt
import warnings

def low_price(cardname:str, prices: pd.DataFrame, start, end) -> pd.DataFrame:
  '''
  Takes a card name & price per day dateframe and returns the lowest price
  between the start and end dates as a one row dataframe.
  Date format '4-digit Year'-'2-digit month'-'2-digit day'.
  Requires date and price columns in dataframe.
  '''
  warnings.filterwarnings('ignore')
  
  start = pd.to_datetime(start, format='%Y-%m-%d')
  end   = pd.to_datetime(end,  format='%Y-%m-%d')
  prices['date'] = pd.to_datetime(prices['date'])

  prices = prices.loc[ 
             prices['date'].between(start, end, inclusive = 'both')
           ]
  prices['card name'] = cardname
  prices = prices.rename(columns={'price':'low price'})

  warnings.resetwarnings()
  
  return prices.nsmallest(1, 'low price')[['card name', 'low price']]

# too finish