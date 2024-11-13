import employee_info as EI
from employee_info import employee_data as EMPDATA

def test_get_employees_by_age_range():
    upper = 36
    lower = 29
    expected = [EMPDATA[0], EMPDATA[3], EMPDATA[4]]
    result = EI.get_employees_by_age_range(lower, upper)
    assert (result == expected)


def test_calculate_average_salary():
    expected = 60166.67
    result = EI.calculate_average_salary()
    assert (result == expected)

def test_get_employees_by_dept():
    targetDept = "Sales"
    expected = [EMPDATA[0], EMPDATA[5]]
    result = EI.get_employees_by_dept(targetDept)
    assert (result == expected)