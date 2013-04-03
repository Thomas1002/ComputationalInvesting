'''
Created on 22 Mar 2013

@author: thomas
'''
import unittest
import event_profiler as ep
import datetime as dt

class Test(unittest.TestCase):


  def setUp(self):
    self.dt_start = dt.datetime(2008, 1, 1, 16)
    self.dt_end = dt.datetime(2009, 12, 31, 16)


  def tearDown(self):
    pass


  def test2012(self):
    count = ep.study(self.dt_start, self.dt_end, 'sp5002012', 'actual_close', 'EventStudy2012', 5.0, 5)
    self.assertEqual(176.0, count, 'msg')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test2012']
    unittest.main()