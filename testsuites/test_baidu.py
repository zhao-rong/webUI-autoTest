import unittest
from testsuites.baseTestCase import BaseTestCase
from baidu.search import BaiduSearch


class TestSearch(BaseTestCase):
    def test_search(self):

        home_page=BaiduSearch(self.driver)
        home_page.search('seleuinmhp')

if __name__=='__main__':
    unittest.main(verbosity=2)