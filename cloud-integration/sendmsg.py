from google.cloud import pubsub_v1
from google.cloud import bigquery
import datetime
import json
import os
import time

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '<your credentials json file>'

def send_data(data):
    project_id = "<project id>" # enter your project id here
    topic_name = "<topicname>" # enter the name of the topic that you created

    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_name)

    futures = dict()

    def get_callback(f, data):
        def callback(f):
            try:
                # print(f.result())
                futures.pop(data)
            except:
                print("Please handle {} for {}.".format(f.exception(), data))

        return callback

    time.sleep(3)   
    print(data)
    # When you publish a message, the client returns a future.
    future = publisher.publish(
        topic_path, data=(json.dumps(data)).encode("utf-8")) # data must be a bytestring.
    # Publish failures shall be handled in the callback function.
    future.add_done_callback(get_callback(future, data))
    # Wait for all the publish futures to resolve before exiting.
    while futures:
        time.sleep(5)

    print("Published message with error handler.")

def get_data():
    client = bigquery.Client()
    QUERY = (
    '<your SQL query>')
    query_job = client.query(QUERY)  # API request
    rows = query_job.result()  # Waits for query to finish
    rows = list(rows)
    
    return rows

