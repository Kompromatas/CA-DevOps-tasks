output "public_ip" {
  value = aws_instance.ubuntu-48.public_ip
}

output "private_key_pem" {
  value     = tls_private_key.ec2-key.private_key_pem
  sensitive = true
}

output "ip_address" {
  value = aws_instance.ubuntu-48.public_ip
}