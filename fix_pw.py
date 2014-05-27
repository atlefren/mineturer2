# -*- coding: utf-8 -*-
import os

import bcrypt

from app import create_app
from models import User

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    db = os.environ.get('DATABASE_URL', 'sqlite:////tmp/mineturer.db')
    app = create_app(os.environ.get('DEBUG', False), db)

    for user in app.db_session.query(User).all():
        user.bcrypt_pwd = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
        app.db_session.add(user)
    app.db_session.commit()      