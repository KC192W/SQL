<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
        <?php
        $method=$_POST['method'];
        $ID=$_POST['ID'];
        $password=$_POST['password'];
        $name=$_POST['name'];
        $level=$_POST['level'];

        $link = require_once('../db_setting.php');

        
    if($method=="update"){ 
        $sql="update account set name='$name', level='$level',password='$password' where ID='$ID'";
        if(mysqli_query($link,$sql)){
        echo "修改成功";
    
    }else{
        echo"修改失敗", $sql;
        
    }
}
   

        ?>
    
</body>
</html>