<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <div align=right>
        <a href="insert.php">[新增帳號]</a>
    </div>
    <form method="post" action="insert.php">
        <caption></caption>
    <table align=center width="500" border=1 bordercolor=blue>
        <tr align=center>
            <th>帳號名稱</th>
            <th>操作</th>
            <th>狀態</th>
        </tr>

        <?php
        $link=mysqli_connect('localhost','root');
        mysqli_select_db($link,'temp');
        $sql="select name from account";
        while($row=mysqli_fetch_assoc($result))
        {
            echo "<tr><td>",$row['name'],"</td><td align=center><a href=update.php>[修改]</a>&nbsp;&nbsp;<a href=delete.php>[刪除]</a></td></tr>";
        }

        mysqli_close($link);

        ?>
    </table>
    </form>
</body>
</html>