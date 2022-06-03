from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_welcome_email(name, receiver):
    # Creating message subject and sender
    subject='Welcome to the Moringa Tribune Newsletter'
    sender='testingkuchunguza@gmail.com'

    #passing in the context variables
    text_content=render_to_string('email/newsemail.txt', {'name':name})
    html_content=render_to_string('email/newsemail.html', {'name':name})

    # EMA for sending email
    msg=EmailMultiAlternatives(subject,text_content,sender,[receiver])
    
    #attach the HTML template alternative for the times the User logs in to the email with basic html
    msg.attach_alternative(html_content,'text/html')
    msg.send()