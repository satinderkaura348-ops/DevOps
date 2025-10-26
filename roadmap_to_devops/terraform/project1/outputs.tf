# outputs for counts

# output "ec2_public_ip" {
#     value = aws_instance.my-test[*].public_ip # if multiple instance then use * .

# }

# output "ec2_public_dns" {
#     value = aws_instance.my-test[*].public_dns 
# }

# output "ec2_private_ip" {
#     value = aws_instance.my-test[*].private_ip
# }



# outputs for for_each
output "ec2_public_ip" {
    value = [
        for key in aws_instance.my-test : key.public_ip
    ]
}