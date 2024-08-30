import boto3

def create_route_table(vpc_id):
    """
    Creates a route table in the specified VPC.

    :param vpc_id: ID of the VPC where the route table will be created.
    :return: The ID of the created route table.
    """
    ec2_client = boto3.client('ec2')
    response = ec2_client.create_route_table(VpcId=vpc_id)
    route_table_id = response['RouteTable']['RouteTableId']
    print(f"Route Table created with ID: {route_table_id}")
    return route_table_id

def associate_route_table(route_table_id, subnet_id):
    """
    Associates a route table with a subnet.

    :param route_table_id: ID of the route table to associate.
    :param subnet_id: ID of the subnet to associate the route table with.
    :return: The association ID of the route table with the subnet.
    """
    ec2_client = boto3.client('ec2')
    response = ec2_client.associate_route_table(RouteTableId=route_table_id, SubnetId=subnet_id)
    association_id = response['AssociationId']
    print(f"Route Table {route_table_id} associated with Subnet {subnet_id}. Association ID: {association_id}")
    return association_id
