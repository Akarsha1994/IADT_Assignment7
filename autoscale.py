import boto3


client = boto3.client('autoscaling')


response = client.create_auto_scaling_group(
    AutoScalingGroupName='ASGName',
    MixedInstancesPolicy={
        'LaunchTemplate': {
            'LaunchTemplateSpecification': {
                'LaunchTemplateId': 'Id',
                'Version': '5'
            },
            'Overrides': [
                {
                    'InstanceType': 't2.micro',
                    'LaunchTemplateSpecification': {
                        'LaunchTemplateId': 'Id',
                        'Version': '5'
                    }
                },
                {
                    'InstanceType': 't2.micro',
                    'LaunchTemplateSpecification': {
                        'LaunchTemplateId': 'Id',
                        'Version': '4'
                    }
                },
                {
                    'InstanceType': 't2.micro',
                    'LaunchTemplateSpecification': {
                        'LaunchTemplateId': 'Id',
                        'Version': '6'
                    }
                },
            ]
        },
        'InstancesDistribution': {
            'OnDemandBaseCapacity': 0,
            'OnDemandPercentageAboveBaseCapacity': 0,
            'SpotAllocationStrategy': 'capacity-optimized',
        }
    },
    MinSize=2,
    MaxSize=3,
    DesiredCapacity=0,
    VPCZoneIdentifier='subnet-1, subnet-2, subnet-3',
    Tags=[
        {
            'ResourceId': 'ASGName',
            'ResourceType': 'auto-scaling-group',
            'Key': 'Name',
            'Value': 'ASGName',
            'PropagateAtLaunch': True
        },
    ],
)

print(response)



