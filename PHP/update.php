<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>

<?php

    $ID=$_GET['ID'];
    $link = require_once('../db_setting.php');
    // $link=mysqli_connect('localhost','root','','temp','3307');//用link儲存回傳的值

    $sql="select * from account where ID='$ID'"; //儲存sql字串的變數
    $result=mysqli_query($link,$sql);

    if($row=mysqli_fetch_assoc($result)){
        //echo var_export($row);
        $ID=$row['ID'];
        $name=$row['name'];
        $password=$row['password'];
        $level=$row['level'];
    }
    mysqli_close($link);
?>
<form method="post" action="dblink.php">
    <center>
        <caption>修改帳號資料</caption>
    </center>
    <table align=center width="500" border=1 bordercolor=purple>
        <input type=hidden name='ID' value="<?php echo $ID;?>"><!--hidden讓他不能改資料-->
        <input type=hidden name='method' value="update">

        <tr>
          <td>帳號</td>
          <td><!--input type="text" name="ID" value="<?php echo $ID;?>" />-->
          <font color=brown><?php echo $ID;?></font>
        </td>
        </tr>
        <tr>
          <td>名稱</td>
          <td><input type="text" name="name" value="<?php echo $name;?>" required /></td>
        </tr>
        <tr>
          <td>密碼</td>
          <td><input type="text" name="password" value="<?php echo $password;?>" required /></td>
        </tr>
        <tr>
          <td>權限</td>
          <td><select name="level">
            <option value="admin">管理者</option>
            <option value="user">使用者</option>
          </td>
        </tr>

        
        <tr>        
            <td><input type="submit"></td>
        </tr>
        
    </table>
</form>
      
</body>
</html>