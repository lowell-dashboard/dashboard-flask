{% extends "appbuilder/base.html" %}

{% block head_meta %}
  <title>Lowell Help Forum Schedules</title>
  <meta name="description" content="Lowell Help Forum Schedule Resource Page.">
  <meta charset='utf-8'>
{% endblock %}

{% block head_css %}
	{{ super() }}
  <link rel="stylesheet" type="text/css" href="../static/css/all.css">
{% endblock %}

{% block content %}
  {% for items in schedule_data %}
    <p>{{schedule_data}}</p>
  {% endfor %}
{% endblock %}
