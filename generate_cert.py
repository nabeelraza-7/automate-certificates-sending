"""

author: Nabeel Raza
"""
import pandas as pd
from PIL import Image, ImageDraw, ImageFont 
from send_mails import send_email

fontLoc = 'C:\\Windows\\Fonts\\arial.ttf' # Default location of fonts
arial28 = ImageFont.truetype(fontLoc, 28)

data = pd.read_csv('YOUR_FILE.csv')

def writeName(name, coords=(440, 335), font=arial28):
    """
    Adds text only in the center, change the coords according to your template.
    """
    image = Image.open('YOUR_TEMPLATE.png')
    width, height = image.size
    draw = ImageDraw.Draw(image)
    w, h =  draw.textsize(name, font=arial28)
    draw.text(((width - w)/2,coords[1]), name, fill='black', font=arial28)
    image = image.convert('RGB')
    image.save(name+'.pdf')
    print("Done with: ", name)
    
if __name__ == "__main__":
    # generating certificates of all the names
    for i in data['Name']:
        writeName(i.strip())

    # Preparing to send mail
    from_addr = 'MAIL ADDRESS USED TO SEND MAIL'
    subject = 'SUBJECT'
    login = 'MAIL ADDRESS USED TO SEND MAIL'
    password = 'PASSWORD'
    for i in range(len(data['Email'])):
        name = data['Name'][i]
        filename = name + '.pdf'
        plain_text_body = "Message with the mail"
        send_email(from_addr, [data['Email'][i]],
                    subject,plain_text_body,
                    login,
                    password,
                    smtpserver='smtp.gmail.com:587',
                    attachment=filename,
                    from_name='COMPANY NAME')