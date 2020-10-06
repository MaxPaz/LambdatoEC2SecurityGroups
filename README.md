# LambdatoEC2SecurityGroups
## This code works in Python 3.7

## The information received by the function should be as the following:

### --------- For Adding a Security Group Rule --------
- {
- "Security_Group":"sg-0a47d09070c824389",		//Security Group ID
- "Security_Group_Region":"us-east-1",				//Region
- "Ip_client":"10.10.10.10/32",    						//IP/Mask
- "action": "add",														//action: add
- "Port":"3389",                              //Port
- "Protocol":"tcp"                            //Protocol
- }

### --------- For Removing a Security Group Rule ------
- {
- "Security_Group":"sg-0a47d09070c824389",		//Security Group ID
- "Security_Group_Region":"us-east-1",				//Region
- "Ip_client":"10.10.10.1/32",								//IP/Mask
- "action": "remove",													//action: remove
- "Port":"3389",                              //Port
- "Protocol":"tcp"                            //Protocol
- }
