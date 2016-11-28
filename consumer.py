import json
from kafka import KafkaConsumer
from alchemyapi import AlchemyAPI
import boto3

client = boto3.client('sns')
# To consume latest messages and auto-commit offsets
print "ALEX"
consumer = KafkaConsumer('test',
                         group_id='my-group',
                         bootstrap_servers=['52.23.195.196:9092'])
alchemyapi = AlchemyAPI()
delimiter='$$delim1738352016$$'
for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print message
    tweetData=json.loads(message.value)
    response=alchemyapi.sentiment("text",tweetData['status'])
    print "ALEXZEROOO"
    print response
    if 'docSentiment' in response:
        feeling=response["docSentiment"]["type"]
        sendString=tweetData['status']+delimiter+str(tweetData['lat'])+delimiter+str(tweetData['lng'])+delimiter+feeling
    #sns send sendString
        respTwo=response = client.publish(
    TopicArn='arn:aws:sns:us-west-2:342969397842:MiniHw2',
    Message=sendString,
)
        print sendString
