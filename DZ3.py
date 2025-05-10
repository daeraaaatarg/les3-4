#task 5 Department

class Employee:
    def __init__(self, name, job, salary):
        self.name = name
        self.job = job
        self.salary = salary

class Department:
    def __init__(self):
        self.employees = []

    def add_emp(self, *args):
        for employee in args:
            self.employees.append(employee)

    def print_emp_names(self):
        if self.employees != []:
            print(f"Names of employees")
            print("==========================================")
            for employee in self.employees:
                print(f"Employee name: {employee.name}")
                print(f"Employee's job: {employee.job}")
                print(f"Employee's salary: ${employee.salary}")
                print("==========================================")
        else:
            print(f"There's no employees")

one = Employee("Adam", "Lawyer", 15000)
two = Employee("Ian", "Programmer", 20000)
three = Employee("Winston", "Developer", 25000)
gen_sal = one.salary + two.salary + three.salary
dep = Department()
dep.add_emp(one, two, three)
dep.print_emp_names()
print(f"General salary: ${gen_sal}")
