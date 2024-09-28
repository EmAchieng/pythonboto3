import unittest
from unittest.mock import patch, MagicMock
import boto3
import ec2_instance  

class TestEC2InstanceFunctions(unittest.TestCase):

    @patch('boto3.client')
    def test_create_ec2_instance(self, mock_ec2_client):
        # Mock the EC2 client and its run_instances method
        mock_response = {
            'Instances': [
                {
                    'InstanceId': 'i-1234567890abcdef0'
                }
            ]
        }
        mock_ec2_client.return_value.run_instances.return_value = mock_response

        # mock parameters
        ami_id = 'ami-12345678'
        instance_type = 't2.micro'
        key_name = 'my-key-pair'
        subnet_id = 'subnet-12345678'
        sg_id = 'sg-12345678'

        # Call the function
        instance_id = ec2_instance.create_ec2_instance(ami_id, instance_type, key_name, subnet_id, sg_id)

        # Assert the output
        self.assertEqual(instance_id, 'i-1234567890abcdef0')

    @patch('boto3.client')
    def test_create_ec2_instance_failure(self, mock_ec2_client):
        # Mock the EC2 client to raise an exception
        mock_ec2_client.return_value.run_instances.side_effect = Exception("Instance creation failed")

        # Mock parameters
        ami_id = 'ami-12345678'
        instance_type = 't2.micro'
        key_name = 'my-key-pair'
        subnet_id = 'subnet-12345678'
        sg_id = 'sg-12345678'

        with self.assertRaises(Exception) as context:
            ec2_instance.create_ec2_instance(ami_id, instance_type, key_name, subnet_id, sg_id)
        
        # Check if the exception message is correct
        self.assertEqual(str(context.exception), "Instance creation failed")

    @patch('boto3.client')
    def test_get_instance_public_ip(self, mock_ec2_client):
        # Mock the EC2 client and its describe_instances method
        mock_instance = {
            'InstanceId': 'i-1234567890abcdef0',
            'PublicIpAddress': '203.0.113.10'  
        }
        mock_ec2_client.return_value.describe_instances.return_value = {
            'Reservations': [
                {
                    'Instances': [mock_instance]
                }
            ]
        }

        # Call the function
        public_ip = ec2_instance.get_instance_public_ip('i-1234567890abcdef0')

        # Assert the output
        self.assertEqual(public_ip, '203.0.113.10')

    @patch('boto3.client')
    def test_get_instance_public_ip_pending(self, mock_ec2_client):
        # Mock describe_instances to return a pending PublicIpAddress
        mock_instance = {
            'InstanceId': 'i-1234567890abcdef0',
            'PublicIpAddress': 'Pending'
        }
        mock_ec2_client.return_value.describe_instances.return_value = {
            'Reservations': [
                {
                    'Instances': [mock_instance]
                }
            ]
        }

        with self.assertRaises(RuntimeError):
            ec2_instance.get_instance_public_ip('i-1234567890abcdef0')


if __name__ == '__main__':
    unittest.main()
