import unittest
from unittest.mock import patch, MagicMock
import sys
import io
import boto3
import security_group  

class TestSecurityGroup(unittest.TestCase):

    @patch('boto3.client')
    def test_create_security_group(self, mock_boto3_client):
        # Mock the response from create_security_group
        mock_client = MagicMock()
        mock_boto3_client.return_value = mock_client
        mock_client.create_security_group.return_value = {
            'GroupId': 'mock-sg-id'
        }

        # Call the function with mock values
        sg_id = security_group.create_security_group('mock-vpc-id', 'test-group', 'Test description')

        # Assert expected behavior
        self.assertEqual(sg_id, 'mock-sg-id')
        mock_client.create_security_group.assert_called_once_with(
            GroupName='test-group',
            Description='Test description',
            VpcId='mock-vpc-id'
        )
        print(f"Mock Security Group created with ID: {sg_id}")

    @patch('boto3.client')
    def test_authorize_ingress(self, mock_boto3_client):
        # Mock the response from authorize_security_group_ingress
        mock_client = MagicMock()
        mock_boto3_client.return_value = mock_client

        # Call the function with mock values
        security_group.authorize_ingress('mock-sg-id', 80, 'tcp', '0.0.0.0/0')

        # Assert expected behavior
        mock_client.authorize_security_group_ingress.assert_called_once_with(
            GroupId='mock-sg-id',
            IpPermissions=[
                {
                    'IpProtocol': 'tcp',
                    'FromPort': 80,
                    'ToPort': 80,
                    'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                }
            ]
        )
