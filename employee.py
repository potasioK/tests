class Employee:
    """Accepts and stores employee information with the ability to update with pay raises."""
    
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
                
    #def employee_data(self):
        #self.data = f"{self.first_name.title()} {self.last_name.title()}, Annual salary: {self.annual_salary}"
        #print(self.data)
        
    def give_raise(self, pay_raise=5000):
        self.annual_salary += pay_raise
        #print(self.data)
        
        