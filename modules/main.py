"""
Set up infrastructure components including VPC, subnet, internet gateway,
security group, and an EC2 instance with Nginx
"""

import time
import vpc
import subnet
import internet_gateway
import security_group
import ec2_instance

if __name__ == "__main__":
    # VPC
    vpc_id = vpc.create_vpc("10.0.0.0/16")

    #  Subnet
    public_subnet_id = subnet.create_subnet(vpc_id, "10.0.1.0/24", "eu-central-2a")

    #  Internet Gateway
    igw_id = internet_gateway.create_internet_gateway(vpc_id)

    # Security Group
    sg_id = security_group.create_security_group(vpc_id, "nginx-sg", "Security group for Nginx")
    security_group.authorize_ingress(sg_id, 80, "tcp", "0.0.0.0/0")

    # EC2 Instance with Nginx
    ami_id = os.getenv("AMI_ID")
    instance_type = os.getenv("INSTANCE_TYPE")
    key_name = os.getenv("KEY_NAME")
    instance_id = ec2_instance.create_ec2_instance(ami_id, instance_type, key_name, public_subnet_id, sg_id)

    # Public IP of the Instance
    public_ip = ec2_instance.get_instance_public_ip(instance_id)
    print(f"EC2 Instance Public IP: {public_ip}")
    
    # Print
    print("Setup complete.")
    print(f"You can access Nginx at http://{public_ip}/")
    print("Hello World from Nginx")
