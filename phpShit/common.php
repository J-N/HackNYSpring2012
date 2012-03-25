<?php

function addGame($userName, $gameName, $s1, $s2, $s3, $s4, $s5)
{
	$string = "cd /var/www/ ; python -c 'import userInput; userInput.insertGame(userInput.getGame(\"$userName\",\"$gameName\",\"$s1\",\"$s2\",\"$s3\",\"$s4\",\"$s5\"))'";

	return system($string);
}


function getTitle($hash)
{
	$string = "cd /var/www/ ; python -c 'import userInput; userInput.getTitle(\"$hash\")'";

	return system($string);
}

function getArtist($hash)
{
	$string = "cd /var/www/ ; python -c 'import userInput; userInput.getArtist(\"$hash\")'";

	return system($string);
}
function getWrongTitle($hash, $num)
{
	$string = "cd /var/www/ ; python -c 'import userInput; userInput.getIncorrectAnswers(\"$hash\")'";
	$result = system($string);
	$split = explode(",", $result);
	return $split[(2*$num)-2];
}
function getWrongArtist($hash, $num)
{
	$string = "cd /var/www/ ; python -c 'import userInput; userInput.getIncorrectAnswers(\"$hash\")'";
	$result = system($string);
	$split = explode(",", $result);
	return $split[(2*$num)-1];
}

function getAllHints($username, $gamename)
{
	$string = "cd /var/www/ ; python -c 'import userInput; userInput.getAllHints(\"$username\", \"$gamename\")'";
	$result = system($string);
	$split = explode(",", $result);
	//return $split[(2*$num)-1];
	echo $result;
}

//getAllHints("Player2", "The Test Game2");
?>
