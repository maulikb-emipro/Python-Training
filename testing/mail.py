import smtplib, ssl

port = 465  # For SSL
password = input("Type your password and press enter: ")

# Create a secure SSL context
context = ssl.create_default_context()

sender_email = "testingemipro@gmail.com"
receiver_email = "maulikb@emiprotechnologies.com"
message = """\
Subject: Hi there

This message is sent from Python."""

# PYTHON 3
# with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
#     server.login(sender_email, password)
#     server.sendmail(sender_email,receiver_email,message)

s = smtplib.SMTP(host='smtp.gmail.com', port=25)
s.starttls()
s.login(sender_email, password)

s.sendmail(sender_email, receiver_email, message)
s.quit()
