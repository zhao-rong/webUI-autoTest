from testsuites.baseTestCase import BaseTestCase
import unittest
from project1.second_Dz import Second


class Test_second(BaseTestCase):
    def test_second(self):
        second_pro=Second(self.driver)
        second_pro.Alogin('admin','root')

        second_pro.delete_tie()

        second_pro.new_bankuai()

        second_pro.loginout()

        second_pro.Plogin('asd','asd')

        second_pro.fatie('ssssees','asdzxcvbnm,nfgh')

        second_pro.reply('sdfghjkgf')

if __name__ == '__main__':
    unittest.main(verbosity=2)