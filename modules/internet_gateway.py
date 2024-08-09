"""An internet gateway attached to VPC."""

import boto3

def create_internet_gateway(vpc_id):
    ec2_client = boto3.client('ec2')
    response = ec2_client.create_internet_gateway()
    igw_id = response['InternetGateway']['InternetGatewayId']
    ec2_client.attach_internet_gateway(InternetGatewayId=igw_id, VpcId=vpc_id)
    print(f"Internet Gateway created with ID: {igw_id}")
    return igw_id
