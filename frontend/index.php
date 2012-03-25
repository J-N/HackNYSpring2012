<?php
session_start();
include('../ytShit/parse.php');
include('../phpShit/common.php');
$count = 0;
if(isset($_POST['ytHash']))
{
	$count = $_POST['count'];
	
	$hash = $_POST['ytHash'];
	//echo "Your hash was $hash \n\n";
	$ytUrl = "http://www.youtube.com/watch?v=$hash";
	//echo "url: $ytUrl\n\n";
	
	$wget = "wget -O /var/www/watch?v=$hash $ytUrl";
	//echo $wget;
	system($wget);
	$_SESSION['hashes'][$count]= $hash;

	$song = getSongP();
	$artist = getArtistP();
	//echo "Song: " . getSong(). " Artist: " . getArtist()."<br />";
	killFile();

	$_SESSION['artists'][$count]= $artist;
	$_SESSION['songs'][$count]= $song;
	$insertString = "cd /var/www ; python -c 'import userInput; userInput.addSong(\"$hash\",\"$song\",\"$artist\")'";
	//echo"ins string: $insertString";
	
	system($insertString);
	if($count==4)
	{
		$username = "newPlayer";
		$gamename = "The best game";
		echo "res: " . addGame($username, $gamename, $_SESSION['hashes'][0],$_SESSION['hashes'][1],$_SESSION['hashes'][2], $_SESSION['hashes'][3], $_SESSION['hashes'][4]);	
	$_SESSION['username']=$username;
		$_SESSION['gamename']=$gamename;
	echo"<br/><br/> <a href='play.php'>Start Game! </a>";
	}
	$count++;
}

?>

<html>
<body>
<center>
Yo give me a youtube hash: <br/><br/>
<form method='POST' action'#'>
<input type='text' name='ytHash'/>
<input type='hidden' name='count' value='<?php echo $count; ?>' />
<input type='submit' value='Submit that shit'>
</form>
</center>
</body>
</html>
