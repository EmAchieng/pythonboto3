import unittest
from unittest.mock import patch, MagicMock
import boto3
import auto_scaling_group  

class TestAutoScalingGroup(unittest.TestCase):

    @patch('boto3.client')
    def test_create_launch_configuration(self, mock_boto3_client):
        # Mock the response from create_launch_configuration
        mock_client = MagicMock()
        mock_boto3_client.return_value = mock_client

        # Call the function
        auto_scaling_group.create_launch_configuration(
            'mock-launch-config',
            'mock-ami-id',
            't2.micro',
            'mock-key-name'
        )

        # Assert expected behavior
        mock_client.create_launch_configuration.assert_called_once_with(
            LaunchConfigurationName='mock-launch-config',
            ImageId='mock-ami-id',
            InstanceType='t2.micro',
            KeyName='mock-key-name'
        )
        print(f"Mock Launch Configuration created with Name: mock-launch-config")

    @patch('boto3.client')
    def test_create_auto_scaling_group(self, mock_boto3_client):
        # Mock the response from create_auto_scaling_group
        mock_client = MagicMock()
        mock_boto3_client.return_value = mock_client

        # Call the function
        auto_scaling_group.create_auto_scaling_group(
            'mock-auto-scaling-group',
            'mock-launch-config',
            1,
            3,
            'mock-subnet-id'
        )

        # Assert expected behavior
        mock_client.create_auto_scaling_group.assert_called_once_with(
            AutoScalingGroupName='mock-auto-scaling-group',
            LaunchConfigurationName='mock-launch-config',
            MinSize=1,
            MaxSize=3,
            VPCZoneIdentifier='mock-subnet-id'
        )
        print(f"Mock Auto Scaling Group created with Name: mock-auto-scaling-group")

if __name__ == '__main__':
    unittest.main()
