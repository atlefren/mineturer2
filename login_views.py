# -*- coding: utf-8 -*-

from flask import (redirect, url_for, request, render_template, current_app,
                   flash)
from flask.ext.login import (LoginManager, logout_user, login_user,
                             current_user)

from models import User, get_user_by_username


def create_login_views(app):

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    @app.route('/register', methods=['GET', 'POST'])
    def register():

        if current_user.is_authenticated():
            return redirect(url_for('editprofile'))

        if request.method == 'GET':
            return render_template('register.html', user=User(), errors={})

        user = User(
            request.form['username'],
            request.form['password'],
            request.form['password2'],
            request.form['email'],
            request.form['fullname']
        )

        if user.validate():

            user.enabled = True
            current_app.db_session.add(user)
            current_app.db_session.commit()

            login_user(user)
            flash(u'Du har nå opprettet en bruker!')
            return redirect(request.args.get('next') or url_for('index'))
        else:
            return render_template(
                'register.html',
                errors=user.validation_errors,
                user=user
            )

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'GET':
            return render_template('login.html')
        username = request.form['username']
        password = request.form['password']

        remember_me = False
        if 'remember_me' in request.form:
            remember_me = True

        user = get_user_by_username(username)

        if user is None or not user.password_ok(password):
            return redirect(url_for('login'))
        login_user(user, remember=remember_me)
        return redirect(request.args.get('next') or url_for('trips'))

    @app.route('/logout')
    def logout():
        logout_user()
        return redirect(url_for('index'))

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
