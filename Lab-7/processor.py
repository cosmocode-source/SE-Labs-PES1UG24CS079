
import math

PLAN_PRICE = {
    "monthly": 1500,
    "quarterly": 4000,
    "yearly": 12000
}


# Function 1: Calculate membership cost
def membership_cost(plan, age, is_student, with_trainer):

    # Validate membership plan
    if not isinstance(plan, str) or plan not in PLAN_PRICE:
        raise ValueError("unknown plan")

    # Validate age
    if type(age) is not int:
        raise TypeError("age must be an integer")

    if age < 14:
        raise ValueError("too young")

    # Validate boolean inputs
    if type(is_student) is not bool:
        raise TypeError("is_student must be a boolean")

    if type(with_trainer) is not bool:
        raise TypeError("with_trainer must be a boolean")

    cost = PLAN_PRICE[plan]

    # Apply age/student discount
    if age >= 60:
        cost -= cost // 4
    elif is_student:
        cost -= cost // 10

    # Add trainer charges
    if with_trainer:
        cost += 2000

        if plan == "yearly":
            cost -= 500

    return cost


# Function 2: Check gym entry eligibility

def can_enter(hour, plan_active, is_women_only_slot, gender):

    # Validate input types
    if type(hour) is not int:
        raise TypeError("hour must be an integer")

    if type(plan_active) is not bool:
        raise TypeError("plan_active must be a boolean")

    if type(is_women_only_slot) is not bool:
        raise TypeError("is_women_only_slot must be a boolean")

    if not isinstance(gender, str):
        raise TypeError("gender must be a string")

    # Check membership status
    if not plan_active:
        return False

    # Check gym operating hours
    if hour < 5 or hour > 22:
        return False

    # Check women-only slot
    if is_women_only_slot:
        return gender == "F"

    return True



# Function 3: Calculate BMI category
def bmi_category(weight_kg, height_m):

    # Validate numeric inputs
    for name, value in [
        ("weight", weight_kg),
        ("height", height_m)
    ]:

        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError(f"{name} must be a number")

        if not math.isfinite(value):
            raise ValueError(f"{name} must be finite")

    # Validate weight and height
    if weight_kg <= 0:
        raise ValueError("invalid weight")

    if height_m <= 0:
        raise ValueError("invalid height")

    bmi = weight_kg / (height_m * height_m)

    if bmi < 18.5:
        return "underweight"

    elif bmi < 25:
        return "normal"

    elif bmi < 30:
        return "overweight"

    return "obese"


# Demonstration
if __name__ == "__main__":

    print("Gym Membership System")
    print("---------------------")

    print(
        "Monthly membership:",
        membership_cost("monthly", 25, False, False)
    )

    print(
        "Entry allowed:",
        can_enter(10, True, False, "M")
    )

    print(
        "BMI category:",
        bmi_category(70, 1.75)
    )
