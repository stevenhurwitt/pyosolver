import pprint
import boto3
import json
import time
import sys
import os

base = os.getcwd()
pp = pprint.PrettyPrinter(indent = 1)
print("imported modules.")

def test():

    # open creds.json, access aws secretsmanager
    filename = "creds.json"
    secrets = boto3.client("secretsmanager", region_name = "us-east-2")
    os.environ["subreddit"] = "technology"
    subreddit = os.environ["subreddit"]
    print("subreddit: " + subreddit)

    # aws access key & secret key
    os.environ["AWS_ACCESS_KEY_ID"] = secrets.get_secret_value(SecretId = "AWS_ACCESS_KEY_ID")["SecretString"]
    os.environ["AWS_SECRET_ACCESS_KEY"] = secrets.get_secret_value(SecretId = "AWS_SECRET_ACCESS_KEY")["SecretString"]
    with open("creds.json", "r") as f:
        creds = json.load(f)
        pp.pprint(creds)
        f.close()

    # get file
    with open(filename, "r") as f:
        file = json.load(f)
        pp.pprint(file)
        f.close()
    print("read file: " + filename)
    assert len(filename) > 0

if __name__ == "__main__":
    # get start time
    print("running main...")
    start = time.time()

    # run main
    test()

    # get end time
    print("done.")
    end = time.time()
    diff = (end - start)
    print("ran in {} seconds.".format(diff*1000))

    # sys.exit(0)
    sys.exit(0)