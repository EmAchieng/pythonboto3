"""
VPC with the specified CIDR block
"""
import boto3

def create_vpc(cidr_block):
    ec2_client = boto3.client('ec2')
    response = ec2_client.create_vpc(CidrBlock=cidr_block)
    vpc_id = response['Vpc']['VpcId']
    ec2_client.get_waiter('vpc_available').wait(VpcIds=[vpc_id])
    print(f"VPC created with ID: {vpc_id}")
    return vpc_id
