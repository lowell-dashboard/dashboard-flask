{% extends "appbuilder/base.html" %}

{% block head_meta %}
  <title>Lowell Help Forum Textbooks</title>
  <meta name="description" content="Lowell Help Forum Textbook Resource Page.">
  <meta charset='utf-8'>
{% endblock %}

{% block head_css%}
  {{ super() }}
  <link rel="stylesheet" type="text/css" href="../static/css/all.css">
{% endblock %}

{% block content %}
    <h1>{{_("Lowell Textbooks")}}</h1>
{% endblock %}
