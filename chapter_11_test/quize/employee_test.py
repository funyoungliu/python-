import unittest
from employee_class import Employee
class TestEmployee(unittest.TestCase):
    """employee的测试类"""
    def setUp(self):
        """创建一个employee的类"""
        self.myemployee=Employee('单建昌',22,4000)
        self.add=3000
    def test_wage_add(self):
        """测试默认增加值"""
        self.myemployee.give_raise()
        self.assertEqual(9000,self.myemployee.wage)
    def test_wage_add_adjust(self):
        """测试自设值"""
        self.myemployee.give_raise(4000)
        self.assertEqual(8000,self.myemployee.wage)
unittest.main()