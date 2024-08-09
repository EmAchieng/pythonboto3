import boto3
import time

"""
1. Creating ec2 instance
2. Returns the instance ID.
"""

def create_ec2_instance(ami_id, instance_type, key_name, subnet_id, sg_id):
    ec2_client = boto3.client('ec2')
    response = ec2_client.run_instances(
        ImageId=ami_id,
        InstanceType=instance_type,
        KeyName=key_name,
        SubnetId=subnet_id,
        SecurityGroupIds=[sg_id],
        MinCount=1,
        MaxCount=1,
        UserData='''#!/bin/bash
                    yum update -y
                    amazon-linux-extras install nginx1 -y
                    systemctl start nginx
                    systemctl enable nginx
                    echo "Hello World" > /usr/share/nginx/html/index.html
                    ''',
        InstanceInitiatedShutdownBehavior='terminate',  
    )
    instance_id = response['Instances'][0]['InstanceId']
    print(f"EC2 Instance created with ID: {instance_id}")
    return instance_id

"""
Retrieve and wait for the public IP address of an EC2 instance identified by instance_id.
"""
def get_instance_public_ip(instance_id, max_wait_time=600, poll_interval=10):
    ec2_client = boto3.client('ec2')
    start_time = time.time()
    elapsed_time = 0

    while elapsed_time < max_wait_time:
        try:
            instance = ec2_client.describe_instances(InstanceIds=[instance_id])['Reservations'][0]['Instances'][0]
            public_ip = instance.get("PublicIpAddress")
            if public_ip:
                print(f"EC2 Instance obtained Public IP: {public_ip}")
                return public_ip
        except (IndexError, KeyError) as e:
            print(f"Error: {e}. Retrying...")
        
        time.sleep(poll_interval)
        elapsed_time = time.time() - start_time

    raise RuntimeError(f"Instance did not acquire a Public IP within {max_wait_time} seconds.")
    