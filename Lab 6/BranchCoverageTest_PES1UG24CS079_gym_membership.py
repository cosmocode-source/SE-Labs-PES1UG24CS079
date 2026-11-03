import pytest

from gym_membership import bmi_category, can_enter, membership_cost


def test_unknown_plan_branch():
    with pytest.raises(ValueError, match="unknown plan"):
        membership_cost("weekly", 30, False, False)


def test_age_too_young_branch():
    with pytest.raises(ValueError, match="too young"):
        membership_cost("monthly", 13, False, False)


def test_regular_non_student_non_senior_branch():
    assert membership_cost("monthly", 30, False, False) == 1500


def test_senior_discount_branch():
    assert membership_cost("monthly", 60, False, False) == 1125


def test_student_discount_branch():
    assert membership_cost("quarterly", 30, True, False) == 3600


def test_trainer_true_non_yearly_branch():
    assert membership_cost("monthly", 30, False, True) == 3500


def test_trainer_false_branch():
    assert membership_cost("yearly", 30, False, False) == 12000


def test_yearly_trainer_discount_branch():
    assert membership_cost("yearly", 30, False, True) == 13500


def test_inactive_plan_branch():
    assert can_enter(10, False, False, "M") is False


def test_hour_before_opening_branch():
    assert can_enter(4, True, False, "M") is False


def test_hour_after_closing_branch():
    assert can_enter(23, True, False, "M") is False


def test_regular_entry_branch():
    assert can_enter(10, True, False, "M") is True


def test_women_only_female_branch():
    assert can_enter(10, True, True, "F") is True


def test_women_only_non_female_branch():
    assert can_enter(10, True, True, "M") is False


def test_invalid_height_branch():
    with pytest.raises(ValueError, match="invalid height"):
        bmi_category(70, 0)


def test_underweight_branch():
    assert bmi_category(45, 1.7) == "underweight"


def test_normal_bmi_branch():
    assert bmi_category(68, 1.7) == "normal"


def test_overweight_branch():
    assert bmi_category(80, 1.7) == "overweight"


def test_obese_branch():
    assert bmi_category(100, 1.7) == "obese"


def test_boundary_values_branch():
    assert can_enter(5, True, False, "F") is True
