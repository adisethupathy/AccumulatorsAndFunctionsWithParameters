"""
This module demonstrates and practices:
  -- using ARGUMENTs in function CALLs,
  -- having PARAMETERs in function DEFINITIONs, and
  -- RETURNING a value from a function,
        possibly CAPTURING the RETURNED VALUE in a VARIABLE.
  -- UNIT TESTING.

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Adi Sethupathy.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import m3t_tester


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_sum_of_digits()
    run_test_digits_in_cube()
    run_test_digits_in_power()
    run_test_fancy_sums_of_digits()

    # ------------------------------------------------------------------
    # DONE: 9. DO THIS LAST!
    #    -- Uncomment the line of code below to run the main function in m3t_tester.py (do not make changes to it).
    #         It runs OUR tests on your code.
    #    -- Check to see whether all test cases indicate they
    #          "COMPLETED SUCCESSFULLY!"
    #    -- If your code fails any of OUR tests but passes YOUR tests,
    #         then you are likely not TESTING the methods correctly.
    #       ** Ask a TA or your professor for help in that case. **
    # ------------------------------------------------------------------

    m3t_tester.main()


def run_test_sum_of_digits():
    """ Tests the  sum_of_digits   function. """
    # ------------------------------------------------------------------
    # DONE: 2. Implement this TEST function, as follows:
    #
    #  Step 1:  This TEST function tests the  sum_of_digits  function.
    #    So read the doc-string of the  sum_of_digits  function
    #    defined below.  Be sure that you understand from the
    #    doc-string what the  sum_of_digits  function SHOULD return.
    #
    #  Step 2:  Pick a test case:  a number that you could send as
    #    an actual argument to the  sum_of_digits  function.
    #      - For example, you could pick the test case  826.
    #
    #  Step 3: Figure out the CORRECT (EXPECTED) answer for your
    #    test case.  In the example of  826  the correct answer
    #    for the sum of its digits is  8 + 2 + 6, which is 16.
    #
    #  Step 4: Write code that prints both the EXPECTED answer
    #    and the ACTUAL answer returned when you call the function.
    #    See the example below.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_of_digits   function:')
    print('--------------------------------------------------')

    # Test 1:
    expected1 = 16
    answer1 = sum_of_digits(826)
    print('Test 1 expected:', expected1)
    print('       actual:  ', answer1)

    # Test 2:
    expected2 = 28
    answer2 = sum_of_digits(1999)

    print('Test 2 expected:', expected2)
    print('actual:', answer2)

    # ------------------------------------------------------------------
    # DONE: 2 (continued).
    # Below this comment, add 3 more test cases of your own choosing.
    # ------------------------------------------------------------------

    # Test 3:
    expected3 = 11
    answer3 = sum_of_digits(2017)

    print('Test 3 expected:', expected3)
    print('actual:', answer3)

    # Test 4:
    expected5 = 22
    answer5 = sum_of_digits(1849)

    print('Test 3 expected:', expected5)
    print('actual:', answer5)

    # Test 5:
    expected6 = 18
    answer6 = sum_of_digits(468)

    print('Test 5 expected:', expected6)
    print('actual:', answer6)


def sum_of_digits(number):
    """
    What comes in:  An integer.
    What goes out:  The sum of the digits in the given integer.
    Side effects:   None.
    Example:
      If the integer is 83135,
      this function returns (8 + 3 + 1 + 3 + 5), which is 20.
    """
    # ------------------------------------------------------------------
    # Students:
    #   Do NOT touch this function - it has no TO DO in it.
    #   Do NOT copy code from this function.
    #
    # Instead, ** CALL ** this function as needed in the other problems.
    #
    # Ask for help if you are unsure what it means to CALL a function.
    # The ONLY part of this function that you need to understand is
    # the doc-string above.  Treat this function as a black box.
    # ------------------------------------------------------------------
    if number < 0:
        number = -number

    digit_sum = 0
    while True:
        if number == 0:
            break
        digit_sum = digit_sum + (number % 10)
        number = number // 10

    return digit_sum


def run_test_digits_in_cube():
    """ Tests the   digits_in_cube   function. """
    # ------------------------------------------------------------------
    # DONE: 3. Implement this function.
    #   It TESTS the  digits_in_cube  function defined below.
    #   Include at least **   3   ** tests.
    #
    # To implement this TEST function, use the same 4 steps as above:
    #
    #   Step 1: Read the doc-string of  digits_in_cube  below.
    #     Understand what that function SHOULD return.
    #
    #   Step 2:  Pick a test case:  a number(s) that you could send as
    #     actual argument(s) to the  digits_in_cube  function.
    #
    #  Step 3: Figure out the CORRECT (EXPECTED) answer for your test case.
    #
    #  Step 4: Write code that prints both the EXPECTED answer
    #    and the ACTUAL answer returned when you call the function.
    #    Follow the same form as in previous examples.
    #
    #   Include at least **   3   ** tests.
    # -----------------------------------------------------------------
    print()
    print('-----------------------------------------------------')
    print('Testing the   digits_in_cube   function:')
    print('-----------------------------------------------------')

    exp1 = 8
    ans1 = digits_in_cube(5)

    print('Test 1 expected:', exp1)
    print('actual:', ans1)

    exp2 = 9
    ans2 = digits_in_cube(3)

    print('Test 2 expected:', exp2)
    print('Actual:', ans2)

    exp3 = 10
    ans3 = digits_in_cube(4)

    print('Test 3 expected:', exp3)
    print('Actual:', ans3)

def digits_in_cube(n):
    """
    What comes in:  A positive integer.
    What goes out:  The sum of the digits in the CUBE of the integer.
    Side effects:   None.
    Example:
      If the integer (n) is 5    (so n cubed is 125),
      this function returns (1 + 2 + 5), which is 8.
    """
    # ------------------------------------------------------------------
    # DONE: 4. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #   That is called TEST-DRIVEN DEVELOPMENT (TDD).
    #
    ####################################################################
    # IMPORTANT: CALL, as many times as needed,
    #    the    sum_of_digits    function that is DEFINED ABOVE.
    ####################################################################
    # ------------------------------------------------------------------

    cubed = n ** 3
    answer = sum_of_digits(cubed)

    return answer

def run_test_digits_in_power():
    """ Tests the   digits_in_power   function. """
    # ------------------------------------------------------------------
    #DONE: 5. Implement this function.
    #   It TESTS the  digits_in_power  function defined below.
    #   Include at least **   3   ** tests.
    #
    # Use the same 4-step process as in implementing the previous TEST functions.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   digits_in_power   function:')
    print('--------------------------------------------------')

    exp1 = 7
    ans1 = digits_in_power(4,2)

    print('Test 1 expected:', exp1)
    print('Actual:', ans1)

    exp2 = 9
    ans2 = digits_in_power(6,2)

    print('Test 2 expected:', exp2)
    print('actual:', ans2)

    exp3 = 13
    ans3 = digits_in_power(7,2)

    print('Test 3 expected:', exp3)
    print('actual:', ans3)

def digits_in_power(n, k):
    """
    What comes in:  Two positive integers, n and k.
    What goes out:
      The sum of the digits in x, where x is n raised to the kth power.
    Side effects:   None.
    Example:
      If the arguments are 12 and 3, respectively,
      this function returns 18
      since 12 to the 3rd power is 1728 (whose digits sum to 18).
    """
    # ------------------------------------------------------------------
    # DONE: 6. Implement and test this function.
    #
    ####################################################################
    # IMPORTANT: CALL, as many times as needed,
    #    the    sum_of_digits    function that is DEFINED ABOVE.
    ####################################################################
    # ------------------------------------------------------------------

    value = n ** k
    answer = sum_of_digits(value)

    return answer


def run_test_fancy_sums_of_digits():
    """ Tests the   fancy_sums_of_digits   function. """
    # ------------------------------------------------------------------
    # DONE: 7. Implement this function.
    #   It TESTS the  fancy_sums_of_digits  function defined below.
    #   Include at least **   3   ** tests.
    #
    # Use the same 4-step process as in implementing the previous
    # TEST functions.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   fancy_sums_of_digits   function:')
    print('--------------------------------------------------')

    exp1 = 1
    ans1 = fancy_sums_of_digits(10)

    print('Test 1 expected:', exp1)
    print('Actual:', ans1)


    exp2 =  19804
    ans2 = fancy_sums_of_digits(2)

    print('Test 2 expected:', exp2)
    print('Actual:', ans2)


    exp3 = 124309
    ans3 = fancy_sums_of_digits(35)

    print('Test 3 expected:', exp3)
    print('Actual:', ans3)


    # ------------------------------------------------------------------
    # HINT:  For your 1st test, consider  n=10.  Figure out BY HAND
    # the correct (expected) answer for that test case.  (It's easy.)
    # The doc-string below gives test cases you can use for
    # your 2nd and 3rd tests but READ THOSE TEST CASES CAREFULLY
    # in the doc-string to be sure that you understand the specification.
    # ------------------------------------------------------------------


def fancy_sums_of_digits(n):
    """
    What comes in:  A positive integer n.
    What goes out:
      -- Let X denote the   sum   of the digits in (n ** 1000).
      -- Let Y denote the   sum   of the digits in (n ** 999).
      This function RETURNs the sum of the digits in (X ** Y).
    Side effects:   None.
    Examples:
      -- If n is 2, then:
            -- the   sum   of the digits in n ** 1000 is 1366 (trust me!).
            -- the   sum   of the digits in n ** 999 is 1367 (trust me!).
            -- so X ** Y is VERY LARGE in this case
                     (don't try to print it!)
            -- the   sum   of the digits in (X ** Y) is 19084 (trust me!)
            -- so this function returns 19084.
      -- If n is 35, then:
            -- the sum of the digits in n ** 1000 is 7021 (trust me!).
            -- the sum of the digits in n ** 999 is 7145 (trust me!).
            -- so X ** Y is VERY LARGE in this case
                     (don't try to print it!)
            -- the sum of the digits in (X ** Y) is 124309 (trust me!)
            -- so this function returns 124309.
    """
    # ------------------------------------------------------------------
    # DONE: 8. Implement and test this function.
    #
    ####################################################################
    # IMPORTANT: CALL, as many times as needed,
    #    the    sum_of_digits    function that is DEFINED ABOVE.
    ####################################################################
    # ------------------------------------------------------------------

    X = sum_of_digits(n ** 1000)
    Y = sum_of_digits(n ** 999)
    answer = sum_of_digits(X ** Y)
    return answer


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# This unusual form is necessary for the special testing we provided.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
