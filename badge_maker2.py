from PIL import Image, ImageFont, ImageDraw
from datetime import date, timedelta

import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path

import schedule
import time

def job():
    badges = {"dylan.PNG":"dpelissiry@gmail.com", "chris.PNG":"chnton@ucsc.edu"}
    for badge, email_user in badges.items():
        today = date.today()
        end = date.today() + timedelta(days=6)
        end_format = end.strftime("%#m/%#d/%Y")
        format_date = today.strftime("%#m/%#d/%Y")
        time = "8:00"
        time2 = "10:00"
        morn = "AM"
        txt = "Next Lab Test Due:"

        

        badge_img = Image.open(badge)
        y_coord = 170


        font = ImageFont.truetype('arialbd.ttf', 53, encoding="unic")
        font2 = ImageFont.truetype('arialbd.ttf', 31, encoding="unic")
        d1 = ImageDraw.Draw(badge_img)
        d1.text((200, y_coord), format_date, font=font, fill=(255,255,255))
        d1.text((560, y_coord), morn, font=font, fill=(255,255,255))
        d1.text((445, y_coord), time, font=font, fill=(255,255,255))

        d1.text((415, 1025), end_format, font = font2, fill = (255,255,255))
        d1.text((120, 1025), txt, font = font2, fill = (255,255,255))
        d1.text((565, 1025), time2, font = font2, fill = (255,255,255))
        d1.text((650, 1025), morn, font = font2, fill = (255,255,255))
        #badge_img.show()
        badge_img.save("orig_badge_new.PNG")

        email = "daily.badge.mailer@gmail.com"
        pwd = "w78H4vkpuDvr&h@G"
        send_to_email = email_user
        subject = "Daily Badge"
        message = 'test'
        file = "C:\\Users\\dpeli\\OneDrive\\Python\\COVID Badge\\orig_badge_new.PNG"

        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = send_to_email
        msg['Subject'] = subject

        #msg.attach(MIMEText(message, 'plain'))

        filename = os.path.basename(file)
        attachment = open(file, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename = %s" % filename)

        msg.attach(part)

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, pwd)
        text = msg.as_string()
        server.sendmail(email, send_to_email, text)
        server.quit()

job()

#828x1438 




##if __name__ == "__main__":
##    schedule.every().day.at("08:00").do(job)
##
##    while True:
##        schedule.run_pending()
##        time.sleep(59)

