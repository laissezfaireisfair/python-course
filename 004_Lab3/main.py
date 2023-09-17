import uuid


class Employee:
    def __init__(self, name: str, identifier: uuid):
        self.name: str = name
        self.balance: float = 0.
        self.identifier: uuid = identifier

    def take_salary(self, amount: float):
        self.balance += amount

    def do_work(self):
        raise Exception('Abstract employee cannot do work')

    def print_balance(self):
        print(f'Balance of {self.name}: {self.balance}')


def read_matrix(file_name: str) -> [[int]]:
    fin = open(file_name, 'r')
    lines = fin.readlines()
    matrix = [[int(num) for num in line.split(' ')] for line in lines]
    fin.close()
    return matrix


def write_matrix(matrix: [[int]]):
    lines = [' '.join([str(digit) for digit in line]) for line in matrix]
    text = '\n'.join(lines)
    print(text)


def read_matrices() -> ([[int]], [[int]]):
    print('File name 1: ')
    filename1 = input()
    print('File name 2: ')
    filename2 = input()
    matrix1 = read_matrix(filename1)
    matrix2 = read_matrix(filename2)
    return matrix1, matrix2


class Pupa(Employee):
    def __init__(self, name: str, identifier: uuid):
        super().__init__(name, identifier)

    def do_work(self):
        print(f'Pupa {self.name} starting to work...')
        matrix1, matrix2 = read_matrices()
        matrix_sum = []
        for i in range(len(matrix1)):
            matrix_sum.append([])
            for j in range(len(matrix1[0])):
                matrix_sum[i].append(matrix1[i][j] + matrix2[i][j])
        write_matrix(matrix_sum)


class Lupa(Employee):
    def __init__(self, name: str, identifier: uuid):
        super().__init__(name, identifier)

    def do_work(self):
        print(f'Lupa {self.name} starting to work...')
        matrix1, matrix2 = read_matrices()
        matrix_sum = []
        for i in range(len(matrix1)):
            matrix_sum.append([])
            for j in range(len(matrix1[0])):
                matrix_sum[i].append(matrix1[i][j] - matrix2[i][j])
        write_matrix(matrix_sum)


class EmployeeFactory:
    @staticmethod
    def create_employee(employee_type: str, name: str) -> Employee:
        identifier: uuid = uuid.uuid4()

        if employee_type.lower() == 'pupa':
            employee = Pupa(name, identifier)
        elif employee_type.lower() == 'lupa':
            employee = Lupa(name, identifier)
        elif employee_type.lower() == 'accountant':
            employee = Accountant(name, identifier)
        else:
            raise Exception('Unknown employee type')

        return employee


class EmploymentManager:
    employee_by_id = {}
    grade_by_employee_id = {}

    @staticmethod
    def employ(employee: Employee, salary: float):
        EmploymentManager.employee_by_id[employee.identifier] = employee
        EmploymentManager.grade_by_employee_id[employee.identifier] = salary

    @staticmethod
    def get_employee(employee_id: uuid):
        return EmploymentManager.employee_by_id[employee_id]

    @staticmethod
    def get_all_employees():
        return [e for e in EmploymentManager.employee_by_id.values()]

    @staticmethod
    def get_grade(employee_id: uuid):
        return EmploymentManager.grade_by_employee_id[employee_id]


class Accountant(Employee):
    def __init__(self, name: str, identifier: uuid):
        super().__init__(name, identifier)
        self.authorised_transactions = []

    def give_salary(self, employee_id: uuid):
        employee = EmploymentManager.get_employee(employee_id)
        grade = EmploymentManager.get_grade(employee_id)
        employee.take_salary(grade)
        self.authorised_transactions.append((employee_id, grade))

    def do_work(self):
        print('Accountant starting to work...')
        for employee in EmploymentManager.get_all_employees():
            self.give_salary(employee.identifier)


def main():
    pupa1 = EmployeeFactory.create_employee('pupa', 'pupa1')
    EmploymentManager.employ(pupa1, 228)
    lupa1 = EmployeeFactory.create_employee('lupa', 'lupa1')
    EmploymentManager.employ(lupa1, 282)

    accountant1 = EmployeeFactory.create_employee('accountant', 'accountant1')
    EmploymentManager.employ(accountant1, 1337)

    for employee in EmploymentManager.get_all_employees():
        employee.do_work()

    for employee in EmploymentManager.get_all_employees():
        employee.print_balance()


main()
