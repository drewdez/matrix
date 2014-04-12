from flask import Flask, url_for, flash, render_template, redirect, request, session, g
from app import app, db
from forms import SampleForm
from models import User, ROLE_USER, ROLE_ADMIN

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html',
		title = 'Home')