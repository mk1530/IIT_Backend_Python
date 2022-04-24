#!C:\Program Files\Python37\python.exe
import flask
import os
import logging

from flask import Flask, render_template, flash, redirect, make_response
from forms import RegistrationForm, LoginForm
#from pydrop.config import config
from werkzeug.utils import secure_filename
from flask import redirect, request, jsonify, url_for,Blueprint
import flask_login



app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

my_database={}

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')



@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    global my_database
    if form.validate_on_submit():
        if form.email.data in my_database:
            flash('Email ID already exists!', 'danger')
            return redirect(url_for('register'))
        my_database[form.email.data]={}
        my_database[form.email.data]['uid']=form.username.data
        my_database[form.email.data]['pwd']=form.password.data
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('user',username=form.username.data))
    return render_template('register.html', title='Register', form=form)


@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():

    return render_template('dashboard.html', title='Login')

@app.route("/logout", methods=['GET'])
def logout():

    return render_template('logout.html', title='logout')


@app.route("/upload", methods=['GET', 'POST'])
def upload():

    return render_template('upload.html', title='Login')


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if (form.email.data in my_database) and (form.password.data == my_database[form.email.data]['pwd']):
            flash('You have been logged in!', 'success')
            return redirect(url_for('user', username=my_database[form.email.data]['uid']))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/user/<username>", methods=['GET'])
def user(username):
    #print(username)
    return render_template('user.html',username=username)



if __name__ == '__main__':
    app.debug = True
    app.run()

