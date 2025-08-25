terraform {
    backend "s3" {
        bucket = "terraformstate1984"
        key    = "52-terraform/terraform.tfstate"
        region = "us-east-1"
        use_lockfile = true
        encrypt = true
    }
}