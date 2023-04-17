<?php

    $data = $_GET['data'];

    $ano = explode('-', $data);
    $ano = $ano[0];
    $ano = (int) $ano;
    if(2022-$ano>15){
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
                        font-size: 25px;
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
                    <form action="SerasaScore.php" method="get">
                        <div class="form-floating mb-2">
                        Digite seu Serasa Score 
                        <input type="number" class="form-control" name="score" placeholder="Serasa Score" maxlength="4" min="0" max="1000">
                        </div>
                        <div class="botao">
                        <input name="button" type="submit" value="Enviar dados"/>
                        </div> 
                    </form>  
                </div>
            </body>
        </html>';
    }else{
        echo '';
    }
    
    
?>