import Lab2.bmi as BMI

def test_calc_bmi_underweight():
    expected = -1
    result=BMI.calculate_bmi(weight=35.0,height=1.80)
    assert (expected == result)

def test_calc_bmi_normalweight():
    expected = 0
    result=BMI.calculate_bmi(weight=60.0,height=1.80)
    assert (expected == result)

def test_calc_bmi_overweight():
    expected = 1
    result=BMI.calculate_bmi(weight=95.0,height=1.80)
    assert (expected == result)