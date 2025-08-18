variable "profile" {
  description = "The AWS profile for authentication"
  type        = string
  default     = "default"
}

variable "region" {
  description = "The AWS region to deploy resources to"
  type        = string
  default     = "us-east-1"
}

variable "ami_id" {
  description = "The default ami is Ubuntu 24.04 LTS"
  type        = string
  default     = "ami-020cba7c55df1f615" # Example AMI ID, replace with a valid one
}
