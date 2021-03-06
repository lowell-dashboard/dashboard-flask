{% extends "appbuilder/base.html" %}

{% block head_meta %}
  <title>Lowell Help Forum Privacy Policy</title>
  <meta name="description" content="Lowell Help Forum Privacy Policy.">
  <meta charset='utf-8'>
{% endblock %}

{% block head_css%}
  {{ super() }}
  <link rel="stylesheet" type="text/css" href="../static/css/all.css">
{% endblock %}

{% block content %}
    <div class="jumbotron">
      <div class="container">
        <center>
          <h1>{{_("Lowell Help Forum Privacy Policy")}}</h1>
          <p>{{_("Privacy Policy being made")}}</p>
        </center>
      </div>
    </div>
{% endblock %}
