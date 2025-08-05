import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    
    # Define your instance ID
    instance_id = 'YOUR_INSTANCE_ID'
    
    try:
        response = ec2.terminate_instances(
            InstanceIds=[instance_id]
        )
        print(f'Instance {instance_id} termination initiated: {response}')
    except Exception as e:
        print(f'Error terminating instance {instance_id}: {str(e)}')
    
    return {
        'statusCode': 200,
        'body': f'Instance {instance_id} termination initiated.'
    }
