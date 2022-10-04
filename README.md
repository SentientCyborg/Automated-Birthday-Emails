# Automated-Birthday-Emails
Can send a random birthday email on someone's birthday. Birthdays are tracked via a spreadsheet.


To setup, first enter update the following constants with your information: 

![info](https://github.com/SentientCyborg/Automated-Birthday-Emails/blob/main/images/info_to_update.png)

All constants should be strings.

For MY_RELAY, this information will be different for every email provider. Read through your provider's documentation if you are not sure. 
The SMTP relay for gmail is "smtp.gmail.com".

The PASSWORD may be your email account password, or another password specific to your app that has to be generated in your email account settings. If this is the case,
be sure to use the app password and not the actual email password. 

The SENDER should be the name of the person the email will be from.

To populate birthdays, input data into the csv file: 

![info](https://github.com/SentientCyborg/Automated-Birthday-Emails/blob/main/images/excel_example.png)

Names will appear on the letter exactly as they are entered on the spreadsheet. Do not change any of the headers. 

---

This code was written as part of the instructor guided assignments on day 32 of the Udemy course [100 Days of Code by Dr. Angela Yu](https://www.udemy.com/course/100-days-of-code/). 
This code is different from the answer that was discussed in the lessons. 

---Built using Python 3.8.6
