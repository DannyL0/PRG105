class Employee:
    def __init__(self, name, number):
        self.employee_name = name
        self.employee_number = number

    def set_name(self, name):
        self.employee_name = name

    def set_number(self, numbers):
        self.employee_number = numbers

    def get_name(self):
        return self.employee_name

    def get_number(self):
        return self.employee_number


class ProductionWorker(Employee):
    def __init__(self, name, number, shift, pay_rate):
        Employee.__init__(self, name, number)
        self.shift = shift
        self.pay_rate = pay_rate

    def __str__(self):
        return f"\nName: {self.employee_name}\n" \
               f"Employee Number: {self.employee_number}\n" \
               f"Shift: {self.shift}\n" \
               f"Hourly Pay Rate: ${self.pay_rate:.2f}\n"
