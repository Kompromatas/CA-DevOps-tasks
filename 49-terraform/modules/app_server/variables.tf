variable "instance_name" {
  description = "The name of the application server instance"
  type        = string
  default     = "app-server"
}

variable "ami_id" {
  description = "The AMI ID for the application server"
  type        = string
  default     = "ami-020cba7c55df1f615" # Example AMI ID, replace with a valid one
  
}

variable "instance_type" {
  description = "The instance type for the application server"
  type        = string
  default     = "t2.micro"
  
}

variable "vpc_security_group_id" {
  description = "The VPC security group ID for the application server"
  type        = string
  default     = "" # Example security group ID, replace with a valid one
}

variable "subnet_id" {
  description = "The subnet ID for the application server"
  type        = string
  default     = "" # Example subnet ID, replace with a valid one
}