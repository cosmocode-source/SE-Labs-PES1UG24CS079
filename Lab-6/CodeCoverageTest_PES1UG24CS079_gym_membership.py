import pytest

from gym_membership import bmi_category, can_enter, membership_cost


def test_monthly_plan_cost():
    assert membership_cost("monthly", 30, False, False) == 1500


def test_quarterly_plan_cost():
    assert membership_cost("quarterly", 30, False, False) == 4000


def test_yearly_plan_cost():
    assert membership_cost("yearly", 30, False, False) == 12000


def test_unknown_plan_raises_error():
    with pytest.raises(ValueError, match="unknown plan"):
        membership_cost("weekly", 30, False, False)


def test_age_below_minimum_raises_error():
    with pytest.raises(ValueError, match="too young"):
        membership_cost("monthly", 13, False, False)


def test_senior_discount():
    assert membership_cost("monthly", 60, False, False) == 1125


def test_student_discount():
    assert membership_cost("monthly", 30, True, False) == 1350


def test_trainer_add_on():
    assert membership_cost("monthly", 30, False, True) == 3500


def test_yearly_trainer_discount():
    assert membership_cost("yearly", 30, False, True) == 13500


def test_plan_active_during_regular_hours():
    assert can_enter(10, True, False, "M") is True


def test_inactive_plan_denies_entry():
    assert can_enter(10, False, False, "M") is False


def test_entry_before_opening_time_is_denied():
    assert can_enter(4, True, False, "M") is False


def test_entry_after_closing_time_is_denied():
    assert can_enter(23, True, False, "M") is False


def test_female_entry_during_women_only_slot():
    assert can_enter(10, True, True, "F") is True


def test_male_entry_during_women_only_slot():
    assert can_enter(10, True, True, "M") is False


def test_invalid_height_raises_error():
    with pytest.raises(ValueError, match="invalid height"):
        bmi_category(70, 0)


def test_underweight_bmi_category():
    assert bmi_category(45, 1.7) == "underweight"


def test_normal_bmi_category():
    assert bmi_category(68, 1.7) == "normal"


def test_overweight_bmi_category():
    assert bmi_category(80, 1.7) == "overweight"


def test_obese_bmi_category():
    assert bmi_category(100, 1.7) == "obese"
