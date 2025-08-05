import boto3

ec2 = boto3.client('ec2')

response = ec2.run_instances(
    ImageId='ami-0c55b159cbfafe1f0',  # Replace with a valid AMI ID for your region
    InstanceType='t2.micro',
    KeyName='my-key-pair',  # Replace with your key pair name
    MinCount=1,
    MaxCount=1
)

instance_id = response['Instances'][0]['InstanceId']
print(f'Launched EC2 instance with ID: {instance_id}')
