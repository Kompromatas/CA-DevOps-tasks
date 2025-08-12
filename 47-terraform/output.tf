output "public_ip" {
  value = aws_instance.ubuntu-47.public_ip
}

output "private_key_pem" {
  value     = tls_private_key.ec2-key.private_key_pem
  sensitive = true
}
