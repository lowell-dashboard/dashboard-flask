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
    <center>

      <h1>{{_("Lowell Help Forum")}}</h1>
      <br>
      <h3 class="text-info">{{_("Create an account to post and communicate with fellow students")}}</h3>

    </center>
  </div>
</div>

<div class="container">
  <div class="row">
    <div class="col-lg-6">
      <div class="jumbotron">
        <center>

          <h2 class="text-primary">{{_("✅ Register ✅")}}</h2>
          <br>
          <h4>{{_("Don't have an account but want one?")}}</h4>
          <br>
          <a class="btn btn-success btn-block btn-lg" href="/register/form" role="button">{{_("Register Here!")}}</a>

          <br>
        </center>
      </div>
    </div>

    <div class="col-lg-6">
      <div class="jumbotron">
        <center>

          <h2 class="text-primary">{{_("🔒 Login 🔒")}}</h2>
          <br>
          <h4>{{_("Already have an account with us?")}}</h4>
          <br>
          <a class="btn btn-success btn-block btn-lg" href="/login/" role="button">{{_("Login Here!")}}</a>

          <br>
        </center>
      </div>
    </div>
  </div>
</div>

<div class="container">
  <div class="row">
    <div class="col-lg-12">
      <div class="jumbotron">
        <center>

          <h2 class="text-primary">{{_("👓 Just a Viewer 👓")}}</h2>
          <br>
          <h4>{{_("Just want to view data or not create an acount? Click this Button.")}}</h4>
          <h4>{{_("(We do recommend using or creating an account because it allows you more resources from the website)")}}</h4>
          <br>
          <a class="btn btn-success btn-block btn-lg" href="/home/general" role="button">{{_("Be a Viewer")}}</a>

          <br>
        </center>
      </div>
    </div>
  </div>
</div>

<div class="container">
  <div class="row">
    <div class="col-lg-12">
      <div class="jumbotron">
        <center>

          <h2 class="text-primary">{{_("🧱 On the Fence 🧱")}}</h2>
          <br>
          <h4>{{_("Not sure if you should trust us?")}}</h4>
          <h4>{{_("We are Lowell Students and created this site to help remove stress. We will never do anything bad with your information. We also only ask for minimal data from you and keep all your data protected. Check out our Privacy Policy Here.")}}</h4>
          <br>
          <a class="btn btn-success btn-block btn-lg" href="/files/privacy" role="button">{{_("Privacy Policy")}}</a>

          <br>
        </center>
      </div>
    </div>
  </div>
</div>

{% endblock %}
