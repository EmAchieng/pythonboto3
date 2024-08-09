"""
a subnet within a specified VPC, using the provided CIDR block and availability zone.
"""

import boto3

def create_subnet(vpc_id, cidr_block, availability_zone):
    ec2_client = boto3.client('ec2')
    response = ec2_client.create_subnet(VpcId=vpc_id, CidrBlock=cidr_block, AvailabilityZone=availability_zone)
    subnet_id = response['Subnet']['SubnetId']
    ec2_client.get_waiter('subnet_available').wait(SubnetIds=[subnet_id])
    print(f"Subnet created with ID: {subnet_id} in AZ: {availability_zone}")
    return subnet_id
