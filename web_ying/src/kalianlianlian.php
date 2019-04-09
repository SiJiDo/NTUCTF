<?php
include "flag.php";
if(isset($_GET['ka']) && isset($_GET['lian']) && isset($_GET['233'])){
    $ying1 = $_GET['ka'];
    $ying2 = $_GET['lian'];
    $ying3 = $_GET['233'];
    if($ying1 != $ying2 && md5($ying1) == md5($ying2)){
        if(!strcmp($ying3, $flag)){
            echo "$flag";
        }
    }
}
highlight_file(__FILE__);
?>