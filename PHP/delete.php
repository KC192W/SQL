<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>


        <?php
        $ID=$_GET['ID']; //帶入參數
       
        $link = require_once('../db_setting.php');
        $sql="delete from account where ID='$ID'";

    if(mysqli_query($link, $sql)){
        header("Location:message.php?message=刪除成功");

    }else{
        
        header("Location:message.php?message=刪除失敗");
        
    }

        mysqli_close($link);

        ?>
    </table>
</body>
</html>