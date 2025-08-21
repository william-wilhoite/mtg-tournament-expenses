'''
Custom functions to operate on Pandas dataframes within project
'''

import pandas as pd
import datetime as dt

def low_price(prices, start, end) -> pd_df:
  '''
  Takes a price per day dateframe and returns the lowest price
  between the start and end dates.
  Date format '4-digit Year'-'2-digit month'-'2-digit day'.
  Requires date and price columns in dataframe.
  '''
  start = pd.to_datetime(start, format='%Y-%m-%d')
  end   = pd.to_dataframe(end,  format='%Y-%m-%d')

  prices = prices.loc[ 
             prices['date'].isbetween(start, end, inclusive = 'both')
           ]
  return 