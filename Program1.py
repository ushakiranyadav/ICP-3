# Created Employee class with name, family, salary and department
class Employee:

    # declared a data member to count the number of Employees
    no_of_employees = 0

    # constructor to initialize the object's attributes
    def __init__(self, name, family_name, salary, department):
        self.__name = name
        self.__family_name = family_name
        self.salary = salary
        self.__department = department
        Employee.no_of_employees += 1

    # declared average_salary function to return average salary 
    def average_salary(employees):
        """
        function to average salary
        """
        sum = 0
        for employee in employees:
            sum += employee.salary
        return sum / Employee.no_of_employees

# Created a Fulltime Employee class and inherited the properties of Employee class
class FulltimeEmployee(Employee):
    """
    Full Time Employee is a sub class of Employee
    """

    def __init__(self, name, family_name, salary, department):
        super().__init__(name, family_name, salary, department)

    def full_time_member(self):
        print("Calling FulltimeEmployee member function.")

# Created the instances of Fulltime Employee class and Employee class and calling their member functions.
def main():
    employees = []
    ftEmployee1 = FulltimeEmployee("Vamshi", "Ponugoti", 140000, "Software Engineering")
    ftEmployee1.full_time_member()
    employees.append(ftEmployee1)
    ftEmployee2 = FulltimeEmployee("Micheal", "Velayudham", 170000, "Cyber Security")
    employees.append(ftEmployee2)
    employee1 = Employee("CoseC", "Pacchipulsula", 150000, "Testing")
    employees.append(employee1)
    employee2 = Employee("VeeraSimhaReddy", "Nandamuri", 192000, "Product Manager")
    employees.append(employee2)
    print("Average salary:", FulltimeEmployee.average_salary(employees))
    print("total no of employees:",Employee.no_of_employees)

# declared this method to execute code When the file runs as a script.
if __name__ == "__main__":
    main()