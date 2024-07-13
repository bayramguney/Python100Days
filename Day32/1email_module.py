import smtplib

my_email = "appbreweyinfo@gmail.com"
password = "vencgtrtyyuewfghy"    # from google 2 way setting
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(from_addr=my_email,to_addrs="appbrewerytesting@yahoo.com",msg="Subject:Hello\n\nThis is the body "
                                                                                      "of the email")
