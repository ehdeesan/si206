# Your name: Edison Chiu
# Your student id: 52872908
# Your email: edisonc@umich.edu
# List who you worked with on this homework:

#The goal of this homework is to practice basic debugging and get familar with
# Python 3 basics.  It includes work with functions, strings, for-each loop,  
# for loop, range, and conditionals

# Fix errors in the function below.  It should return a password (string)
# created from the first letter of each word in the passed string
# follwed by ! and then the last two digits of the passed year
def create_pass(the_str, year):
    words = the_str.split()
    password = ""
    year = str(year)
    for word in words:
        password = password + word[0]
    password = password + "!" + year[-2:]
    return password

# Testing the create_pass function 
def test_create_pass():
    print("Testing create_pass")
    res = create_pass("Hello world", 2021)
    print("Expected: Hw!21, Actual:", res)
    res = create_pass("Some one stop me", 2020)
    print("Expected: Sosm!20, Actual:", res)
    res = create_pass("Walk", 2019)
    print("Expected: W!19, Actual:", res)
    res = create_pass("Walk 4 Hope", 2019)
    print("Expected: W4H!19, Actual:", res)
    res = create_pass("a b c", 2021)
    print("Expected: abc!21, Actual:", res)

# Fix errors in the function below. It should return a count of the number
# of values less than the passed target value in the passed list nums
def count_lt(target, nums):
    count = 0
    for num in nums:
        if num < target:
            count += 1
    return count

# Testing the count_lt function 
def test_count_lt():
    print("Testing count_lt")
    res = count_lt(3, [0, 1, 2, 3])
    print("Expected: 3, Actual", res)
    res = count_lt(10, [0, 1, 2, 3])
    print("Expected: 4, Actual:", res)
    res = count_lt(2, [0, 1, 2, 3])
    print("Expected: 2, Actual", res)
    res = count_lt(-3, [0, -1, -2, 3])
    print("Expected: 0, Actual", res)
    res = count_lt(10, [])
    print("Expected: 0, Actual:", res)

# Fix errors in the function below.  It should return a total of the values from 0 
# to the specified end (inclusive) when counting by fives (0, 5, 10), etc.
def total_by_fives(end):
    total = 0
    for x in range(0, end+5, 5):
        total += x
    return total

# Testing the total_by_fives function
def test_total_by_fives():
    print("Testing total_by_fives")
    res = total_by_fives(10)
    print("Expected: 15, Actual:", res)
    res = total_by_fives(0)
    print("Expected: 0, Actual:", res)
    res = total_by_fives(15)
    print("Expected: 30, Actual:", res)
    res = total_by_fives(20)
    print("Expected: 50, Actual:", res)
    res = total_by_fives(25)
    print("Expected: 75, Actual:", res)

# Return true if all the values in num_list are positive (> 0) and false otherwise
def check_all_pos(num_list):
    for num in num_list:
        if num <= 0:
            return False
    return True    

# Testing the check_all_pos function
def test_check_all_pos():
    print("Testing check_all_pos")
    res = check_all_pos([1, 2, 3])
    print("Expected: True, Actual:", res)
    res = check_all_pos([1, 3, 0, 2])
    print("Expected: False, Actual:", res)
    res = check_all_pos([3, -1, 5])
    print("Expected: False, Actual:", res)
    res = check_all_pos([-1, 3, 5])
    print("Expected: False, Actual:", res)
    res = check_all_pos([1, 3, -5])
    print("Expected: False, Actual:", res)

# Fix the function below to return the index of the minimum value in the list nums
# or -1 if there aren't any values in the list
def get_index_min(nums):

    if (len(nums) == 0):
        return -1

    min = nums[0]
    min_index = 0
    # loop through the list
    for index in range(len(nums)):
        
        # get the current value
        current = nums[index]

        # if new min
        if current < min:

            # reset min
            min = current
            min_index = index

    return min_index

# Testing the get_index_min function
def test_get_index_min():
    print("Testing get_index_min")
    res = get_index_min([2, -3, 5])
    print("Expected: 1, Actual:", res)
    res = get_index_min([-2, 3, 5])
    print("Expected: 0, Actual:", res)
    res = get_index_min([-2, 3, -5])
    print("Expected: 2, Actual:", res)
    res = get_index_min([1])
    print("Expected: 0, Actual:", res)
    res = get_index_min([89, 20, 14, 4])
    print("Expected: 3, Actual:", res)

# Fix the function below to return 0 if score < 100
# return 1 if score >= 100 and less than 150
# return 2 if score >= 150 and less than 180
# return 3 if score >= 180 and less than 200
# else return 4
def get_group(score):
    group = 0
    if score < 100:
        group = 0
    elif score < 150:
        group = 1
    elif score < 180: 
        group = 2
    elif score < 200:
        group = 3
    else:
        group = 4
    return group

# Test the get_group function
def test_get_group():
    print("Testing get_group")
    res = get_group(99)
    print("Expected: 0, Actual:", res)
    res = get_group(100)
    print("Expected: 1, Actual:", res)
    res = get_group(150)
    print("Expected: 2, Actual:", res)
    res = get_group(180)
    print("Expected: 3, Actual:", res)
    res = get_group(200)
    print("Expected: 4, Actual:", res)


# declare the main method
def main():
    test_create_pass()
    print()
    test_count_lt()
    print()
    test_total_by_fives()
    print()
    test_check_all_pos()
    print()
    test_get_index_min()
    print()
    test_get_group()

# call the main method
main()
