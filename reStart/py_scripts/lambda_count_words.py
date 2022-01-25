import urllib
import boto3

def lambda_handler(event, context):
    # Get the bucket name
    bucket = event['Records'][0]['s3']['bucket']['name']
    # 2 - Get the file/key name
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8') 
    # print(key)
    try:
        s3 = boto3.client('s3') 
        #3 - Fetch the file from S3
        response = s3.get_object(Bucket=bucket, Key=key)
        #4 - Deserialize the file's content
        text = response["Body"].read().decode('utf-8')
        number_of_words = 0 
        # print(text) 
        lines = [i for i in text.split() if i.isalnum()]
        number_of_words += len(lines) 
        # # Printing total number of words
        sns_message = f'The word count in the file {key} is {number_of_words}.'
        print(sns_message) 
        sns = boto3.client('sns')
        subject = "Word Count Result"
        sns_response = sns.publish(
            TargetArn='arn:aws:sns:us-west-2:097619393403:count-words-topic',
            Message= str(sns_message),
            Subject= subject 
        ) 

    except Exception as e:
        print(e)
        raise e 



# s3 = boto3.resource('s3')
# obj = s3.Object(bucket, key)
# obj.get()['Body'].read().decode('utf-8') 