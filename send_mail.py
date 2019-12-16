from sendgrid.helpers.mail import Mail, To
from sendgrid import SendGridAPIClient
import os
import requests
import json

# class RecipeItem
#     def __init__(self, type, name, recipe):
#         self.type = type

    

url = 'http://taco-randomizer.herokuapp.com/random/'

res = requests.get(url).json()

def make_email(mixin, condiment, base_layer, seasoning, shell):
    mixin_name = mixin.get('name')
    mixin_recipe = mixin.get('recipe')
    template = f"""
    <Strong>Here's a taco recipe</Strong>
    <p>{mixin_name}: {mixin_recipe}</p>

    """
    return template


email = make_email(res.get('mixin'), res.get('condiment'), res.get(
    'base_layer'), res.get('seasoning'), res.get('shell'))

print(email)

# message = Mail(
#     from_email=('tacobot@delicious.party', 'Taco Bot'),
#     to_emails=['tilde@thuryism.net'], # replace this with your email address
#     html_content=make_email(res.get('mixin'), res.get('condiment'), res.get('base_layer'), res.get('seasoning'), res.get('shell')),
#     subject='Delicious tacos',
# )

# try:
#     sendgrid_client = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
#     response = sendgrid_client.send(message)
#     print(response.status_code)
#     print(response.body)
#     print(response.headers)
# except Exception as e:
#     print(e.message)
