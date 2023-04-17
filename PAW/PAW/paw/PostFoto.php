<?php

    include "connect.php";

    date_default_timezone_set('UTC');

    $titulo = $_POST['titulo'];
    $subititulo = $_POST['subtitulo'];
    $texto = $_POST['post'];
    $idtipoPost = $_POST['idtipoPost'];
    $momento = date('Y-m-d H:i:s');
    $foto = $_POST['foto'];

    if(isset($_FILES['foto']))
 { 
    $dir = 'imagens\ ';
    $dir = rtrim($dir, ' '); //Diretório para uploads 
    $nome1 = $_FILES['foto']['name']; //Definindo um novo nome para o arquivo
    move_uploaded_file($_FILES['foto']['tmp_name'], $dir.$nome1); //Fazer upload do arquivo
 } 

    $query = $con->prepare("insert into post (momento, post, titulo, subtitulo, tipoPost_idtipoPost, foto) values (?,?,?,?,?,?)");
    $query->bind_param("ssssis", $momento, $texto, $titulo, $subititulo, $idtipoPost, $foto);
    $query->execute();  


    echo 'Postado!
            <html>
            <br>
                <img src="imagens/'.$nome1.'" width="200"><br><br>
                <form action="Index.html" method="post">
                    <input type="submit" value="Voltar">
                </form>
            </html>';

?>