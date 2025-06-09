# Configuration Management: Ansible & Terraform

## Ansible

Ansible is an open-source automation tool for configuration management, application deployment, and task automation. It uses YAML-based playbooks to define automation tasks and operates agentlessly over SSH.

### Key Features

- Agentless architecture
- Simple YAML syntax (playbooks)
- Idempotent operations
- Large module ecosystem

### Basic Usage

#### Inventory File (`hosts`)
```ini
[webservers]
server1.example.com
server2.example.com
```

#### Simple Playbook Example
```yaml
---
- name: Install Nginx on webservers
    hosts: webservers
    become: yes
    tasks:
        - name: Ensure Nginx is installed
            apt:
                name: nginx
                state: present
```

#### Running a Playbook
```sh
ansible-playbook -i hosts install_nginx.yml
```

### Common Commands

- Run ad-hoc command:  
        `ansible all -i hosts -m ping`
- Check playbook syntax:  
        `ansible-playbook --syntax-check playbook.yml`

---

### Advanced Example: Multi-Role Playbook with Variables and Handlers

```yaml
---
- name: Configure webservers with Nginx and firewall
    hosts: webservers
    become: yes
    vars:
        nginx_port: 8080
    roles:
        - nginx
        - ufw

# roles/nginx/tasks/main.yml
- name: Install Nginx
    apt:
        name: nginx
        state: present

- name: Configure Nginx to listen on custom port
    lineinfile:
        path: /etc/nginx/sites-available/default
        regexp: 'listen 80 default_server;'
        line: "listen {{ nginx_port }} default_server;"
    notify: Restart Nginx

# roles/nginx/handlers/main.yml
- name: Restart Nginx
    service:
        name: nginx
        state: restarted

# roles/ufw/tasks/main.yml
- name: Allow Nginx port through firewall
    ufw:
        rule: allow
        port: "{{ nginx_port }}"
        proto: tcp
```

---

## Terraform

Terraform is an open-source Infrastructure as Code (IaC) tool for provisioning and managing cloud resources. It uses declarative configuration files written in HashiCorp Configuration Language (HCL).

### Key Features

- Supports multiple cloud providers
- Declarative resource definitions
- State management
- Modular and reusable code

### Basic Usage

#### Example Configuration (`main.tf`)
```hcl
provider "aws" {
        region = "us-west-2"
}

resource "aws_instance" "example" {
        ami           = "ami-0c55b159cbfafe1f0"
        instance_type = "t2.micro"
}
```

#### Common Commands

- Initialize working directory:  
        `terraform init`
- Preview changes:  
        `terraform plan`
- Apply configuration:  
        `terraform apply`
- Destroy resources:  
        `terraform destroy`

### Example Workflow

```sh
terraform init
terraform plan
terraform apply
```

---

### Advanced Example: Using Modules, Variables, and Outputs

#### Directory Structure
```
terraform/
├── main.tf
├── variables.tf
├── outputs.tf
└── modules/
        └── vpc/
                ├── main.tf
                ├── variables.tf
                └── outputs.tf
```

#### Root Module (`main.tf`)
```hcl
module "vpc" {
    source = "./modules/vpc"
    cidr_block = var.vpc_cidr
}

resource "aws_instance" "web" {
    ami           = var.ami_id
    instance_type = var.instance_type
    subnet_id     = module.vpc.public_subnet_id
}

output "web_instance_public_ip" {
    value = aws_instance.web.public_ip
}
```

#### Variables (`variables.tf`)
```hcl
variable "vpc_cidr" {
    description = "CIDR block for the VPC"
    default     = "10.0.0.0/16"
}

variable "ami_id" {
    description = "AMI ID for EC2 instance"
}

variable "instance_type" {
    description = "EC2 instance type"
    default     = "t2.micro"
}
```

#### Module Example (`modules/vpc/main.tf`)
```hcl
resource "aws_vpc" "this" {
    cidr_block = var.cidr_block
}

resource "aws_subnet" "public" {
    vpc_id     = aws_vpc.this.id
    cidr_block = cidrsubnet(var.cidr_block, 8, 0)
}

output "public_subnet_id" {
    value = aws_subnet.public.id
}
```

---

Both Ansible and Terraform are essential tools for modern DevOps workflows, enabling automation, repeatability, and scalability in infrastructure and configuration management.