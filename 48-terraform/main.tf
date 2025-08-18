# Terraform AWS EC2 Instance creation with access key

terraform {
    required_providers {
        aws = {
        source  = "hashicorp/aws"
        version = "~> 3.0"
        }
    }
}

provider "aws" {
  profile = var.profile
  region  = var.region 
  
}

resource "tls_private_key" "ec2-key" {  
  algorithm = "RSA"
  rsa_bits  = 4096
}

resource "aws_key_pair" "Key-48" {
  key_name   = "Key-48"
  public_key = tls_private_key.ec2-key.public_key_openssh # Path to your public key file
  
}

resource "aws_security_group" "ec2-sg-48" {
  name        = "ec2-sg-48"
  description = "Security group to access EC2 instance - 48 pamoka"
  
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["88.118.71.155/32"] # Replace with your CIDR block
  }
}

resource "aws_instance" "ubuntu-48" {
  ami           = var.ami_id # Example AMI ID, replace with a valid one
  instance_type = "t2.micro"
  key_name = aws_key_pair.Key-48.key_name
  security_groups = [aws_security_group.ec2-sg-48.name]
  associate_public_ip_address = true
  tags = {
    Name = "48 pamoka"
  }
}