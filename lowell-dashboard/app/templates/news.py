{% extends "appbuilder/base.html" %}

{% block head_meta %}
  <title>Lowell Help Forum News</title>
  <meta name="description" content="Lowell Help Forum News Page.">
  <meta charset='utf-8'>
{% endblock %}

{% block head_css%}
  {{ super() }}
  <link rel="stylesheet" type="text/css" href="../static/css/all.css">
  <link rel="stylesheet" type="text/css" href="../static/css/news.css">
  <link rel="stylesheet" type="text/css" href="../static/js/news.js">
{% endblock %}

{% block content %}
  <div class="body">
    <div class="container">
      <div class="row">
        <center>
          <h1>{{_("Lowell News")}}</h1>

          <div class="col-xs-4">
          </div>
          <div class="col-xs-4">
          </div>

          <div class="col-xs-4">
            <a class="btn btn-success btn-sm" href="/news/form" role="button">{{_("Create News")}}</a>
          </div>
        </center>
      </div>

      {% for n in news %}
        <div class="announcements">
          <center><h2>{{n.title}}</h2></center>
          <br>
          <p style="white-space: pre-line;">{{n.news}}</p>
          <h5>{{n.made_by_message}}{{n.creator_username}} about {{timestamps[loop.index-1]}} {{time_unit[loop.index-1]}} ago</h5>
        </div>
        <br>
      {% endfor %}

      {% if news|length == 0 %}
        <p>There are no announcements</p>
      {% endif %}

    </div>
  </div>
{% endblock %}
