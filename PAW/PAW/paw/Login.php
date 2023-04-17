<?php
    include "connect.php";

    $nome = $_POST['usuario'];
    $senha = $_POST['senha'];

    $sql1 = "SELECT nome, senha FROM uniposts.usuario;";
    $resultado1 = mysqli_query($con,$sql1) or die(mysql_error()."<br>Erro ao executar a inserção dos dados");

    $login = 0;
    if (mysqli_num_rows($resultado1)!=0){
        while($elemento = mysqli_fetch_array($resultado1)){
            $nomeItem1 = $elemento['nome'];
            $nomeItem2 = $elemento['senha'];
            if($nome == $nomeItem1 and $senha == $nomeItem2){
                $login = 1; 
                echo '  <html>
                            <head>
                                <title>Pagina inicial</title>
                            </head>
                            <body>
                                Voce esta logado. <br><br>
                                <a href="Post.html">Crie um post </a><br>
                                <a href="search.html">Pesquisar usuario </a><br>
                                <a href="postCrono.php">Posts mais recentes </a><br>
                                <a href="Index.html">Cadastrar turma</a><br>

                            </body>
                        </html>';
            }
        }
    }else{
        echo '<a href="CadastroUsuario.php">Cadastrar</a>';
    }

    if($login == 0){
        echo 'usuario ou senha incorretos.';
    }

?>