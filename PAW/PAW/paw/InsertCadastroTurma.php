<?php

    include "connect.php";
    
    $NomeTurma = $_POST['NomeTurma'];
    $Ano = $_POST['Ano'];
    
    $NomeTurma = strtoupper($NomeTurma);

    $sql1 = "SELECT turma, ano FROM uniposts.turma order by ano, turma;";
    $resultado1 = mysqli_query($con,$sql1) or die(mysql_error()."<br>Erro ao executar a inserção dos dados");

    $Sair = 0;
    if (mysqli_num_rows($resultado1)!=0){
        while($elemento = mysqli_fetch_array($resultado1)){
            $nomeItem1 = $elemento['turma'];
            $nomeItem2 = $elemento['ano'];
            if($nomeItem1 == $NomeTurma and $nomeItem2 == $Ano){
                $Sair = 1;
                echo 'Esta turma ja existe no '.$Ano.'º ano.
                <form action="Index.html" method="post">
                    <input type="submit" value="Voltar">
                </form>';
            }
        }
    }

    if($Sair == 0){
        if($Ano>0 and $Ano<4){
            $query = $con->prepare("insert into turma (turma, ano) values (?,?)");
            $query->bind_param("si", $NomeTurma, $Ano);
            $query->execute();
            echo 'Cadastrado com sucesso!
            <html>
                <form action="LoginUsuario.html" method="post">
                    <input type="submit" value="Voltar">
                </form>
            </html>';
        }else{
            echo 'Digite um ano válido
            <html>
                <form action="Index.html" method="post">
                    <input type="submit" value="Voltar">
                </form>
            </html>';
        }
    }
  
?>