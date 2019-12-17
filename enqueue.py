from redis import Redis
from rq import Queue
import os

from build_email import send_message
from sendgrid import SendGridAPIClient

sendgrid_client = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))

q = Queue(connection=Redis())

emails = ['example1@mail.com', 'example2@mail.com', 'tilde@thuryism.net'] #replace these with your email address

for email in emails:
    q.enqueue(send_message, sendgrid_client, email)
