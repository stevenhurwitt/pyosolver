import pprint
import json
import time
import sys
import os

base = os.getcwd()
pp = pprint.PrettyPrinter(indent = 1)
print("imported modules.")

def test():
    print("test")
    assert True

def read_file(filename):

    with open(filename, "r") as f:
        file = json.load(f)
        f.close()
        print("read file: " + filename)

    assert str(type(file)) == "<class 'dict'>"

def main():

    test()

    read_file("creds.json")

    print("ran tests successfully.")

if __name__ == "__main__":
    # get start time
    print("running main...")
    start = time.time()

    # run main
    main()

    # get end time
    print("done.")
    end = time.time()
    diff = (end - start)
    print("ran in {} seconds.".format(diff*1000))

    # sys.exit(0)
    sys.exit(0)