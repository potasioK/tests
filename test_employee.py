import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for 'employee.py'."""
    
    def setUp(self):
        """Creates employee data and raises for use in future tests."""
        self.employee1 = Employee("Roger", "Rabbit", 9000)
        #self.data = Employee.employee_data(self)
        
        
    def test_give_default_raise(self):
        """Test that $5000 raise stores properly."""
        #self.employee1
        self.employee1.give_raise()
        self.assertEqual(self.employee1.annual_salary, 14000)
        
        
        
    def test_give_custom_raise(self):
        """Test that custom raise amount stores properly."""
        #self.employee1
        self.employee1.give_raise(pay_raise=3200)
        self.assertEqual(self.employee1.annual_salary, 12200)
        
if __name__ == '__main__':
    unittest.main()
    
