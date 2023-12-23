<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>


        <?php
        //$id=$GET['id'];
        $ID=$_POST['ID'];
        $name=$_POST['name'];
        $level=$_POST['level'];
        $password=$_POST['password'];
        //$company=$_POST['company'];

        
        $link = require_once('../db_setting.php');
    
        //echo var_dump($link);
        $sql="insert into account (ID, name, level,password) value('$ID','$name','$level','$password')";
        //$sql1 = "SELECT * FROM `projects` WHERE projects.project_id = '123'"

        // $mysqli_select_db($link,'temp');
        
    if(mysqli_query($link, $sql)){
        echo "新增成功";

    }else{
        
        echo"新增失敗";
        echo $ID,$name,$level,$password;
        
    }

        mysqli_close($link);

        ?>
    </table>
</body>
</html>