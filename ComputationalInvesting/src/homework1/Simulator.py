'''
Created on 11 Mar 2013

@author: thomas
'''
import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.tsutil as tsu
import QSTK.qstkutil.DataAccess as da

import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from Onboard.utils import matmult

def simulate(startdate, enddate, symbols, allocation):
  timeofday = dt.timedelta(hours=16)
  timestamps = du.getNYSEdays(startdate, enddate, timeofday)
  c_dataobj = da.DataAccess('Yahoo')
  ls_keys = ['close']
  ldf_data = c_dataobj.get_data(timestamps, symbols, ls_keys)
  d_data = dict(zip(ls_keys, ldf_data))
  
  na_price = d_data['close'].values
  #print na_price
  '''plot(na_price, 'Adjusted close', ldt_timestamps, ls_symbols)'''
  #print 'normalized prices'
  normalized_price = na_price / na_price[0, :]
  #print 'cumulative'
  c = normalized_price * allocation
  #print c
  #print ' Fund Invest $'
  invest = c.sum(axis=1)
  #print invest

  daily_returns = tsu.daily(invest) 
  #print 'Daily returns %'
  #print daily_returns * 100.0
  mean_daily_return = np.mean(daily_returns) 
  stdev_daily_return = np.std(daily_returns)
  #sharpe_ratio = mean_daily_return / stdev_daily_return * np.sqrt(252)
  sharpe_ratio = tsu.get_sharpe_ratio(daily_returns)
  return stdev_daily_return, mean_daily_return, sharpe_ratio, invest[-1]
 
  
if __name__ == '__main__':
  np.set_printoptions(precision=2)
  symbols = ["AAPL", "GLD", "GOOG", "$SPX", "XOM"]
  symbols = ["AAPL", "GOOG", "XOM", "GLD"]
  #symbols = ["AAPL", "GLD"]
  startdate = dt.datetime(2011, 1, 1)
  enddate = dt.datetime(2011, 12, 31)
  allocation = [0.4, 0.0, 0.2, 0.4]
  #allocation = [0.6, 0.4]
  
  result = simulate(startdate, enddate, symbols, allocation)
  print 'Sharpe ratio: %.11f' % (result[2])
  print 'Volatility %.13f' % (result[0])
  print 'Average Daily Return %.15f' % (result[1])
  print 'Cumulatative return %.11f' % (result[-1])
  