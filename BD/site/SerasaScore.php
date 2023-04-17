<?php 

    $score = $_GET['score'];
    
    if($score>500){
        echo '<html>
    <head>
        <title>Validacao cartao de credito</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha284-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
        <style type="text/css">
            .form{
                padding-top: 30px;
                padding-right: 250px;
                padding-left: 250px;
                padding-bottom: 30px;
                background-color: rgba(255, 255, 255, 0.190);
                margin-left: 100px;
                margin-right: 100px;
                margin-bottom: 10px;
                border-radius: 10px;
                font-size: 35px;
                font-family:"Courier New", Courier, monospace;
            }
            .titulo{
              font-family:"Courier New", Courier, monospace;
              margin-top: 30px;
              margin-left: 100px;
              margin-right: 100px;
              margin-bottom: 10px;
              text-align: center;
              font-size: 50px;
              background-color:rgba(255, 254, 254, 0.190);
              border-radius: 10px;
              color: rgb(0, 0, 0);
            }
            .corDoSite{
              background-image: linear-gradient(to bottom, rgb(135, 5, 5), rgb(255, 123, 0), rgb(255, 187, 0) ); 
            }
            .botao{
              padding-top:  15px;
              padding-left: 1000px;
              font-size: 20px;
            }
            .proposta{
              padding-top: 10px;
              font-size: 25px;
            }
            .form-control{
                font-size: 18px;
            }
            .menor{
                font-size: 18px;
            }
        </style>
    </head>
    <body class="corDoSite">
          
          <div class="titulo">
            <div class="proposta">
              Proposta 
              <br>
            </div>
            Cadastro do cartao de credito<img src="master.png" height="100">
            <br>
          </div>
          <div class="form">
            <form action="Banco.php" method="get">
                <div class="form-floating mb-2">
                  Complete o cadastro do mastercard 
                  <div class="menor">
                      Nome:
                    <input type="text" class="form-control" name="nome" placeholder="Nome" maxlength="30">
                      Telefone (apenas numeros):
                    <input type="number" class="form-control" name="telefone" placeholder="Telefone" maxlength="11">
                      Email:
                    <input type="email" class="form-control" name="email" placeholder="Email" maxlength="40">
                      CPF (apenas numeros):
                    <input type="text" class="form-control" name="cpf" placeholder="cpf" maxlength="11">
                      salario (apenas numeros):
                    <input type="number" class="form-control" name="salario" placeholder="R$" maxlength="5">
                  </div>                  
                </div>
                <div class="botao">
                  <input name="button" type="submit" value="Enviar dados"/>
                </div> 
              </form>  
          </div>
    </body>
</html>';
    }

?>