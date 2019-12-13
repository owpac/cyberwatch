from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools
from email.mime.text import MIMEText
from base64 import urlsafe_b64encode

from options import Options

SENDER = Options.SENDER_MAIL
RECIPIENT = Options.RECIPIENT
SUBJECT = Options.SUBJECT
CONTENT = Options.CONTENT
SCOPE = 'https://www.googleapis.com/auth/gmail.compose'  # Allows sending only, not reading


# Initialize the object for the Gmail API
# https://developers.google.com/gmail/api/quickstart/python
class Gmail:
    def __init__(self):
        store = file.Storage('credentials.json')
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets('client_secret.json', SCOPE)
            creds = tools.run_flow(flow, store)
        service = discovery.build('gmail', 'v1', http=creds.authorize(Http()))

    # https://developers.google.com/gmail/api/guides/sending
    def create_message(self, sender, to, subject, message_text):
        """Create a message for an email.
        Args:
          sender: Email address of the sender.
          to: Email address of the receiver.
          subject: The subject of the email message.
          message_text: The text of the email message.
        Returns:
          An object containing a base64url encoded email object.
        """
        message = MIMEText(message_text)
        message['to'] = to
        message['from'] = sender
        message['subject'] = subject
        encoded_message = urlsafe_b64encode(message.as_bytes())
        return {'raw': encoded_message.decode()}

    # https://developers.google.com/gmail/api/guides/sending
    def send_message(self, service, user_id, message):
        try:
            message = (self.service.users().messages().send(userId=user_id, body=message)
                       .execute())
            print('Message Id: %s' % message['id'])
            return message

        except:
            print('An error occurred')
