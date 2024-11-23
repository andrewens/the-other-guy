from tests import main_test

tests_directory_name = "tests"
test_modules = [
    main_test, # test 0
]

def print_test_summary(failed_tests, passed_tests):
    tests_string1 = "test" if failed_tests == 1 else "tests"
    tests_string2 = "test" if passed_tests == 1 else "tests"
    
    print(f"{failed_tests} {tests_string1} failed; {passed_tests} {tests_string2} passed")

    if failed_tests <= 0:
        print("All tests passed!")
    

def run():
    failed_tests = 0
    passed_tests = 0
    
    for i in range(len(test_modules)):
        test = test_modules[i]
        try:
            test.run()
            passed_tests += 1

        except Exception as e:
            failed_tests += 1
            print(f"Test #{i} threw exception: {e}")

    print_test_summary(failed_tests, passed_tests)
