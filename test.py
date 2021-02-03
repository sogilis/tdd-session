import unittest

def fizzbuzz():
    numbers = []
    for i in range(1, 101):
        if (i % 15 == 0):
            numbers.append("FizzBuzz")
        elif (i % 3 == 0):
            numbers.append("Fizz")
        elif (i % 5 == 0):
            numbers.append("Buzz")
        else:
            numbers.append(i)
    return numbers
        
class FizzBuzzTest(unittest.TestCase):
  def test_regular_numbers_return_digits(self):
      self.assertEqual(1, fizzbuzz()[0])
      self.assertEqual(2, fizzbuzz()[1])

  def test_three_multiples_return_Fizz(self):
      self.assertEqual("Fizz", fizzbuzz()[2])
      self.assertEqual("Fizz", fizzbuzz()[5])

  def test_five_multiples_return_Buzz(self):
      self.assertEqual("Buzz", fizzbuzz()[4])
      self.assertEqual("Buzz", fizzbuzz()[9])

  def test_fifteen_multiples_return_FizzBuzz(self):
      self.assertEqual("FizzBuzz", fizzbuzz()[14])
      self.assertEqual("FizzBuzz", fizzbuzz()[29])

  

if __name__ == '__main__':
  unittest.main()