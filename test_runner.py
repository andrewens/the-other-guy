import os
import importlib

tests_directory_name = "tests"


def print_test_summary(failed_tests, passed_tests):
    tests_string1 = "test" if failed_tests == 1 else "tests"
    tests_string2 = "test" if passed_tests == 1 else "tests"
    
    print(f"\n{failed_tests} {tests_string1} failed; {passed_tests} {tests_string2} passed")

    if failed_tests <= 0:
        print("All tests passed!")
    

def run():
    test_modules = {} # string module_name --> <Module>
    for file_name in os.listdir(tests_directory_name):
        # get python modules
        if "__" in file_name:
            continue
        
        filename_without_extension, _ = os.path.splitext(file_name)
        module = importlib.import_module(tests_directory_name + "." + filename_without_extension)

        test_modules[filename_without_extension] = module

    failed_tests = 0
    passed_tests = 0

    for test_name, test_module in test_modules.items():
        try:
            test_module.run()
            passed_tests += 1

        except Exception as e:
            failed_tests += 1
            print(f"Test '{test_name}' threw exception: {e}")

    print_test_summary(failed_tests, passed_tests)
