import boto3
from pprint import pprint
from os import getenv

dry_run = getenv("DRY_RUN", "True") in (True, "True")


def lambda_handler(event=None, context=None):
    ec2 = boto3.resource("ec2")

    instances = ec2.instances.filter(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

    for instance in instances:
        pprint(instance.terminate(InstanceIds=[instance.id], DryRun=dry_run))


if __name__ == "__main__":
    lambda_handler()
