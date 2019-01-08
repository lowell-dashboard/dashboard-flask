# Import flask functions for redirecting and getting user status
from flask import g, url_for, redirect
# Import IndexView class to overwrite files/redirects and expose to expose custom index view
from flask_appbuilder import IndexView, expose

# File to display custom made different views based off if user is signed

class MyIndexView(IndexView):

    # Checking user and redirecting for user when user goes to index view
	@expose('/')
	def index(self):

		# Get user status
		user = g.user

		# Check user
		if user.is_anonymous:
			# user is not authenticated and gets redirected to New user page
			return redirect(url_for('HomeView.new'))
		else:
			# user is authenticated and has an account redirect to General page
			return redirect(url_for('HomeView.general'))
