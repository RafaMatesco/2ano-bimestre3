<?php

    $TipoPost = $_POST['tipo'];
    $qntFotos = $_POST['qntFotos'];

    if($TipoPost == 'texto'){
        echo '  <html>
                    <head>
                        <title>Página inicial</title>
                    </head>
                    <body>
                        Crie seu primeiro post
                        <form action="PostTexto.php" method="post">
                            <input type="text" placeholder="Titulo" name ="titulo"><br>
                            <input type="text" placeholder="Subtitulo" name ="subtitulo"><br>
                            <input type="text" placeholder="Texto" name ="post"><br>
                            <input type="radio" name="idtipoPost" value=1 CHECKED> Texto <br>
                            <input type="submit" value="Enviar">
                        </form>
                    </body>
                </html>';
    }else if($TipoPost == 'foto'){
        echo '  <html>
                    <head>
                        <title>Página inicial</title>
                    </head>
                    <body>
                        Crie seu primeiro post
                        <form action="PostFoto.php" method="post" enctype="multipart/form-data">
                            <input type="text" placeholder="Titulo" name ="titulo"><br>
                            <input type="text" placeholder="Subtitulo" name ="subtitulo"><br>
                            <input type="text" placeholder="Texto" name ="post"><br>
                            Selecione a foto: <br><input type="file" name="foto" /><br>
                            <input type="radio" name="idtipoPost" value=2 CHECKED> Foto <br>
                            <input type="submit" value="Enviar">
                        </form>
                    </body>
                </html>';
    }

?>