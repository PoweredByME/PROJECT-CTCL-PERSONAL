<?php 

    $data = $_POST['imgBase64'];
    $file = "sel_image.png";
    $uri = substr($data,strpos($data, ",") + 1);
    file_put_contents($file, base64_decode($uri));
    echo "hello"

?>