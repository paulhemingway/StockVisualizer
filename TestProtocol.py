import unittest
from unittest import mock
import datetime
from stockvisualizer import chart_type, stock_symbol, time_series, get_dates

class Tests(unittest.TestCase):

  def test_stock_symbol_valid(self):
    original_input = mock.builtins.input
    mock.builtins.input = lambda _: "GOOGL"
    result = stock_symbol()
    self.assertEqual(result, 'GOOGL')

  def test_stock_symbol_long(self):
    original_input = mock.builtins.input
    mock.builtins.input = lambda _: "INSTAGRAM"
    result = stock_symbol()
    self.assertEqual(result, 'NA')

  def test_stock_symbol_numeric(self):
    original_input = mock.builtins.input
    mock.builtins.input = lambda _: "30GOOGL"
    result = stock_symbol()
    self.assertEqual(result, 'NA')    

  def test_time_series_valid(self):
    original_input = mock.builtins.input
    mock.builtins.input = lambda _: "2"
    result = time_series()
    self.assertEqual(result, 2)

  def test_time_series_out(self):
    original_input = mock.builtins.input
    mock.builtins.input = lambda _: "8"
    result = time_series()
    self.assertEqual(result, 0)

  def test_time_series_alpha(self):
    original_input = mock.builtins.input
    mock.builtins.input = lambda _: "a"
    result = time_series()
    self.assertEqual(result, 0)    

  def test_chart_type_bad_integer(self):
    original_input = mock.builtins.input
    mock.builtins.input = lambda _: "3"
    result = chart_type()
    self.assertRaises(ValueError)
  
  def test_chart_type_letter(self):
    original_input = mock.builtins.input
    mock.builtins.input = lambda _: "a"
    result = chart_type()
    self.assertRaises(ValueError)

  def test_chart_type_valid(self):
    original_input = mock.builtins.input
    mock.builtins.input = lambda _: "1"
    result = chart_type()
    self.assertEqual(result, 1)

  def test_get_dates_bad_input(self):
    original_input = mock.builtins.input
    mock.builtins.input = lambda _: "202-2-2"
    result = get_dates()
    self.assertRaises(ValueError)
  
  def test_get_dates_valid(self):
    target = datetime.datetime(2022,2,1)

    original_input = mock.builtins.input
    mock.builtins.input = lambda _: "2022-02-01"
    result = get_dates()
    self.assertEqual(result[0], target)



if __name__ == '__main__':
  unittest.main()