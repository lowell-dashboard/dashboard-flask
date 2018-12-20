from flask_appbuilder import IndexView
from flask import g, url_for, redirect
from flask_appbuilder import expose

# File to display custom made different views based off if user is signed

class MyIndexView(IndexView):

	@expose('/')
	def index(self):
		user = g.user
		if user.is_anonymous:
			return redirect(url_for('HomeView.new'))
		else:
			# user is authenticated and has an account
			return redirect(url_for('HomeView.general'))
