import smtplib

host = "smtp.gmail.com"
port = 587 # Gmail
# For Yahoo host = 'smtp.mail.yahoo.com', port = 465 or port = 587
# For Outlook host = 'smtp-mail.outlook.com', port = 587

#Enter your email and password
user = 'ramanathan.placement@gmail.com'
password = 'ramanathan0@'
print("Subject? ",end="")
subject = input()
print("Body? ",end="")
lines = []
line=input()
lines.append(line)
text = '\n'.join(lines)
print("Recipient? ",end="")
receiver = input()

message = """From: """+user+"""
To: """+receiver+"""
Subject: """+subject+"""
"""+text

#create smtp object for connection with the server
#connect to gmail's SMTP server with the port provided by google
conn = smtplib.SMTP(host, port)

#identify yourself to ESMPT server
conn.ehlo()

#For Security purpose
conn.starttls()
conn.ehlo()

#Login to the server
conn.login(user, password)
#print(conn.verify(receiver))

#Send Message
conn.sendmail(user, receiver, message)

#Close or Terminate the connection from the server
conn.quit()
print("Email sent!")