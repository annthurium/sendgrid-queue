from sendgrid.helpers.mail import Mail, To
from sendgrid import SendGridAPIClient
import os
import requests
import json
from markdown2 import Markdown
    

url = 'http://taco-randomizer.herokuapp.com/random/'

response = requests.get(url).json()

def make_email(response):
    taco_components = ['base_layer', 'mixin',
                       'condiment', 'seasoning', 'shell']
    template = "<strong> Here's a taco recipe! </strong>\n"
    markdowner = Markdown()

    for component in taco_components:
       html_content = markdowner.convert(response.get(component).get('recipe'))
       template += f"<p>{html_content}</p>\n"
    return template

html_content = make_email(response)

message = Mail(
    from_email=('tacobot@delicious.party', 'Taco Bot'),
    to_emails=['tilde@thuryism.net'], # replace this with your email address
    html_content=html_content,
    subject='Delicious tacos',
)

try:
    sendgrid_client = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sendgrid_client.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e)
