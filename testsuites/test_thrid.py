#coding: utf-8
from testsuites.baseTestCase import BaseTestCase
from project1.third_Dz import Third

class Test_Third(BaseTestCase):
    def test_third(self):
        third_pro=Third(self.driver)

        third_pro.login('admin','root')

        title=third_pro.search('haotest')

        try:
            self.assertEqual(title,'haotest',msg=title)
            print("帖子标题与预期结果相符")
        except:
            print("帖子标题与预期结果不符")


        third_pro.loginout()