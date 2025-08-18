module "vpc" {
    source  = "terraform-aws-modules/vpc/aws"
    version = "6.0.1"

    name = "vpc-49-terraform"
    cidr = "10.10.0.0/16"
    azs  = ["us-east-1a"]
    public_subnets = ["10.10.5.0/24"]
}

module "app_server" {
    source = "./modules/app_server"
    instance_type = "t2.micro"
#    ami = "ami-020cba7c55df1f615"
    subnet_id = module.vpc.public_subnets[0]
    vpc_security_group_id = module.vpc.default_security_group_id
    count = 1
}

module "ec2_instance" {
  source = "git::https://github.com/terraform-aws-modules/terraform-aws-ec2-instance.git?ref=v6.0.2"
#   version = "6.0.2"

  name = "git-module-ec2-49"
  ami = "ami-020cba7c55df1f615" # Example AMI, replace with a valid one for your region
  instance_type = "t2.micro"

  vpc_security_group_ids = [module.vpc.default_security_group_id]
  subnet_id = module.vpc.public_subnets[0]

  tags = {
    Name = "git-module-ec2-49"
  }
}