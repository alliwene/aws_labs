import boto3

client = boto3.client('cloudformation')

response = client.create_stack(
    StackName='lab192Stack',
    TemplateURL='https://bunmi0045.s3.us-west-2.amazonaws.com/CloudFormationChallenge.yml',
    OnFailure='DO_NOTHING',
    Capabilities=['CAPABILITY_NAMED_IAM'])

print(response)