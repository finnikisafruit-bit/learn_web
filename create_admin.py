import sys
from getpass import getpass

from webapp import create_app
from webapp.db import db
from webapp.user.models import User

app = create_app()

with app.app_context():
    username = input("Введите логин: ")

    if User.query.filter_by(username=username).first():
        print("Пользователь с таким логином уже существует")
        sys.exit(0)

    password1 = getpass("Введите пароль: ")
    password2 = getpass("Повторите пароль: ")

    if password1 != password2:
        print("Пароли не одинаковые")
        sys.exit(0)

    new_user = User(username=username, role="admin")
    new_user.set_password(password1)

    db.session.add(new_user)
    db.session.commit()
    print(f"Создан администратор с id={new_user.id}")
