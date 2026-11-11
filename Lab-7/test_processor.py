import math

import pytest
from hypothesis import given, strategies as st

from processor import membership_cost, can_enter, bmi_category


PLANS = ["monthly", "quarterly", "yearly"]


# 1. membership_cost()


@given(
    plan=st.sampled_from(PLANS),
    age=st.integers(min_value=14, max_value=100),
    is_student=st.booleans(),
    with_trainer=st.booleans(),
)
def test_membership_cost_returns_non_negative_integer(
    plan, age, is_student, with_trainer
):
    result = membership_cost(plan, age, is_student, with_trainer)
    assert isinstance(result, int)
    assert result >= 0


@given(plan=st.text().filter(lambda value: value not in PLANS))
def test_membership_cost_rejects_unknown_plan(plan):
    with pytest.raises(ValueError):
        membership_cost(plan, 25, False, False)


@given(age=st.one_of(st.none(), st.text(), st.floats(allow_nan=True, allow_infinity=True)))
def test_membership_cost_rejects_invalid_age_type(age):
    with pytest.raises((TypeError, ValueError)):
        membership_cost("monthly", age, False, False)


# 2. can_enter()


@given(
    hour=st.integers(min_value=0, max_value=23),
    plan_active=st.booleans(),
    is_women_only_slot=st.booleans(),
    gender=st.sampled_from(["F", "M"]),
)
def test_can_enter_returns_boolean(hour, plan_active, is_women_only_slot, gender):
    result = can_enter(hour, plan_active, is_women_only_slot, gender)
    assert isinstance(result, bool)


@given(hour=st.integers(max_value=4))
def test_can_enter_denies_hours_before_opening(hour):
    assert can_enter(hour, True, False, "M") is False


@given(hour=st.integers(min_value=23))
def test_can_enter_denies_hours_after_closing(hour):
    assert can_enter(hour, True, False, "M") is False


@given(hour=st.text())
def test_can_enter_rejects_non_numeric_hour(hour):
    with pytest.raises((TypeError, ValueError)):
        can_enter(hour, True, False, "M")


# 3. bmi_category()


@given(
    weight=st.floats(min_value=0.1, max_value=300, allow_nan=False, allow_infinity=False),
    height=st.floats(min_value=0.5, max_value=2.5, allow_nan=False, allow_infinity=False),
)
def test_bmi_category_returns_valid_category(weight, height):
    result = bmi_category(weight, height)
    assert result in {"underweight", "normal", "overweight", "obese"}


@given(height=st.floats(max_value=0, allow_nan=False, allow_infinity=False))
def test_bmi_category_rejects_non_positive_height(height):
    with pytest.raises(ValueError):
        bmi_category(60, height)


@given(weight=st.floats(max_value=0, allow_nan=False, allow_infinity=False))
def test_bmi_category_rejects_non_positive_weight(weight):
    with pytest.raises(ValueError):
        bmi_category(weight, 1.7)


@pytest.mark.parametrize(
    "weight,height",
    [
        (float("nan"), 1.7),
        (60, float("nan")),
        (float("inf"), 1.7),
        (60, float("inf")),
    ],
)
def test_bmi_category_rejects_non_finite_values(weight, height):
    with pytest.raises(ValueError):
        bmi_category(weight, height)
