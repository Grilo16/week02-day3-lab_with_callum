import unittest
from src.pub import Pub

# creating a class called TestPub thats parameters is inherited from unittest.TestCase


class TestPub(unittest.TestCase):

    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)

    # the above function is called the Pub class and assinging the pub name as The Prancing Pony and the till
    # float of 100.00. setUp(self) will always reset the pub back to these initial parameters.

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_had_till(self):
        self.assertEqual(100.00, self.pub.till)

    def test_increase_till(self):
        self.pub.increase_till(2.5)
        self.assertEqual(102.50, self.pub.till)

    # this can also be written in the format below which will assign variables which are passed as arguments
    # the self asset arguments.

    # def test_add(self):
    #     self.pub.increase_till(2.50)
    #     expected = 102.50
    #     actual = self.pub.till
    #     self.assertEqual(expected, actual)
