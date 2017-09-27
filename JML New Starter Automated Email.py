# JML New Starter Automated Email
# Danny Wade - 22/09/2017 - Version 1.

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

import getpass

print """
This script will automatically send 3 emails with details for:

- Active Directory
- Synergist
- Jira
"""

print """
First we'll start with your admin credentials...

Please enter the following:
"""

admin = raw_input("Username (name.surname): ")
print"\nPassword characters are hidden."
admin_pass = getpass.getpass()

print """

Now for the user's credentials...

Please enter the following:
"""

user_first = raw_input("Full Name: ")
username = raw_input("Username (name.surname): ")
manager = raw_input("Line Manager's Username (name.surname): ")
bit = raw_input("Bitlocker pin: ")

# your email address
fromaddr = "%s@creatormail.co.uk" % (admin)
# new user's email address
toaddr = "%s@creatormail.co.uk" % (username)
# line managers email address
ccaddr = "%s@creatormail.co.uk" % (manager)

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['cc'] = ccaadr
# email subject
msg['Subject'] = "Welcome to ITGCreator!"

# email body
body = """Hi %s,

On behalf of the IT Infrasturcture team, I would like to welcome you to ITG Creator.

Please find your account details below:

Username: %s
Password: Creator123 (You will be prompted to change this upon first login.)
Bitlocker: %s

If you ever require IT related assiatance, you will need to create a service ticket. This is done by emailing: servicedesk@creator.co.uk.

If you have any other questions please don't hesitate to contact us at: infrastructure@creator.co.uk.

Kind Regards,
Infrastructure""" % (user_first, username, bit)

msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.office365.com', 587)
server.starttls()
# email address password
server.login(fromaddr, admin_pass)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()

# your email address
fromaddr = "%s@creatormail.co.uk" % (admin)
# new user's email address
toaddr = "%s@creatormail.co.uk" % (username)
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['cc'] = ccaddr
# email subject
msg['Subject'] = "Your Synergist Account"

# email body
body = """Hi %s,

The link to access Synergist is as follows: 
https://synergist.creator.co.uk

Please find your details below:

Username: %s
Password: Creator123' (You will be prompted to change this upon first login.)

If you have any questions please contact your line manager (%s@creator.co.uk) or servicedesk@creator.co.uk.

Kind Regards,
Infrastructure""" % (user_first, username, manager)

msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.office365.com', 587)
server.starttls()
# email address password
server.login(fromaddr, admin_pass)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()

# your email address
fromaddr = "%s@creatormail.co.uk" % (admin)
# new user's email address
toaddr = "%s@creatormail.co.uk" % (username)
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['cc'] = ccaddr
# email subject
msg['Subject'] = "Your Jira Account"

# email body
body = """Hi %s,

The link to access Jira is as follows: 
https://jira.creator.co.uk

Please find your details below:

Username: %s
Password: (Same as PC login.)

If you have any questions please contact your line manager (%s@creator.co.uk) or servicedesk@creator.co.uk.

Kind Regards,
Infrastructure""" % (user_first, username, manager)

msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.office365.com', 587)
server.starttls()
# email address password
server.login(fromaddr, admin_pass)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()

raw_input("\nPress enter to exit.")