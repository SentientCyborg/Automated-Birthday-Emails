import random
import smtplib
import pandas as pd
import datetime as dt

# Configure this information to your specifics
MY_EMAIL = "******@email.com"
PASSWORD = "****email password****"
MY_RELAY = "****SMTP Relay****"
SENDER = "****Your Name****"

birthdays_data = pd.read_csv("birthdays.csv")
birthdays = birthdays_data.to_dict(orient="records")
today = dt.date.today()
now = dt.datetime.now()

for birthday in birthdays:
    if birthday["day"] == now.day and birthday["month"] == now.month:
        with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as f:
            letter = f.read()
            letter = letter.replace("[NAME]", birthday['name'])
            letter = letter.replace("[SENDER]", SENDER)
            with smtplib.SMTP(host=MY_RELAY, port=587) as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=PASSWORD)
                connection.sendmail(from_addr=MY_EMAIL,
                                    to_addrs=birthday["email"],
                                    msg=f"Subject:Happy Birthday!\n\n{letter}"
                                    )







