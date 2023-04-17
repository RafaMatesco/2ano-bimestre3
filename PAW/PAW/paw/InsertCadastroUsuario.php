<?php
    include "connect.php";
    
    $sql1 = "SELECT nome FROM uniposts.usuario;";
    $resultado1 = mysqli_query($con,$sql1) or die(mysql_error()."<br>Erro ao executar a inserção dos dados");

    $perfil = $_FILES['perfil']['name'];
    $Nome = $_POST['Nome'];
    $Email = $_POST['Email'];
    $Senha = $_POST['Senha'];
    $DataNasc = $_POST['DataNasc'];
    $TurmaAno = $_POST['TurmaAno'];
    $x = 0;

    if (mysqli_num_rows($resultado1)!=0){
        while($elemento = mysqli_fetch_array($resultado1)){
            $nomeItem1 = $elemento['nome'];
            if($Nome== $nomeItem1 ){
                $x = 1;
                echo 'Nome de cadastrado existente
        
                <html>
                    <form action="CadastroUsuario.php" method="post">
                        <input type="submit" value="Voltar">
                    </form>
                </html>';
            }
        }
    }
        if ($x == 0){
            if(isset($_FILES['perfil']))
            { 
            $dir = 'imagens/perfil/ ';
            $dir = rtrim($dir, ' '); //Diretório para uploads 
            $nome1 = $_FILES['perfil']['name']; //Definindo um novo nome para o arquivo
            move_uploaded_file($_FILES['perfil']['tmp_name'], $dir.$nome1); //Fazer upload do arquivo
            } 
            $query = $con->prepare("insert into usuario (nome, email, senha, foto, dataNascimento, turma_idturma) values (?,?,?,?,?,?)");
            $query->bind_param("sssssi", $Nome, $Email, $Senha, $perfil, $DataNasc, $TurmaAno);
            $query->execute();
            echo 'Cadastrado com sucesso 
                
                    <html>  
                        <form action="Index.html" method="post">
                            <input type="submit" value="Voltar">
                        </form>
                    </html>';
        }
?>