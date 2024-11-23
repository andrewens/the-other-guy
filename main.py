import config
import test_runner


def main():
    if config.testing_mode:
        test_runner.run()

    # insert code for the main experiment here
    print("Main!")


main()
