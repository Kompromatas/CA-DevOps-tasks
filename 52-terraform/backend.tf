terraform {
    backend "s3" {
        bucket = "terraformstate1984"
        key    = "52-terraform/terraform.tfstate"
        region = "us-east-1"
        dynamodb_table = "terraform-locks"
        encrypt = true
    }
}