
from people import get_employees
from salary import calculate_salary
from datetime import datetime

if __name__ == '__main__':
    print(datetime.now())
    get_employees()
    calculate_salary()