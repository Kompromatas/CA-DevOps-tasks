#!/bin/bash

# AWS CLI script to manage AWS resources

#create VPC
AWS_VPC=$(aws ec2 create-vpc --cidr-block 10.0.0.0/16 --query 'Vpc.{VpcId:VpcId}' --output text)
echo "Created VPC with ID: $AWS_VPC"

#add new tag to VPC
aws ec2 create-tags --resources $AWS_VPC --tags Key=Name,Value=DevOps-CA

#enable DNS hostnames
aws ec2 modify-vpc-attribute --vpc-id $AWS_VPC --enable-dns-hostnames "{\"Value\":true }"

#enable DNS support
aws ec2 modify-vpc-attribute --vpc-id $AWS_VPC --enable-dns-support "{\"Value\":true }"

#Create a public subnet
AWS_SUBNET=$(aws ec2 create-subnet --vpc-id $AWS_VPC --cidr-block 10.0.5.0/24 --availability-zone us-east-1a --query 'Subnet.{SubnetId:SubnetId}' --output text)

echo "Created Subnet with ID: $AWS_SUBNET"

#Add new tag to  public Subnet
aws ec2 create-tags --resources $AWS_SUBNET --tags Key=Name,Value=DevOps-CA-Public-Subnet

#Create a private subnet
AWS_PRIVATE_SUBNET=$(aws ec2 create-subnet --vpc-id $AWS_VPC --cidr-block 10.0.10.0/24 --availability-zone us-east-1a --query 'Subnet.{SubnetId:SubnetId}' --output text)
echo "Created Private Subnet with ID: $AWS_PRIVATE_SUBNET"

#Add new tag to private Subnet
aws ec2 create-tags --resources $AWS_PRIVATE_SUBNET --tags Key=Name,Value=DevOps-CA-Private-Subnet

#Enable auto-assign public IP on public subnet
aws ec2 modify-subnet-attribute --subnet-id $AWS_SUBNET --map-public-ip-on-launch

#Create an Internet Gateway
AWS_IGW=$(aws ec2 create-internet-gateway --query 'InternetGateway.{InternetGatewayId:InternetGatewayId}' --output text)
echo "Created Internet Gateway with ID: $AWS_IGW"

#Add new tag to Internet Gateway
aws ec2 create-tags --resources $AWS_IGW --tags Key=Name,Value=DevOps-CA-Internet-Gateway

#Attach The Internet Gateway to the VPC
aws ec2 attach-internet-gateway --vpc-id $AWS_VPC --internet-gateway-id $AWS_IGW --query 'InternetGateway.{InternetGatewayId:InternetGatewayId}' --output text
echo "Attached Internet Gateway $AWS_IGW to VPC $AWS_VPC"

#Create a custom route table
AWS_ROUTE_TABLE=$(aws ec2 create-route-table --vpc-id $AWS_VPC --query 'RouteTable.{RouteTableId:RouteTableId}' --output text)
echo "Created Route Table with ID: $AWS_ROUTE_TABLE"

#Add new tag to Route Table
aws ec2 create-tags --resources $AWS_ROUTE_TABLE --tags Key=Name,Value=DevOps-CA-Route-Table

#Get Elastic IP
AWS_EIP=$(aws ec2 allocate-address --domain vpc --query 'AllocationId' --output text)
echo "Allocated Elastic IP with ID: $AWS_EIP"

#Create a NAT Gateway in the public subnet
AWS_NAT_GATEWAY=$(aws ec2 create-nat-gateway --subnet-id $AWS_SUBNET --allocation-id $AWS_EIP --query 'NatGateway.{NatGatewayId:NatGatewayId}' --output text)
echo "Created NAT Gateway with ID: $AWS_NAT_GATEWAY"

#Add new tag to NAT Gateway
aws ec2 create-tags --resources $AWS_NAT_GATEWAY --tags Key=Name,Value=DevOps-CA-NAT-Gateway

#Create a custom route table association for the public subnet
aws ec2 associate-route-table --subnet-id $AWS_SUBNET --route-table-id $AWS_ROUTE_TABLE
echo "Associated Route Table $AWS_ROUTE_TABLE with Public Subnet $AWS_SUBNET"

#Associate the subnet with route table, making it a public subnet
aws ec2 create-route --route-table-id $AWS_ROUTE_TABLE --destination-cidr-block 0.0.0.0/0 --gateway-id $AWS_IGW --output text
echo "Created route in Route Table $AWS_ROUTE_TABLE to Internet Gateway $AWS_IGW for Public Subnet $AWS_SUBNET"

#Associate the NAT Gateway with the route table, makinit it a private subnet
aws ec2 create-route --route-table-id $AWS_ROUTE_TABLE --destination-cidr-block 10.0.10.0/24 --nat-gateway-id $AWS_NAT_GATEWAY --output text
echo "Created route in Route Table $AWS_ROUTE_TABLE to NAT Gateway $AWS_NAT_GATEWAY for Private Subnet $AWS_PRIVATE_SUBNET"


