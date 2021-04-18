"""
Unit test file for the methods we wrote
"""
import GlobalVariables as g

# Each test makes sure the defined functions return a valid value (if applicable)
passed = 0
failed = 0
total = 7
failed_test = []


def payroll_tests():
    global passed
    global failed

    # First test doesn't return anything but it's VERY important
    try:
        assert len(g.pr.employees) > 0
        passed += 1
    except AssertionError or IOError:
        failed += 1
        failed_test.append("Payroll.load_employees")

    # Authentication
    try:
        value = g.pr.authenticate("557", "assertion")
        assert value in [False, True, "None"]
        passed += 1
    except AssertionError:
        failed += 1
        failed_test.append("Payroll.authenticate")

    # User Exists
    try:
        value = g.pr.user_exists(123)
        assert value in [False, True]
        passed += 1
    except AssertionError:
        failed += 1
        failed_test.append("Payroll.user_exists")

    # Change Password
    try:
        value = g.pr.change_password("557", 123)
        assert value in ["Fail", False, True]
        passed += 1
    except AssertionError:
        failed += 1
        failed_test.append("Payroll.change_password")

    # Find Employee by ID
    try:
        value = g.pr.find_employee_by_id("123")
        assert value == False
        passed += 1
    except AssertionError:
        failed += 1
        failed_test.append("Payroll.find_employee_by_id")

    """
    Excluded:
    save_profile
    new_user
    write_out
    class_number
    Whoel employee class (we didn't write that)
    process timecards
    process receipts
    run payroll
    """


def user_data_tests():
    global passed
    global failed

    # Access Check
    try:
        g.ud.access_check("557")
        assert g.emp_access in [1, 2, 3]
        passed += 1
    except AssertionError:
        failed += 1
        failed_test.append("UserData.access_check")

    # Get Match
    try:
        value = g.ud.get_match("Nikolai")
        assert len(value) > 0
        passed += 1
    except AssertionError:
        failed += 1
        failed_test.append("UserData.get_match")

    """
    Excluded or not in use:
    new_user
    user_exists
    read_value
    verify_user
    change_field
    """


payroll_tests()
user_data_tests()

print(f"Total Passed: {passed}\n"
      f"Total Failed: {failed}\n"
      f"Total Tests: {total}\n")

if len(failed_test) > 0:
    print(f"Failed Tests are: {failed_test}")
