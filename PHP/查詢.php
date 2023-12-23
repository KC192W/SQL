<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>

    <div align=right>
        <a href="insert.html">[新增帳號]</a>
    </div>

    <table align="center" width="500" border="1" bordercolor="blue">
      <tr align="center">
        <!-- <th>帳號名稱</th> -->
        <th>帳號</th>
        <th>名稱</th>
        <th>層級</th>
        <th>操作</th>
      </tr>
      <?php


       $link = require_once('../db_setting.php');
       //mysqli_select_db($link,"temp");
       $sql="select ID, name, level from account"; //查詢資料庫的name
       $result=mysqli_query($link,$sql);

       while($row=mysqli_fetch_assoc($result)){
                 echo "<tr>
                 <td>",$row['ID'],"</td>
                 <td>",$row['name'],"</td>
                 <td>",$row['level'],"</td>
                 <td align=center>
                 <a href=update.php?ID=",$row['ID'],">[修改]</a>&nbsp;&nbsp;
                 <a href=delete.php?ID=",$row['ID'],">[刪除]</a></td>
                 </tr>";
               }



    mysqli_close($link);
      ?>
    </table>
  </body>
</html>
