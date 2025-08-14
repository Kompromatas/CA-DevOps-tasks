# Terraform Basics

Terraform is an open-source Infrastructure as Code (IaC) tool that allows you to define and provision infrastructure using a declarative configuration language.

## Key Concepts

- **Providers**: Plugins that interact with cloud platforms (AWS, Azure, GCP, etc.).
- **Resources**: Infrastructure components (VMs, networks, databases).
- **State**: Terraform keeps track of resources it manages in a state file.

## Installation

Download Terraform from [terraform.io](https://www.terraform.io/downloads.html) and add it to your system PATH.

## Basic Commands

### 1. Initialize Terraform

```sh
terraform init
```
Initializes the working directory containing Terraform configuration files.

### 2. Format Configuration Files

```sh
terraform fmt
```
Automatically formats your code for readability.

### 3. Validate Configuration

```sh
terraform validate
```
Checks whether the configuration is syntactically valid.

### 4. Plan Infrastructure Changes

```sh
terraform plan
```
Shows what actions Terraform will take without making changes.

### 5. Apply Changes

```sh
terraform apply
```
Applies the planned changes to your infrastructure.

### 6. Destroy Infrastructure

```sh
terraform destroy
```
Removes all resources defined in your configuration.

## Example: Provision an AWS EC2 Instance

```hcl
provider "aws" {
    region = "us-west-2"
}

resource "aws_instance" "example" {
    ami           = "ami-0c55b159cbfafe1f0"
    instance_type = "t2.micro"
}
```

## Workflow

1. Write configuration in `.tf` files.
2. Run `terraform init`.
3. Run `terraform plan`.
4. Run `terraform apply`.
5. Manage resources as needed.

## Useful Links

- [Terraform Documentation](https://www.terraform.io/docs)
- [Terraform Registry](https://registry.terraform.io/)


## Get info from Output

terraform output -raw private_key_pem > ec2-key.pem
