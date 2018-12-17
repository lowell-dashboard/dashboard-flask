from flask_appbuilder import IndexView
from flask import g, url_for, redirect
from flask_appbuilder import expose
# File to display custom made index.html

class MyIndexView(IndexView):

	@expose('/')
	def index(self):
		user = g.user
		if user.is_anonymous:
			return redirect(url_for('AuthDBView.login'))
		else:
			# user is authenticated and has an account
			return redirect(url_for('HomeView.general'))

