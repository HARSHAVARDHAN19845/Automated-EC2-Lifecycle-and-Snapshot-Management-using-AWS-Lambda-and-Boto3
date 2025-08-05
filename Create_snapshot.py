import boto3
from datetime import datetime

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    
    # Define your instance and volume IDs
    instance_id = 'YOUR_INSTANCE_ID'
    volume_id = 'YOUR_VOLUME_ID'
    
    # Create a snapshot for the predefined volume
    try:
        response = ec2.create_snapshot(
            VolumeId=volume_id,
            Description=f'Snapshot of {volume_id} created on {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
        )
        print(f'Snapshot created for volume {volume_id}: {response["SnapshotId"]}')
    except Exception as e:
        print(f'Error creating snapshot: {str(e)}')
    
    return {
        'statusCode': 200,
        'body': f'Snapshot created for volume {volume_id}'
    }
