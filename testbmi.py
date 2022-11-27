import testing as bmi

def test_bmi_normal_weight():
    bmirange= bmi.calculate_bmi(1.73, 66)

    assert  (bmirange==0)

def test_bmi_under_weight():
    bmirange= bmi.calculate_bmi(1.73, 20)

    assert  (bmirange==-1)

def test_bmi_over_weight():
    bmirange= bmi.calculate_bmi(1.73, 100)
    assert  (bmirange==1)
