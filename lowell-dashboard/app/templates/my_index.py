{% extends "appbuilder/base.html" %}

{% block head_meta %}
  <meta name="description" content="Lowell support site to help Lowell students get information easily and remove stress.">
  <meta charset='utf-8'>
{% endblock %}

{% block head_css%}
  {{ super() }}
  <link rel="stylesheet" type="text/css" href="../static/css/all.css">
{% endblock %}

{% block content %}
<div class="jumbotron">
  <div class="container">
    <center><h1>{{_("Lowell Help Forum")}}</h1></center>
  </div>
</div>
{% endblock %}
