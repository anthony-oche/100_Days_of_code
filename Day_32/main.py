import pandas
import datetime as dt
import random
import smtplib

my_email = "ocheanthonyowoicho@gmail.com"
password = "phvvqbwuzakvhhma"
now = dt.datetime.now()
today = (now.month, now.day)

data = pandas.read_csv("birthdays.csv")
birth_dict = {(data_row["month"],data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birth_dict:
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    birthday_person = birth_dict[today]
    with open(file_path) as letter:
        content = letter.read()
        new_content = content.replace("[NAME]", f"{birthday_person['name']}")

    #sending the letter via mail now
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="rochi.switch@gmail.com",
            msg=f"Subject: BIRTHDAY WISHES\n\n{new_content}"
        )

