from django.core.mail import send_mail as mail_sender
from django.template.loader import render_to_string
from django.conf import settings as django_settings


def send_mail(*args, render_kwargs={}, **kwargs):
    mail_sender(
        *args, 
        html_message=render_to_string(
            **render_kwargs
        ),
        **kwargs
    )

    need_copy = False
    for email in kwargs.get('recipient_list', []):
        if not 'softserveinc.com' in email:
            need_copy = True
            
    if need_copy:
        kwargs['recipient_list'] = django_settings.EMAIL_COPY_EMAILS
        render_kwargs['context'].update(
            django_settings.EMAIL_COPY_EMAIL_REPLACE
        )
        mail_sender(
            *args, 
            html_message=render_to_string(
                **render_kwargs
            ),
            **kwargs
        )
        
