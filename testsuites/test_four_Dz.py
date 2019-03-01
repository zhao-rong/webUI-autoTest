from testsuites.baseTestCase import BaseTestCase
from project1.four_Dz import Four


class Test_Four(BaseTestCase):
    def test_four(self):
        four_pro=Four(self.driver)
        four_pro.login('admin','root')
        four_pro.set_vote('set vote','num-one','num-two','num-three','sadasfghjkcbn')
        four_pro.submit_vote()
        four_pro.con_and_theme()