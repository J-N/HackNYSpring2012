<?php
include('../ytShit/parse.php');
if(isset($_POST['ytHash']))
{
	$hash = $_POST['ytHash'];
	//echo "Your hash was $hash \n\n";
	$ytUrl = "http://www.youtube.com/watch?v=$hash";
	//echo "url: $ytUrl\n\n";
	
	$wget = "wget -O /var/www/watch?v=$hash $ytUrl";
	//echo $wget;
	system($wget);

	$song = getSong();
	$artist = getArtist();
	//echo "Song: " . getSong(). " Artist: " . getArtist()."<br />";
	killFile();

	$insertString = "cd /var/www ; python -c 'import userInput; userInput.addSong(\"$hash\",\"$song\",\"$artist\")'";
	//echo"ins string: $insertString";

	system($insertString);

}
else
{
?>

<html>
<body>
<center>
Yo give me a youtube hash: <br/><br/>
<form method='POST' action'#'>
<input type='text' name='ytHash'/>
<input type='submit' value='Submit that shit'>
</form>
</center>
</body>
</head>

<?
}
?>
