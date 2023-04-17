<?php
    include 'connect.php';
    
    $posts = array(); 
    $sql1 = "SELECT idpost, tipoPost_idtipoPost FROM uniposts.post order by -idpost;";
    $resultado1 = mysqli_query($con,$sql1) or die(mysql_error()."<br>Erro ao executar a inserção dos dados");
    
    if (mysqli_num_rows($resultado1)!=0){
        while($elemento = mysqli_fetch_array($resultado1)){ 
            $userid = $elemento['idpost'];
            $tipoPost_id = $elemento['tipoPost_idtipoPost'];
            $sql = "select titulo,subtitulo,post,momento, foto from post where idpost = '$userid' order by momento desc";  
            $result =  mysqli_query($con,$sql) or die(mysql_error()."<br>Erro ao executar a inserção dos dados");
            while($data = mysqli_fetch_object($result)){
                if($tipoPost_id == 2){
                    $posts[] = array('titulo' => $data->titulo, 
                                 'subtitulo' =>$data->subtitulo,
                                 'post' => $data->post,
                                 'foto' => $data->foto);    
                }else{
                    $posts[] = array('titulo' => $data->titulo, 
                                 'subtitulo' =>$data->subtitulo,
                                 'post' => $data->post); 
                }   
             } 
        }
        if (count($posts)){
            ?>
            <table border='1' cellspacing='0' width='500'>
            <?php
            foreach ($posts as $key => $list){
                if(isset($list["foto"])){
                    echo "<tr valign='top'>\n";
                    echo "<td>".$list['titulo'] ."</td>\n";
                    echo "<td>".$list['subtitulo'] ."<br/>\n";
                    echo "<small>".$list['post'] ."</small><br>\n";
                    echo "<small><img src='imagens/".$list["foto"]."' width='200'></small></td>\n";
                    echo "</tr>\n";
                }else{
                    echo "<tr valign='top'>\n";
                    echo "<td>".$list['titulo'] ."</td>\n";
                    echo "<td>".$list['subtitulo'] ."<br/>\n";
                    echo "<small>".$list['post'] ."</small></td>\n";
                    echo "</tr>\n";
                }
            }
            ?>
            </table>
            <?php
            }else{
            ?>
            <p><b>Você não postou nada ainda</b></p>
            <?php
            }
    }
    echo '
    <html>
    <br>
        <form action="Index.html" method="post">
            <input type="submit" value="Voltar">
        </form>
    </html>';
        ?>



