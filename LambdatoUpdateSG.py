import boto3
import json
import os
from datetime import date

datetime = str
dynamodb = boto3.client('dynamodb')


def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    SG = event["queryStringParameters"]["Security_Group"]
    print (SG)
    SG_region = event["queryStringParameters"]["Security_Group_Region"]
    print (SG_region)
    Port = 3389
    Protocol = event["queryStringParameters"]["Protocol"]
    print (Protocol)
    client = event["queryStringParameters"]["Ip_client"]
    print (client)
    connection = boto3.client('ec2', region_name=SG_region)
    action = event["queryStringParameters"]["action"]
    if action == "add" :
        try:
            response = connection.authorize_security_group_ingress(
                GroupId=SG,
                    IpPermissions=[
                        {
                            'FromPort': Port,
                            'IpProtocol': Protocol,
                            'IpRanges': [
                                {
                                    'CidrIp': client,
                                    'Description': 'RDP connection from client',
                                },
                            ],
                            'ToPort': Port,
                        },
                    ],
                ),
            print(response)
            today = date.today()
            datetime = today.strftime("%d/%m/%Y")
            dynamodb.put_item(TableName='SG_Data', 
                Item={  
                        'CreationDate':{'S':(datetime)},
                        'IP':{'S':(client)},
                        'SG':{'S':(SG)}
                    }
                )
            
            return {
                'statusCode': '200',
                'body': json.dumps(response),
                'headers': {
                'Content-Type': 'application/json',
                }
            }
        except Exception:
            response = "Error en la carga del security group"
            return {
                'statusCode': '200',
                'body': json.dumps(response),
                'headers': {
                'Content-Type': 'application/json',
                }
            }
    
    if action == "remove" :
        try:
            response = connection.revoke_security_group_ingress(
                GroupId=SG,
                    IpPermissions=[
                        {
                            'FromPort': Port,
                            'IpProtocol': Protocol,
                            'IpRanges': [
                                {
                                    'CidrIp': client,
                                    'Description': 'RDP connection from client',
                                },
                            ],
                            'ToPort': Port,
                        },
                    ],
                ),
            print(response)
            today = date.today()
            datetime = today.strftime("%d/%m/%Y")
            value = dynamodb.delete_item(TableName='SG_Data', 
                    Key={  
                        'CreationDate':{'S':(datetime)},
                        'IP':{'S':(client)}
                        }
                    )
            print (value)
            return {
                'statusCode': '200',
                'body': json.dumps(response),
                'headers': {
                'Content-Type': 'application/json',
                }
            }
        except Exception:
            response = "Error en la remocion del security group"
            return {
                'statusCode': '200',
                'body': json.dumps(response),
                'headers': {
                'Content-Type': 'application/json',
                }
            }
        
