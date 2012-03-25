<?php
include("../phpShit/common.h");
if(isset($_GET['g']))
{
	class song{

		var $title;
		var $artist;
	}
	class game{
		var $s1;
		var $s2;
		var $s3;
		var $s4;
		var $s5;
		var $title;
		var $username;

		function game($theUser, $theGame, $h1, $h2, $h3, $h4, $h5)
		{
			$this->title = $theGame;
			$this->username = $theUser;
			$this->s1 = new song($h1);
			$this->s2 = new song($h2);
			$this->s3 = new song($h3);
			$this->s4 = new song($h4);
			$this->s5 = new song($h5);
		}
	}
}

?>

<html>
<head>
 <link href="http://hackerleague.org/assets/application-da9448e0ee4efa1d7b1830eec79bd41e.css" media="all" rel="stylesheet" type="text/css" />
<script type='text/javascript' src="http://player.longtailvideo.com/jwplayer.js"></script>
<script src="http://hackerleague.org/assets/application-8c2b636f01d3b7ed1480810e93baaa2c.js" type="text/javascript"></script>

<script type='text/javascript'>//<![CDATA[ 
window.onload=function(){
	jwplayer('player').setup({
		flashplayer: 'http://player.longtailvideo.com/player.swf',
		autostart: 'true',	
		controlbar: 'none',
		repeat: 'list',
		playlist:
		[{
			file: 'http://www.youtube.com/watch?v=LOZuxwVk7TU', 
			start: '<?php $start = rand(30,120); echo $start; ?>', 
			duration: '<?php echo $start + 10; ?>'
		},{
			file: 'http://www.youtube.com/watch?v=PsO6ZnUZI0g', 
			start: '<?php $start = rand(30,120); echo $start; ?>', 
			duration: '<?php echo $start + 10; ?>'
		},{
			file: 'http://www.youtube.com/watch?v=qrO4YZeyl0I', 
			start: '<?php $start = rand(30,120); echo $start; ?>', 
			duration: '<?php echo $start + 10; ?>'
		},{
			file: 'http://www.youtube.com/watch?v=dQw4w9WgXcQ', 
			start: '<?php $start = rand(30,120); echo $start; ?>', 
			duration: '<?php echo $start + 10; ?>'
		},{
			file: 'http://www.youtube.com/watch?v=SRcnnId15BA', 
			start: '<?php $start = rand(30,120); echo $start; ?>', 
			duration: '<?php echo $start + 10; ?>'
		}]		
	});

	jwplayer().onPlay( function() {  
	var clock = $('.final_countdown .value');
	Application.timer.countdown_from(clock, 10);
});
	//jwplayer().onPause( function() { this.play(); });
	//jwplayer().onComplete( function() { alert("the video is finished!"); });
}//]]>  
$(document).ready(function(){
	//var clock = $('.final_countdown .value');
	//Application.timer.countdown_from(clock, 12);
});

</script>

</head>
<body>
  <div id="player"></div>
<div class="final_countdown">
          <div class="value">
            <div><span class="seconds large">00</span></div>
            <div><span class="milliseconds large">00</span></div>
          </div>
          <div class="key">
            <div><span>Seconds</span></div>
            <div><span>Miliseconds</span></div>
          </div>
	</div>
</div>
<div class="right">
<div id="1"></div>
<div id="2"> </div>
<div id="3"> </div>
<div id="4"> </div>
</div>

</body>

</html>
