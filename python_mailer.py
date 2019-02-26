import smtplib
import email.utils as em
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Mailer(object):
    #mail server credentials  
    USERNAME_SMTP = None
    PASSWORD_SMTP = None
    HOST = None
    PORT = None
    EMAIL_BULK = []
    SERVER = None

    def __inti__(self,sender,sender_name,to_mail,subject,**kwargs):
        self.sender
        self.sender_name
        self.to_mail
        self.subject
        self.kwargs
        self.template_name

    #for printing credentials given for reference
    def mail_creds(self):
        print("The username for smtp is %s \n password for smtp is %s \n host for smtp is %s \n port for smtp is %s" %
                (self.USERNAME_SMTP,self.PASSWORD_SMTP,self.HOST,self.PORT))
    # html template assigning and dynamic data passing
    def template_details(self):
        BODY_HTML = open(self.template_name).read().format(**self.kwargs)
        print (BODY_HTML)
    
    def connect_mailer(self):
        try:
           server = smtplib.SMTP(self.HOST, self.PORT)
           server.ehlo()
           server.starttls()
           #stmplib docs recommend calling ehlo() before & after starttls()
           server.ehlo()
           if server.login(self.USERNAME_SMTP, self.PASSWORD_SMTP):
              self.SERVER = server
        except Exception as e:
            print ("Error: ", e)

    def send_mail(self):
        BODY_HTML = open(self.template_name).read().format(**self.kwargs)
        msg = MIMEMultipart('alternative')
        msg['Subject'] = self.subject
        msg['From'] = em.formataddr((self.sender_name,self.sender))
        part2 = MIMEText(BODY_HTML, 'html')
        msg.attach(part2)
        self.SERVER.sendmail(self.sender, self.to_mail, msg.as_string())
    def close_server(self):    
        self.SERVER.close()


a = Mailer()
a.USERNAME_SMTP = ""
a.PASSWORD_SMTP = ""
a.HOST = ""
a.PORT = 587
a.connect_mailer()
a.sender = 'example@example.com'
a.sender_name = "example"
a.subject = "test mail"
a.template_name = "example.html"
EMAIL_BULK = ["email_ids"]
for i in EMAIL_BULK:
    #for passing values to html
    a.kwargs = {"test":i}
    a.to_mail = i
    a.send_mail()

a.close_server
