from pprint import pprint
import boto3
import configparser

def put_item(seq, community_seq, text):
    config = configparser.ConfigParser()
    config.read('/app/config.ini', encoding='utf-8')
    dynamodb = boto3.client('dynamodb', aws_access_key_id=config['AWS']['AccessKey'], aws_secret_access_key=config['AWS']['SecretKey'], region_name='ap-northeast-2')

    response = dynamodb.put_item(
        TableName='tbl_designer_gather', 
        Item={ 
            'seq':{ 'N':seq }, 
            'community_seq':{ 'N': community_seq },
            'text':{'S': text },
            }       
        ),
        
        
    return response
    