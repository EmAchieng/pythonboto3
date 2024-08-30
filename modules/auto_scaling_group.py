import boto3

def create_launch_configuration(launch_configuration_name, ami_id, instance_type, key_name):
    """
    Creates a launch configuration for auto-scaling groups.

    :param launch_configuration_name: Name of the launch configuration.
    :param ami_id: ID of the AMI to use for the instances.
    :param instance_type: Type of instance to launch.
    :param key_name: Name of the key pair to use for SSH access.
    """
    asg_client = boto3.client('autoscaling')
    response = asg_client.create_launch_configuration(
        LaunchConfigurationName=launch_configuration_name,
        ImageId=ami_id,
        InstanceType=instance_type,
        KeyName=key_name
    )
    print(f"Launch Configuration created with Name: {launch_configuration_name}")

def create_auto_scaling_group(auto_scaling_group_name, launch_configuration_name, min_size, max_size, vpc_zone_identifier):
    """
    Creates an auto-scaling group with the specified configuration.

    :param auto_scaling_group_name: Name of the auto-scaling group.
    :param launch_configuration_name: Name of the launch configuration to use.
    :param min_size: Minimum number of instances in the group.
    :param max_size: Maximum number of instances in the group.
    :param vpc_zone_identifier: Comma-separated list of subnet IDs for the auto-scaling group.
    """
    asg_client = boto3.client('autoscaling')
    response = asg_client.create_auto_scaling_group(
        AutoScalingGroupName=auto_scaling_group_name,
        LaunchConfigurationName=launch_configuration_name,
        MinSize=min_size,
        MaxSize=max_size,
        VPCZoneIdentifier=vpc_zone_identifier
    )
    print(f"Auto Scaling Group created with Name: {auto_scaling_group_name}")
