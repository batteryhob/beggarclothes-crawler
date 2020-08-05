from pprint import pprint
from datetime import datetime

import boto3
import configparser
import pymysql


def get_items():
    config = configparser.ConfigParser()
    config.read('/app/config.ini', encoding='utf-8')

    con = pymysql.connect(host=config['Nas']['HOST'], port=3307, user=config['Nas']['USER'], passwd=config['Nas']['PASSWORD'], db=config['Nas']['NAME'], charset='utf8')
    cur = con.cursor()
    cur.execute(
        query='''
            SELECT 
            `tag`, `name`, `designer_seq` 
            FROM tbl_designer_tags A
            LEFT JOIN tbl_designer B
            ON A.designer_seq = B.seq
            WHERE `use` = true
        ''')
    rows = cur.fetchall()
    con.close()
    return rows


def put_item(seq, community_seq, designer, tag, text):
    config = configparser.ConfigParser()
    config.read('/app/config.ini', encoding='utf-8')
    dynamodb = boto3.client('dynamodb', aws_access_key_id=config['AWS']['AccessKey'], aws_secret_access_key=config['AWS']['SecretKey'], region_name='ap-northeast-2')

    response = dynamodb.put_item(
        TableName='tbl_designer_gather', 
        Item={ 
            'seq':{ 'N':seq }, 
            'community_seq':{ 'N': community_seq },
            'designer':{'S': designer },
            'tag':{'S': tag },
            'text':{'S': text },
            'date': {'S': datetime.today().strftime('%Y%m%d') },
            'timestamp': {'S': datetime.today().strftime('%Y%m%d%H%M%S') }
            }
        ),
        
        
    return response
    