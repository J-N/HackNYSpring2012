<?php
include("../phpShit/common.h");
if(isset($_GET['g']))
{
	class song{

		var $title;
		var $artist;
		var $hash;
		var $wrong1;
		var $wrong2;
		var $wrong3;

		function song($theHash)
		{
			$this->hash = $theHash;
			$this->title = getTitle($theHash);
			$this->artist = getArtist($theHash);
			$this->wrong1 = new song(getWrongTitle($theHash,1),getWrongArtist($theHash,1))
			$this->wrong2 = new song(getWrongTitle($theHash,2),getWrongArtist($theHash,2))
			$this->wrong3 = new song(getWrongTitle($theHash,3),getWrongArtist($theHash,3))
		}
		function song($theTitle, $theArtist)
		{
			$this->title = $theTitle;
			$this->artist = $theArtist;
		}

		public function printFull()
		{
			echo $this->title . " by " . $this->artist;
		}

		public function getHash()
		{
			return $this->hash;
		}
		public function getWrong1()
		{
			return $this->wrong1;
		}

		
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
		public function getSong1()
		{
			return $this->s1;
		}
		public function getSong2()
		{
			return $this->s2;
		}
		public function getSong3()
		{
			return $this->s3;
		}
		public function getSong4()
		{
			return $this->s4;
		}
		public function getSong5()
		{
			return $this->s5;
		}
	}

$game = new game();
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
			file: 'http://www.youtube.com/watch?v=<?php echo $game->getSong1()->getHash(); ?>', 
			start: '<?php $start = rand(30,120); echo $start; ?>', 
			duration: '<?php echo $start + 10; ?>'
		},{
			file: 'http://www.youtube.com/watch?v=<?php echo $game->getSong2()->getHash(); ?>', 
			start: '<?php $start = rand(30,120); echo $start; ?>', 
			duration: '<?php echo $start + 10; ?>'
		},{
			file: 'http://www.youtube.com/watch?v=<?php echo $game->getSong3()->getHash(); ?>', 
			start: '<?php $start = rand(30,120); echo $start; ?>', 
			duration: '<?php echo $start + 10; ?>'
		},{
			file: 'http://www.youtube.com/watch?v=<?php echo $game->getSong4()->getHash(); ?>', 
			start: '<?php $start = rand(30,120); echo $start; ?>', 
			duration: '<?php echo $start + 10; ?>'
		},{
			file: 'http://www.youtube.com/watch?v=<?php echo $game->getSong5()->getHash(); ?>', 
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
<div id="1"><?php game->getSong1()->getWrong1()->printFull(); ?></div>
<div id="2"><?php game->getSong1()->getWrong2()->printFull(); ?></div>
<div id="3"><?php game->getSong1()->getWrong3()->printFull(); ?></div>
<div id="4"><?php game->getSong1()->printFull(); ?></div>
</div>

</body>

</html>
