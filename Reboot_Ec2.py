import boto3

def reboot_ec2_instance(instance_id):
    # Create an EC2 client
    ec2_client = boto3.client('ec2')

    # Reboot the instance
    response = ec2_client.reboot_instances(InstanceIds=[instance_id])

    return response

if _name_ == "_main_":
    # Replace with your instance ID
    instance_id = 'i-0123456789abcdef0'
    
    # Reboot the instance
    response = reboot_ec2_instance(instance_id)
    print(response)
