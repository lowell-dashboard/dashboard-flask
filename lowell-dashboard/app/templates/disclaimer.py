{% extends "appbuilder/base.html" %}

{% block head_meta %}
  <title>Lowell Help Forum Disclaimer</title>
  <meta name="description" content="Lowell Help Forum Disclaimer.">
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

          <h1>{{_("Lowell Help Forum Disclaimer")}}</h1>
          <p>{{_("We are in no way run by or affiliated with Lowell High school")}}</p>
          <p>{{_("in San Francisco. This site was created by Lowell students")}}</p>
          <p>{{_("for Lowell students. If there is ever a bug or something a")}}</p>
          <p>{{_("problem that needs to reported, use the websites report function")}}</p>
          <p>{{_("and do not ask Lowell school staff for help with this website")}}</p>

        </center>
      </div>
    </div>
{% endblock %}
