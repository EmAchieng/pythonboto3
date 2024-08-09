# AWS Infrastructure Management with Python boto3

## Overview

This Python SDK provides modularized management of AWS infrastructure resources using boto3. It simplifies tasks such as creating Virtual Private Clouds (VPCs), launching EC2 instances, managing security groups, and more.

## Modularity

### Architecture

The SDK is structured into individual modules for different AWS resources:
- **VPC Module:** Handles VPC creation and management.
- **EC2 Instance Module:** Manages EC2 instance launching and configuration.
- **Security Group Module:** Facilitates security group creation and rules management.
- **Subnet Module:** Supports subnet creation and configuration.
- **Internet Gateway Module:** Provides functionality for managing internet gateways.

### Benefits of Modularity

1. **Code Organization:** Each module encapsulates logic specific to its AWS resource, enhancing code organization and readability.

2. **Reusability:** Modules can be reused across projects or within the same project for different infrastructure components, promoting code reusability.

3. **Scalability:** Easily add new modules for additional AWS resources or modify existing ones without impacting other parts of the SDK.

### Prerequisites

Before installing the SDK, ensure:
- Python 3.9+ is installed on your system.
- AWS credentials are configured:
  - Either through environment variables (`AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`).
  - Or using AWS CLI configuration (`aws configure`).

### Installation Guide
   ```bash
   python3 -m venv path/to/venv
    source path/to/venv/bin/activate
    python3 -m pip install -r requirements.txt
   ```
### Running the module files
  ```bash
   python3 modules/main.py
```

### Testing
   ```bash
   python3 pip install pytest
   pytest test/

   ```
