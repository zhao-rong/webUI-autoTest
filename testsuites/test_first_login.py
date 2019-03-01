from testsuites.baseTestCase import BaseTestCase
import unittest
from project1.first_login import First


class Test_login(BaseTestCase):
    def test_login(self):
        self.first=First(self.driver)
        self.first.login('admin','root')

        self.first.fatie('12344e','123fxg4566789')

        self.first.reply('kaalaalalalla')

        self.first.loginout()

if __name__=='__main__':
    unittest.main(verbosity=2)