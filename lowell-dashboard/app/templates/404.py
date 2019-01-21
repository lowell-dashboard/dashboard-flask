{% extends "appbuilder/base.html" %}

{% block head_meta %}
  <meta charset='utf-8'>
  <title>404 Lowell Help Forum 404</title>
  <meta name="description" content="Lowell Help Forum 404 page.">
  <meta name="viewport" content="width=device-width, initial-scale=1">
{% endblock %}

{% block head_css%}
  {{ super() }}
  <link rel="stylesheet" type="text/css" href="../static/css/all.css">
  <link rel="stylesheet" type="text/css" href="../static/css/404.css">
{% endblock %}

{% block content %}
	<h1>404</h1>
{% endblock %}
