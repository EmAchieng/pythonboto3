import unittest
from unittest.mock import patch, MagicMock
import boto3
import route_table 

class TestRouteTable(unittest.TestCase):

    @patch('boto3.client')
    def test_create_route_table(self, mock_boto3_client):
        # Mock the response from create_route_table
        mock_client = MagicMock()
        mock_boto3_client.return_value = mock_client
        mock_client.create_route_table.return_value = {
            'RouteTable': {
                'RouteTableId': 'mock-route-table-id'
            }
        }

        # Call the function
        route_table_id = route_table.create_route_table('mock-vpc-id')

        # Assert expected behavior
        self.assertEqual(route_table_id, 'mock-route-table-id')
        mock_client.create_route_table.assert_called_once_with(VpcId='mock-vpc-id')
        print(f"Mock Route Table created with ID: {route_table_id}")

    @patch('boto3.client')
    def test_associate_route_table(self, mock_boto3_client):
        # Mock the response from associate_route_table
        mock_client = MagicMock()
        mock_boto3_client.return_value = mock_client
        mock_client.associate_route_table.return_value = {
            'AssociationId': 'mock-association-id'
        }

        # Call the function
        association_id = route_table.associate_route_table('mock-route-table-id', 'mock-subnet-id')

        # Assert expected behavior
        self.assertEqual(association_id, 'mock-association-id')
        mock_client.associate_route_table.assert_called_once_with(
            RouteTableId='mock-route-table-id',
            SubnetId='mock-subnet-id'
        )
        print(f"Mock Route Table associated with Subnet. Association ID: {association_id}")

if __name__ == '__main__':
    unittest.main()
