'''
Created on 28 Mar 2013

@author: thomas
'''
import numpy as np
import pandas as pd
import datetime as dt
import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.DataAccess as da

def find_symbols_dates(orders):
  data = pd.read_csv(orders, parse_dates=True, names=['year','month','day','symbol','transaction','nr_shares','empty'], header=0)
  data = data.sort(['year', 'month', 'day']);
  array = np.array(data)
  symbols = np.unique(array[:,3])
  symbols = np.array(symbols, dtype='S').tolist()
  print 'type', type(symbols)
  start_date = dt.datetime(array[0,0], array[0,1], array[0,2])
  end_date = dt.datetime(array[-1,0], array[-1,1], array[-1,2])
  print '%s - %s' % (start_date, end_date)  
  print symbols
  return symbols, start_date, end_date, array

def load_data(symbols, dt_start, dt_end, key):
  timestamps = du.getNYSEdays(dt_start, dt_end, dt.timedelta(hours=16))
  dataobj = da.DataAccess('Yahoo')
  data = dataobj.get_data(timestamps, symbols, key)
  price = data.values
  return price

def run(cash, orders, values, key):
  result = find_symbols_dates(orders)
  prices = load_data(result[0], result[1], result[2], key)
  order_data = result[3]
  print prices
  print order_data
  
  '''dt_start = symbols_and_dates[1]
  dt_end = symbols_and_dates[2]
  symbols = symbols_and_dates[0]
  print "symbols %s" % (symbols)'''

  
if __name__ == '__main__':
  run(1000000, 'orders.csv', 'values.csv', 'actual_close')
  