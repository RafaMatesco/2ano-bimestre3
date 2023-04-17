<?php

    include "connect.php";

    date_default_timezone_set('UTC');

    $titulo = $_POST['titulo'];
    $subititulo = $_POST['subtitulo'];
    $texto = $_POST['post'];
    $idtipoPost = $_POST['idtipoPost'];
    $momento = date('Y-m-d H:i:s');
    
    

    $query = $con->prepare("insert into post (momento, post, titulo, subtitulo, tipoPost_idtipoPost) values (?,?,?,?,?)");
    $query->bind_param("ssssi", $momento, $texto, $titulo, $subititulo, $idtipoPost);
    $query->execute();

    echo 'Postado!
            <html>
                <form action="Index.html" method="post">
                    <input type="submit" value="Voltar">
                </form>
            </html>';

?>