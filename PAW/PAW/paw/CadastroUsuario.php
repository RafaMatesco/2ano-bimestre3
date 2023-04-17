<?php
    include "connect.php";

    $sql1 = "SELECT idturma, turma, ano FROM uniposts.turma order by turma, -ano;";
    $resultado1 = mysqli_query($con,$sql1) or die(mysql_error()."<br>Erro ao executar a inserção dos dados");
    $sql2 = "SELECT idturma FROM uniposts.turma;";
    $resultado2 = mysqli_query($con,$sql2) or die(mysql_error()."<br>Erro ao executar a inserção dos dados");
    if (mysqli_num_rows($resultado2)!=0){
        echo '<form action="InsertCadastroUsuario.php" method="post" enctype="multipart/form-data">';
        echo '  <input type="text" placeholder="nome" name ="Nome"><br>
                <input type="text" placeholder="e-mail" name ="Email"><br>
                <input type="password" placeholder="senha" name ="Senha"><br>
                <input type="date" name="DataNasc"><br>';

        if (mysqli_num_rows($resultado1)!=0){
            echo'<select name= "TurmaAno" id="TurmaAno">
                    <option value="">---Escolha uma turma e seu ano:---</option>';
            while($elemento = mysqli_fetch_array($resultado1)){
                $nomeItem3 = $elemento['idturma'];
                $nomeItem1 = $elemento['turma'];
                $nomeItem2 = $elemento['ano'];
                echo '<option value="'.$nomeItem3.'">'.$nomeItem1.', '.$nomeItem2.'º ano</option>';
            }
            echo '</select>';
        }

            echo '  <br> Foto de perfil <br> 
                    <input type="file" name="perfil"/><br><br>
                    <input type="submit" value="Cadastrar">';
            echo '</form>';
            echo '<a href="LoginUsuario.html">Login</a><br>';
        
    }else{
        echo'Cadastre uma turma primeiro
        <html>
        <form action="Index.html" method="post">
            <input type="submit" value="Voltar">
        </form>
        </html>';






    }
?>