# -*- coding: utf-8 -*-

from flask import render_template, current_app, request, redirect, url_for, flash, g

from flask.ext.login import (LoginManager, login_required, 
  logout_user, login_user, current_user)

from models import Test, User


def create_views(app):

  login_manager = LoginManager()
  login_manager.init_app(app)
  login_manager.login_view = 'login'

  @app.before_request
  def before_request():
    g.user = current_user

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
    current_app.db_session.add(user)
    current_app.db_session.commit()

    login_user(user)
    return redirect(request.args.get('next') or url_for('index'))

    #flash('User successfully registered')
    #return redirect(url_for('login'))
 
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

   
    print user
    if user is None or not user.password_ok(password):
      return redirect(url_for('login'))
      print "???"
    #    flash('Username or Password is invalid' , 'error')
      return redirect(url_for('login'))
    login_user(user, remember=remember_me)
    #flash('Logged in successfully')
    return redirect(request.args.get('next') or url_for('trips'))

  @app.route('/logout')
  def logout():
    logout_user()
    return redirect(url_for('index'))   

  @login_manager.user_loader
  def load_user(id):
    return User.query.get(int(id))

  @app.route('/')
  def index():    
    return render_template('index.html')

  @app.route('/editprofile')
  def editprofile():  
    return render_template('index.html')

  @app.route('/trips', methods=['GET', 'POST'])
  @login_required
  def trips():
    return render_template('trips.html')