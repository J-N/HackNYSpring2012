<?php

$title = system("grep eow-title watch*");
$search = "title=";
$pos = strpos($title, $search);
$pos2 = strpos($title, " - ");
$length = $pos2- ($pos+7);
print("pos = $pos pos2= $pos2 length = $length\n");
$artist = substr($title, $pos+7, $length);

$song = substr($title, $pos2+3,-2);

//$artist = substr($artist
print ("The artist: $artist the song: $song\n");
system("rm watch*");
?>
