from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass


class Intern(Employee):
    def calculate_salary(self):
        return 15000


class FullTimeEmployee(Employee):
    def calculate_salary(self):
        return 50000


class ContractEmployee(Employee):
    def calculate_salary(self):
        return 30000


intern = Intern()
fulltime = FullTimeEmployee()
contract = ContractEmployee()

print("Intern Salary:", intern.calculate_salary())
print("Full-Time Employee Salary:", fulltime.calculate_salary())
print("Contract Employee Salary:", contract.calculate_salary())