{% extends "appbuilder/base.html" %}

{% block head_meta %}
  <title>Profile Page</title>
  <meta name="description" content="Profile">
  <meta charset='utf-8'>
  <meta http-equiv="Content-Type" content="text/html">
  <link rel="stylesheet" type="text/css" media="all" href="/static/css/profile.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
{% endblock %}

{% block content %}

<div id="w">
<div id="content" class="clearfix">
  <div id="userphoto"><img src="/static/img/avatar.png" alt="default avatar"></div>
  <h1>{{user.username}}'s Profile</h1>

  <nav id="profiletabs">
    <ul class="clearfix">
      <li><a href="#bio" class="sel">Overview</a></li>
      <li><a href="#activity">Classes</a></li>
      <li><a href="#friends">Discussions</a></li>
      <li><a href="#settings">Settings</a></li>
    </ul>
  </nav>
  
  <section id="bio">    
    <p>Account created on: {{user.created_on}}</p>
    <p>Active: {{user.active}}</p>
    <p>Roles: {{user.roles}}</p>
  </section>
  
  <section id="activity" class="hidden">
    <p>Most recent actions:</p>
    <p>Checking {{user.class_ids}}</p>
    {% for id in user.class_ids %}
      <p class="activity">{{id}}</p>
    {% endfor%}
  </section>
  
  <section id="friends" class="hidden">
    <p>Friends list:</p>
    
    <ul id="friendslist" class="clearfix">
      <li><a href="#"><img src="/static/img/avatar.png" width="22" height="22"> Username</a></li>
      <li><a href="#"><img src="/static/img/avatar.png" width="22" height="22"> SomeGuy123</a></li>
      <li><a href="#"><img src="/static/img/avatar.png" width="22" height="22"> PurpleGiraffe</a></li>
    </ul>
  </section>
  
  <section id="settings" class="hidden">
    <p>Edit your user settings:</p>
    
    <p class="setting"><span>E-mail Address <img src="/static/img/edit.png" alt="*Edit*"></span> lolno@gmail.com</p>
    
    <p class="setting"><span>Language <img src="/static/img/edit.png" alt="*Edit*"></span> English(US)</p>
    
    <p class="setting"><span>Profile Status <img src="/static/img/edit.png" alt="*Edit*"></span> Public</p>
    
    <p class="setting"><span>Update Frequency <img src="/static/img/edit.png" alt="*Edit*"></span> Weekly</p>
    
    <p class="setting"><span>Connected Accounts <img src="/static/img/edit.png" alt="*Edit*"></span> None</p>
  </section>
</div><!-- @end #content -->
</div><!-- @end #w -->
<script type="text/javascript">
$(function(){
  $('#profiletabs ul li a').on('click', function(e){
    e.preventDefault();
    var newcontent = $(this).attr('href');
    
    $('#profiletabs ul li a').removeClass('sel');
    $(this).addClass('sel');
    
    $('#content section').each(function(){
      if(!$(this).hasClass('hidden')) { $(this).addClass('hidden'); }
    });
    
    $(newcontent).removeClass('hidden');
  });
});
</script>
{% endblock %}