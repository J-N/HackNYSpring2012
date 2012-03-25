<?php

function getArtist()
{
$title = system("grep eow-title /var/www/watch*");
$search = "title=";
$pos = strpos($title, $search);
$pos2 = strpos($title, " - ");
$length = $pos2- ($pos+7);
//print("pos = $pos pos2= $pos2 length = $length\n");
$artist = substr($title, $pos+7, $length);
	return $artist;
}
function getSong()
{
$title = system("grep eow-title /var/www/watch*");
$search = "title=";
$pos = strpos($title, $search);
$pos2 = strpos($title, " - ");
$length = $pos2- ($pos+7);
//print("pos = $pos pos2= $pos2 length = $length\n");
//$artist = substr($title, $pos+7, $length);
$song = substr($title, $pos2+3,-2);
	return $song;
}

//$artist = substr($artist
//print ("The artist: $artist the song: $song\n");
function killFile()
{
	system("rm /var/www/watch*");
}
?>
