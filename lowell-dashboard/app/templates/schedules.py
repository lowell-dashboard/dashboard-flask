{% extends "appbuilder/base.html" %}

{% block head_js %}
    {{ super() }}
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <!-- <script src="{{url_for('static',filename='js/schedules.js')}}"></script> -->
{% endblock %}

{% block head_meta %}
  <title>Lowell Help Forum Schedules</title>
  <meta name="description" content="Lowell Help Forum Schedule Resource Page.">
  <meta charset='utf-8'>
{% endblock %}

{% block head_css %}
	{{ super() }}
  <link rel="stylesheet" type="text/css" href="../static/css/all.css">
	<link rel="stylesheet" href="../static/css/schedules.css"></link>
	<style type="text/css">
		.main a:hover{text-decoration:none!important;}
		.main ul{list-style-type: none!important;}
		@media only screen and (min-width: 800px){
	  .cd-schedule .events{float:left; width:100%;}
	  .cd-schedule .events .events-group{width:20%; float:left; border:1px solid #EAEAEA; margin-bottom:0;}
	  .cd-schedule .events .events-group:not(:first-of-type){border-left-width:0;}
	  .cd-schedule .events .top-info{display:table; height:50px; border-bottom:1px solid #EAEAEA; padding:0;}
	  .cd-schedule .events .top-info>span{display:table-cell; vertical-align:middle; padding:0 .5em; text-align:center; font-weight:normal; margin-bottom:0;}
	  .cd-schedule .events .events-group>ul{height:1150px; display:block; overflow:visible; padding:0;}
	  .cd-schedule .events .events-group>ul::after{clear:both;content:""; display:block;}
	  .cd-schedule .events .events-group>ul::after{display:none;}
	  .cd-schedule .events .single-event{position:absolute; z-index:3; width:calc(100% + 2px);left:-1px; box-shadow:0 10px 20px rgba(0,0,0,0.1),inset 0 -3px 0 rgba(0,0,0,0.2); -ms-flex-negative:1; flex-shrink:1; height:auto; max-width:none; margin-right:0;}
	  .cd-schedule .events .single-event a{padding:1.2em;}
	  .cd-schedule .events .single-event:last-of-type{margin-right:0;}
	  .cd-schedule .events .single-event.selected-event{visibility:hidden;}
	}
	</style>
{% endblock %}

{% block content %}
<div class="main">
<div class="main2">
  <h1>{{_("Lowell Schedules")}}</h1>
	<br/>
	<div class="cd-schedule loading">
		<div class="timeline">
			<ul>
				<li><span>07:00</span></li>
				<li><span>07:30</span></li>
				<li><span>08:00</span></li>
				<li><span>08:30</span></li>
				<li><span>09:00</span></li>
				<li><span>09:30</span></li>
				<li><span>10:00</span></li>
				<li><span>10:30</span></li>
				<li><span>11:00</span></li>
				<li><span>11:30</span></li>
				<li><span>12:00</span></li>
				<li><span>12:30</span></li>
				<li><span>1:00</span></li>
				<li><span>1:30</span></li>
				<li><span>2:00</span></li>
				<li><span>2:30</span></li>
				<li><span>3:00</span></li>
				<li><span>3:30</span></li>
				<li><span>4:00</span></li>
				<li><span>4:30</span></li>
				<li><span>5:00</span></li>
				<li><span>5:30</span></li>
				<li><span>6:00</span></li>
			</ul>
		</div> <!-- .timeline -->

		<div class="events">
			<ul>
				{% set days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"] %}
				{% for i in range(5) %}
					<li class="events-group">
						<div class="top-info"><span>{{ days_of_week[i] }}</span></div>
						<ul>
							{% set count = namespace(value=1) %}
							{% for event in table[i] %}
								{% if (loop.index == 5) %}
									<li class="single-event" data-start="{{event['StartTime']}}" data-end="{{event['EndTime']}}" data-content="event-abs-circuit" data-event="event-1">
										<a href="#0">
											<em class="event-name">Block Registry</em>
										</a>
									</li>
								{% elif (table[i]|length == 1) %}
									<li class="single-event" data-start="{{event['StartTime']}}" data-end="{{event['EndTime']}}" data-content="event-abs-circuit" data-event="event-1">
										<a href="#0">
											<em class="event-name">{{_("See announcements for more infomation on the current schedule")}}</em>
										</a>
									</li>
								{% else %}
									<li class="single-event" data-start="{{event['StartTime']}}" data-end="{{event['EndTime']}}" data-content="event-abs-circuit" data-event="event-1">
										<a href="#0">
											<em class="event-name">Block {{ count.value }}</em>
										</a>
									</li>
									{% set count.value = count.value + 1 %}
								{% endif %}
							{% endfor %}
						</ul>
					</li>
				{% endfor %}
			</ul>
		</div>

		<div class="event-modal">
			<header class="header">
				<div class="content">
					<span class="event-date"></span>
					<h3 class="event-name"></h3>
				</div>

				<div class="header-bg"></div>
			</header>

			<div class="body">
				<div class="event-info"></div>
				<div class="body-bg"></div>
			</div>

			<a href="#0" class="close"></a>
		</div>

		<div class="cover-layer"></div>
	</div> <!-- .cd-schedule -->
</div>
</div>
<script type="text/javascript" src="../static/js/schedules.js"></script>
{% endblock %}
