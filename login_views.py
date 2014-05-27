# -*- coding: utf-8 -*-

from flask import redirect, url_for, request, render_template, current_app
from flask.ext.login import (LoginManager, login_required, 
  logout_user, login_user, current_user)

from models import User

def create_login_views(app):
    
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    @app.route('/register' , methods=['GET','POST'])
    def register():
        if request.method == 'GET':
            return render_template('register.html')
        user = User(
            request.form['username'],
            request.form['password'],
        request.form['email'],
        request.form['fullname']
        )
        user.enabled = True
        current_app.db_session.add(user)
        current_app.db_session.commit()

        login_user(user)
        return redirect(request.args.get('next') or url_for('index'))
 
    @app.route('/login',methods=['GET','POST'])
    def login():
        if request.method == 'GET':
            return render_template('login.html')
        username = request.form['username']
        password = request.form['password']
    
        remember_me = False
        if 'remember_me' in request.form:
            remember_me = True
        
        user = User.query.filter_by(
            username=username, 
        ).first()
   
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