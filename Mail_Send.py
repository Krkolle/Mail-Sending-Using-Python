#Python Script to send a mail with the help of 'smtplib' and 'email' modules. We can extend the same code to send mails to multiple recepients.
#This can be done by importing the csv. Defining a new function, inside the function, cut paste the below code.
#Then with the help of for loop, we can keep calling the defined function to send mails to each entry in the CSV file.
#Please note that I have tested this script for Gmail only. You are free to use this code to enable sending mails via other providers.

#Note : If you plan on uploading your script to GitHub or any other location, ensure that you don't mention your sender_mail_id and Application_Password in the file.

#If at all you do upload it, those who get access to the repository will be able to send mails using the credentials. #If you face issues while implementing this code, or sending mails to multiple users, feel free to reach out to me at 'krkolle@gmail.com'
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
msg = MIMEMultipart() 
msg['From'] ='sender_address' #Enter sender address here
msg['Subject'] = "type subject here" #Enter subject here 
body = "type_the_email_body_here" #Enter mail content here
msg.attach(MIMEText(body, 'plain'))
p = MIMEBase('application', 'octet-stream') 
s = smtplib.SMTP('smtp.gmail.com', 587) #You dont have to change this if you are sending a mail from GMAIL. Incase of others, find the names of SMTP Servers and the respective ports.
s.starttls()
s.login('sender_address', "application_password") # Generate an app password you have generated from Google. If you don't have one, visit 'https://bit.ly/googleapppasswords' to create one.
text = msg.as_string()
s.sendmail('sender_address', 'to_address', text) 
s.quit() 