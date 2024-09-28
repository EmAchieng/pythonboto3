import unittest
from unittest.mock import patch, MagicMock
import sys
import io
import time
import vpc
import subnet
import internet_gateway
import security_group
import ec2_instance
import main_setup
import route_table
import auto_scaling_group  

class TestMainSetup(unittest.TestCase):

    @patch('vpc.create_vpc')
    @patch('subnet.create_subnet')
    @patch('internet_gateway.create_internet_gateway')
    @patch('security_group.create_security_group')
    @patch('security_group.authorize_ingress')
    @patch('ec2_instance.create_ec2_instance')
    @patch('ec2_instance.get_instance_public_ip')
    @patch('route_table.create_route_table')  
    @patch('route_table.associate_route_table')  
    @patch('auto_scaling_group.create_launch_configuration') 
    @patch('auto_scaling_group.create_auto_scaling_group')  
    @patch('vpc.check_vpc_status')  # Mocking the status check
    @patch('subnet.check_subnet_status')  
    @patch('internet_gateway.check_igw_status')  
    @patch('security_group.check_sg_status')  
    @patch('route_table.check_route_table_status')  
    @patch('ec2_instance.check_instance_status') 
    @patch('main_setup.cleanup_resources')  # Ensure cleanup_resources is mocked
    def test_main_setup(self, mock_cleanup_resources, mock_create_auto_scaling_group, mock_create_launch_configuration, 
                        mock_associate_route_table, mock_create_route_table, 
                        mock_get_instance_public_ip, mock_create_ec2_instance,
                        mock_authorize_ingress, mock_create_security_group,
                        mock_create_internet_gateway, mock_create_subnet, mock_create_vpc,
                        mock_check_vpc_status, mock_check_subnet_status, 
                        mock_check_igw_status, mock_check_sg_status, 
                        mock_check_route_table_status, mock_check_instance_status):
        
        # Mock return values for each function call
        mock_create_vpc.return_value = "mock-vpc-id"
        mock_create_subnet.return_value = "mock-subnet-id"
        mock_create_internet_gateway.return_value = "mock-igw-id"
        mock_create_security_group.return_value = "mock-sg-id"
        mock_create_ec2_instance.return_value = "mock-instance-id"
        mock_get_instance_public_ip.return_value = "mock-public-ip"
        mock_create_route_table.return_value = "mock-route-table-id"
        mock_associate_route_table.return_value = "mock-association-id"
        mock_create_launch_configuration.return_value = None
        mock_create_auto_scaling_group.return_value = None

        # Mock the status checks to return True immediately
        mock_check_vpc_status.return_value = True
        mock_check_subnet_status.return_value = True
        mock_check_igw_status.return_value = True
        mock_check_sg_status.return_value = True
        mock_check_route_table_status.return_value = True
        mock_check_instance_status.return_value = True
        
        # Redirect stdout to capture print statements
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Call the main setup function
        main_setup.main()

        # Assert expected sequence of function calls
        mock_create_vpc.assert_called_once_with("10.0.0.0/16")
        mock_create_subnet.assert_called_once_with("mock-vpc-id", "10.0.1.0/24", "eu-central-2a")
        mock_create_internet_gateway.assert_called_once_with("mock-vpc-id")
        mock_create_security_group.assert_called_once_with("mock-vpc-id", "nginx-sg", "Security group for Nginx")
        mock_authorize_ingress.assert_called_once_with("mock-sg-id", 80, "tcp", "0.0.0.0/0")
        mock_create_ec2_instance.assert_called_once_with("ami-0c577783b0a2933b7", "t3.micro", "my-key-pair", "mock-subnet-id", "mock-sg-id")
        
        # Assert that get_instance_public_ip is only called once
        mock_get_instance_public_ip.assert_called_once_with("mock-instance-id")

        mock_create_route_table.assert_called_once_with("mock-vpc-id")
        mock_associate_route_table.assert_called_once_with("mock-route-table-id", "mock-subnet-id")
        mock_create_launch_configuration.assert_called_once_with("my-launch-configuration", "ami-0c577783b0a2933b7", "t3.micro", "my-key-pair")
        mock_create_auto_scaling_group.assert_called_once_with("my-auto-scaling-group", "my-launch-configuration", 1, 3, "mock-subnet-id")
        
        # Assert printed output
        self.assertIn("EC2 Instance Public IP: mock-public-ip", captured_output.getvalue())
        self.assertIn("Setup complete.", captured_output.getvalue())
        self.assertIn(f"You can access Nginx at http://mock-public-ip/", captured_output.getvalue())
        self.assertIn("Hello World from Nginx", captured_output.getvalue())

        # Assert that cleanup_resources is called after the setup process
        mock_cleanup_resources.assert_called_once_with("mock-instance-id", "mock-subnet-id", "mock-sg-id", "mock-route-table-id", "mock-vpc-id")
        
if __name__ == '__main__':
    unittest.main()
