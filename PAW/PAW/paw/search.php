<?php
    include 'connect.php';

    if (isset($_POST['cxnome'])){
        $nome=$_POST['cxnome'];
        $pesquisa=$_POST['pesquisar'];
    }

    if(isset($pesquisa)&&!empty($nome))
    {
        $sql1 = 'SELECT nome FROM usuario WHERE nome LIKE "%'.$nome.'%"';
        $resultado1 = mysqli_query($con,$sql1) or die(mysql_error()."<br>Erro ao executar a inserção dos dados");

        if(mysqli_num_rows($resultado1)!=0){
            echo "Resultado(s) encontrado(s): ".mysqli_num_rows($resultado1)."<br /><br />";
            while($reg = mysqli_fetch_array($resultado1))
            {
                echo $reg['nome']."<br>";
            }
            echo '
            <html>
                <br>
                <form action="search.html" method="post">
                    <input type="submit" value="Voltar">
                </form>
            </html>';
        }
        else
        {
            echo 'Não existe usuario cadastrado
            <html>
                <br>
                <form action="search.html" method="post">
                    <input type="submit" value="Voltar">
                </form>
            </html>';
        }
    }
    else{
        echo 'Preencha o campo de pesquisa
        <html>
        <br>
            <form action="search.html" method="post">
                <input type="submit" value="Voltar">
            </form>
        </html>';
    }
?>