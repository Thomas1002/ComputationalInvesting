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
  print na_price
  '''plot(na_price, 'Adjusted close', ldt_timestamps, ls_symbols)'''
  print 'normalized prices'
  normalized_price = na_price / na_price[0, :]
  print 'cumulative'
  c = normalized_price * allocation
  print c
  np.set_printoptions(precision=7)
  print 'sum'
  invest = c.sum(axis=1)
  print invest
  np.set_printoptions(precision=3)
  copy = invest.copy()
  print 'copy' 
  print copy
  dr = tsu.returnize0(copy)
  print 'dr'
  print dr
  
  print 'fc'
  fc = invest / invest[0] * 100.0
  print fc
  np.set_printoptions(precision=3)
  daily_returns = np.array([1.000] + [100.0 * ((invest[i] / invest[i-1]) - 1) for i in range(1, len(invest))])
  print daily_returns
  print len(daily_returns)
  
  drsum = daily_returns.sum() / len(daily_returns)
  print 'drsum %f %f %f' % (daily_returns.sum(), len(daily_returns), drsum)
  print daily_returns.std()
  
  print invest.sum() / len(invest)
  ''''b = normalized_price.transpose() * [0.6, 0.4]
  print b
  print 100.0 * normalized_price'''
  '''print 'norm %'
  b = normalized_price * 100.0
  print b'''
  
  
if __name__ == '__main__':
  np.set_printoptions(precision=2)
  symbols = ["AAPL", "GLD", "GOOG", "$SPX", "XOM"]
  symbols = ["AAPL", "GOOG", "XOM", "GLD"]
  startdate = dt.datetime(2011, 1, 1)
  enddate = dt.datetime(2011, 12, 31)
  allocation = [0.4, 0.0, 0.2, 0.4]
  
  simulate(startdate, enddate, symbols, allocation)