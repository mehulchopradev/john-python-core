class Email:
  def send_email(self):
    print('Making connection with SMTP server')
    print('Email sent to {0}'.format(self.email))
    print('Closing connection to SMTP server')