import boto3
import json
import os

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    SG = (event.get('Security_Group'))
    SG_region = (event.get('Security_Group_Region'))
    client = (event.get('Ip_client'))
    connection = boto3.client('ec2', region_name=SG_region)
    action = (event.get('action'))
    if action == "add" :
        try:
            response = connection.authorize_security_group_ingress(
                GroupId=SG,
                    IpPermissions=[
                        {
                            'FromPort': 3389,
                            'IpProtocol': 'tcp',
                            'IpRanges': [
                                {
                                    'CidrIp': client,
                                    'Description': 'RDP connection from client',
                                },
                            ],
                            'ToPort': 3389,
                        },
                    ],
                ),
            print(response)
            return response
        except Exception:
            response = "Error en la carga del security group"
            return response
    
    if action == "remove" :
        try:
            response = connection.revoke_security_group_ingress(
                GroupId=SG,
                    IpPermissions=[
                        {
                            'FromPort': 3389,
                            'IpProtocol': 'tcp',
                            'IpRanges': [
                                {
                                    'CidrIp': client,
                                    'Description': 'RDP connection from client',
                                },
                            ],
                            'ToPort': 3389,
                        },
                    ],
                ),
            print(response)
            return response
        except Exception:
            response = "Error en la remoción del security group"
            return response
        

