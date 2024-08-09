"""
Create a security group and authorizing ingress rules 
"""

import boto3

def create_security_group(vpc_id, group_name, description):
    ec2_client = boto3.client('ec2')
    response = ec2_client.create_security_group(GroupName=group_name, Description=description, VpcId=vpc_id)
    sg_id = response['GroupId']
    print(f"Security Group created with ID: {sg_id}")
    return sg_id

def authorize_ingress(sg_id, port, protocol, cidr):
    ec2_client = boto3.client('ec2')
    ec2_client.authorize_security_group_ingress(
        GroupId=sg_id,
        IpPermissions=[
            {
                'IpProtocol': protocol,
                'FromPort': port,
                'ToPort': port,
                'IpRanges': [{'CidrIp': cidr}]
            }
        ]
    )
    print(f"Ingress rule added to SG {sg_id} for port {port} from {cidr}")
