import os
import secrets

from flask import url_for, current_app
from flask_mail import Message
from PIL import Image

from flaskblog import mail

def save_picture(form_picture):
    random_hex = secrets.token_hex(8) # 8 for 8 bytes. This is to ensure that the picture name won't be a duplicate of what we already have. 
    _, file_ext = os.path.splitext(form_picture.filename)
    picture_file_name_ext = random_hex + file_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pictures', picture_file_name_ext)

    # resize image before saving using the Pillow Library
    output_size = (125, 125)
    image = Image.open(form_picture)
    image.thumbnail(output_size)
    image.save(picture_path)
    return picture_file_name_ext


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message(subject='Password Reset Request', 
                recipients=[user.email], 
                sender='noreply@olumodemo.com')
    msg.body = f'''To reset your password, visit the following link:
{url_for('users.reset_request_token', token=token, _external=True)}
PS: If you did not make this request then simply ignore this email and no changes will be made.
'''
    mail.send(msg)