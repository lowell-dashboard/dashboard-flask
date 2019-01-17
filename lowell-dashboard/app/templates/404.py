{% extends "appbuilder/base.html" %}

{% block head_meta %}
	<meta charset='utf-8'>
  <title>404 Lowell Help Forum 404</title>
  <meta name="description" content="Lowell Help Forum 404 page.">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1">
{% endblock %}

{% block head_css%}
  {{ super() }}
  <link rel="stylesheet" type="text/css" href="../static/css/all.css">
  <link rel="stylesheet" type="text/css" href="../static/css/404.css">
	<link href="https://fonts.googleapis.com/css?family=Montserrat:700,900" rel="stylesheet">
{% endblock %}

{% block content %}
	<div class="body">

		<div id="notfound">
			<div class="notfound">
				<div class="notfound-404">
					<h1>404</h1>
					<h2>Page not found</h2>
				</div>
				<a href="/">Homepage</a>
			</div>
		</div>

	</div><!-- This templates was made by Colorlib (https://colorlib.com) -->
{% endblock %}
