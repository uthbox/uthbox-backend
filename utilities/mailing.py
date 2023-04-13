import os
import requests
from django.utils.safestring import mark_safe
from dotenv import load_dotenv

load_dotenv()


def enviar_verificacion(correo, user_id):
    """
        DOCSTRING: funcion responsable de construir y enviar el correo de verificacion de identidad
    """
    requests.post(
        "https://api.mailgun.net/v3/{}/messages".format(os.getenv('MAILGUN_DOMAIN')),
        auth=("api", "{}".format(os.getenv('MAILGUN_API_KEY'))),
        data={"from": "Verificacion de Identidad - UTHShare <mailgun@{}>".format(os.getenv('MAILGUN_DOMAIN')),
              "to": [correo],
              "subject": "Verificacion de Identidad",
              "text": "Testing some Mailgun awesomness!",
              "html": '<html>Gracias por utilizar UTHShare, para seguir utilizando nuestro servicio es necesario su '
                      'verificacion de identidad, por favor abrir el siguiente link para realizar dicha operacion '
                       '<a href="https://www.api.katiosca.com/auth/verificacion/{}">https://www.api.katiosca.com/auth/verificacion/{}</a></html>'.format(user_id, user_id)})