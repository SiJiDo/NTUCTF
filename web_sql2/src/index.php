<?php
	$dao = mysql_connect("localhost", "root", "root");
	mysql_select_db("sql_test2", $dao);
	mysql_set_charset("gbk");

	$uid = $_GET['id'];
	$uid = addslashes($uid);
	if(preg_match("/^union|\s|sleep|and$/i",$uid)){
		die("waf");
	}
	$sql = "SELECT * FROM info WHERE id='$uid'";
	//echo $sql;
	$result=mysql_query($sql);
	if($ans = mysql_fetch_array($result)){
		echo "sucess";
	}
	else{
		echo "wrong";
	}
?>
