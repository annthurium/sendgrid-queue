import requests

from sendgrid.helpers.mail import Mail
from markdown2 import Markdown

def build_title(response):
    title = ''
    taco_components_to_names = {'base_layer': ' with ',
                                'mixin': ' garnished with ',
                                'condiment': ' topped off with ',
                                'seasoning': ' and wrapped in delicious ',
                                'shell': '!'}
    for key, value in taco_components_to_names.items():
        title += f"{response.get(key).get('name')}{value}"
    
    return title

def get_html_content():
    url = 'http://taco-randomizer.herokuapp.com/random/'
    response = requests.get(url).json()

    taco_components = ['base_layer', 'mixin',
                       'condiment', 'seasoning', 'shell']
    html_content = f"<strong> Here's a taco recipe! {build_title(response)} </strong>\n"
    markdowner = Markdown()

    for component in taco_components:
       html_component = markdowner.convert(response.get(component).get('recipe'))
       html_content += f"<p>{html_component}</p>\n"
    return html_content

def send_message(sendgrid_client, email):
    pass
    message = Mail(
        from_email=('tacobot@delicious.ceo', 'Taco Bot'),
        to_emails=email,
        html_content=get_html_content(),
        subject='Delicious tacos 🌮',
    )

    try:
        response = sendgrid_client.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)
