import unittest
from unittest.mock import patch, MagicMock
import boto3
import vpc  

class TestVPC(unittest.TestCase):

    @patch('boto3.client')
    def test_create_vpc(self, mock_boto3_client):
        # Mock the response from create_vpc
        mock_client = MagicMock()
        mock_boto3_client.return_value = mock_client
        mock_client.create_vpc.return_value = {
            'Vpc': {
                'VpcId': 'mock-vpc-id'
            }
        }

        vpc_id = vpc.create_vpc('10.0.0.0/16')

        # Assert expected behavior
        self.assertEqual(vpc_id, 'mock-vpc-id')
        mock_client.create_vpc.assert_called_once_with(CidrBlock='10.0.0.0/16')
        print(f"Mock VPC created")
