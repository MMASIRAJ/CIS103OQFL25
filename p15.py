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

class developer(employee):
    raise_amt = 1.10
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class manager(employee):
    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def rem_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('-->', emp.fullname())


    
dev_1 = developer('Corey', 'Schafer', 50000, 'python')
dev_2 = developer('test', 'user', 60000, 'Java')

mgr1 = manager('sue', 'smith', 90000, [dev_1])
mgr1.add_emp(dev_2)
mgr1.print_emp()



