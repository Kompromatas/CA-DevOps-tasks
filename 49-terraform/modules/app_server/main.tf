resource "aws_instance" "server" { 
  ami           = var.ami_id # Example AMI ID, replace with a valid one
  instance_type = var.instance_type
  subnet_id = var.subnet_id
  vpc_security_group_ids = [var.vpc_security_group_id]
  tags = {
    Name = "${var.instance_name}-49"
  }
}