import boto3


def getSsmVal(ssmObject: str) -> dict:
    """returns ssm value given object name"""
    ssm = boto3.client('ssm')
    parameter = ssm.get_parameter(Name=ssmObject, WithDecryption=True)
    return parameter['Parameter']['Value']


ssmOb = getSsmVal('/Prod/Db/Password')
print(ssmOb)
