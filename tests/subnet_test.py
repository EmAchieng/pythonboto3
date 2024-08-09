import unittest
from unittest.mock import patch, MagicMock
import boto3
import subnet  

class TestSubnet(unittest.TestCase):

    @patch('boto3.client')
    def test_create_subnet(self, mock_boto3_client):
        # Mock the response from create_subnet
        mock_client = MagicMock()
        mock_boto3_client.return_value = mock_client
        mock_client.create_subnet.return_value = {
            'Subnet': {
                'SubnetId': 'mock-subnet-id'
            }
        }

        subnet_id = subnet.create_su
