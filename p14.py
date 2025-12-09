class employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self,first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        employee.num_of_emps += 1

    def fullname(self):
        print(self.first, self.last)
        return

    def apply_raise(self):
        self.pay = float(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday == 6:
            return False
        return True
    
emp_1 = employee('Corey', 'Schafer', 50000)
emp_2 = employee('test', 'user', 60000)

import datetime
my_date = datetime.date(2025, 10, 29)

print(employee.is_workday(my_date))


