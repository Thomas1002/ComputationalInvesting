'''
Created on 3 Apr 2013

@author: thomas
'''
import unittest
import datetime as dt
import numpy as np
import pandas as pd
import csv

class Test(unittest.TestCase):


  def setUp(self):
    pass


  def tearDown(self):
    pass

  def pandaText(self):
    pass

  def testName(self):
    date1 = dt.datetime(2010,12,24,16)
    date2 = dt.datetime(2011,12,24,16)
    array = np.array([date1, 'aap'])
    array = np.concatenate((array, [date2, 'bb']))
    r1 = [2011,1,10,'AAPL','Buy',1500,'']
    r2 = [2011,1,13,'IBM','Buy',4000,'']
    resultFile = open("myorders.csv",'wb')
    wr = csv.writer(resultFile, dialect='excel')
    #for item in results:
    wr.writerow(r1)
    wr.writerow(r2)
    ar = np.array([r1])
    ar = np.vstack([ar, r1])
    ar = np.vstack([ar, r2])
    print array, ar
    np.savetxt('arto.csv', ar, fmt='%s', delimiter=';')

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
  unittest.main()