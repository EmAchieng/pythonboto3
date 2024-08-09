import unittest
from unittest.mock import patch, MagicMock
import boto3
from internet_gateway import create_internet_gateway

class TestCreateInternetGateway(unittest.TestCase):

    @patch('boto3.client')
    def test_create_internet_gateway(self, mock_boto3_client):
        # Mock the return value of create_internet_gateway
        mock_response = {
            'InternetGateway': {
                'InternetGatewayId': 'mock-igw-id'
            }
        }
        mock_boto3_client.return_value.create_internet_gateway.return_value = mock_response

        # Mock the return value of attach_internet_gateway
        mock_attach_response = {}
        mock_boto3_client.return_value.attach_internet_gateway.return_value = mock_attach_response

        # Mock the VPC ID
        mock_vpc_id = 'mock-vpc-id'

        # Call the function
        igw_id = create_internet_gateway(mock_vpc_id)

        # Assert calls were made
        mock_boto3_client.assert_called_once_with('ec2')
        mock_boto3_client.return_value.create_internet_gateway.assert_called_once()

        # Assert the result
        self.assertEqual(igw_id, 'mock-igw-id')

if __name__ == '__main__':
    unittest.main()
