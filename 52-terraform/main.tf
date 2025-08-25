resource "aws_instance" "server1" {
  ami             = "ami-0a7d80731ae1b2435" # Example AMI, replace with a valid one for your region
  instance_type   = "t2.micro"
  security_groups = [aws_security_group.servers.name]
  tags = {
    Name = "WebAppServer1"
    Environment = "Dev"
  }
  user_data = <<-EOF
              #!/bin/bash
              echo "Hello, World from terraform build!!!!!!" > index.html
              python3 -m http.server 8080 &
              EOF

}

resource "aws_security_group" "servers" {
  name = "server-security-group"
}

resource "aws_security_group_rule" "allow_http_inbound" {
  type              = "ingress"
  from_port         = 8080
  to_port           = 8080
  protocol          = "tcp"
  security_group_id = aws_security_group.servers.id
  cidr_blocks       = ["78.63.11.220/32"]
}

