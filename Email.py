import smtplib
import datetime

class Email(object):
    def email_when_complete(self):
        try:
            with smtplib.SMTP('smtp.office365.com', 587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.ehlo()

                smtp.login('contact@ukrainianrestoration.com', 'gr838083!')
    
                subject = 'Finished New Jersey Verification'
                datetime_object = datetime.datetime.now() 
                body = 'New jersey Verification has been completed at ' + str(datetime_object) 

                msg = f'Subject: {subject}\n\n{body}'

                smtp.sendmail('contact@ukrainianrestoration.com', 'u', msg) 
                print("email sent")
        except BaseException:
            print("Did not send email")
            
    def email_when_error(self):
        try:
            with smtplib.SMTP('smtp.office365.com', 587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.ehlo()

                smtp.login('contact@ukrainianrestoration.com', 'gr838083!')
    
                subject = 'Finished New Jersey Verification'
                datetime_object = datetime.datetime.now() 
                body = 'There was an Error: Please check the API' + str(datetime_object) 

                msg = f'Subject: {subject}\n\n{body}'

                smtp.sendmail('contact@ukrainianrestoration.com', 'u', msg) 
                print("email sent")
        except BaseException:
            print("Did not send email")
            
        
        
    
