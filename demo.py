import unittest
import json
from apitest import RunMain
from BeautifulReport import BeautifulReport
class TestRun(unittest.TestCase):
    def setUp(self) -> None:
        self.run_main1 = RunMain()

    def test_01(self):
        url = "http://106.75.9.19:88/active/get_info"
        params = {"pid": "1"}
        res = self.run_main1.run_main("get", url,params)
        print(res)
        print(type(res))
        self.assertIn('"code": "0"',res)
if __name__=="__main__":
    suite = unittest.TestCase
    suite.addTest(TestRun('test_01'))
    unittest.TextTestRunner().run((suite))
