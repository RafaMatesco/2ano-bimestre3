<?php
    include("lib/vendor/autoload.php");

    $nome = $_GET['nome'];
    $telefone = $_GET['telefone'];
    $email = $_GET['email'];
    $cpf = $_GET['cpf'];
    $salario = $_GET['salario'];
    $cardNumber = ' '.rand(1001,9989);
    $cardNumber .= ' '.rand(1001,9989);
    $cardNumber .= ' '.rand(1001,9989);
    $cardNumber .= ' '.rand(1001,9989);
    $securityCode = rand(101,989);

    $data = 'Cartão de crédito: '.$cardNumber.'; Nome: '.$nome.'; CPF: '.$cpf.'; member since: '.date("m/Y").'; Código de segurança: '.$securityCode;


    //aqui ele vai enviar todos os dados pro banco de dados
    echo '<!DOCTYPE html>
    <html lang="en">
    
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="preconnect" href="https://fonts.gstatic.com">
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap" rel="stylesheet">
        <title>Cartao aprovado</title>
        <style type="text/css">
            :root {
            --white: #ffffff;
            --gray: #999999;
            --purple: #442c61;
            --yellow: #f79e1b;
            --red: #eb001b;
            --light-blue: #0061ff;
            --dark-blue: #08189e;
        }
    
        *,
        *::before,
        *::after {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: Poppins, sans-serif;
        }
        
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
          margin-left: 50px;
          margin-right: 100px;
          margin-bottom: 10px;
          text-align: center;
          font-size: 50px;
          background-color:rgba(0, 0, 0, 0.397);
          border-radius: 10px;
          color: rgb(255, 255, 255);
          align-items: center;
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

        .flex { display: flex }
        .absolute { position: absolute }
    
        .credit-card {
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            background-image: linear-gradient(to bottom, rgb(135, 5, 5), rgb(255, 123, 0), rgb(255, 187, 0) );
        }
    
        .credit-card::before {
            content: "";
            position: absolute;
            width: 600px;
            height: 400px;
            transform: scaleX(-1);
        }
    
        .card {
            position: relative;
            width: 500px;
            height: 300px;
            transform-style: preserve-3d;
            perspective: 500px;
        }
    
        .card .face {
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            border: 1px solid rgb(255 255 255 / 20%);
            border-radius: 10px;
            background: linear-gradient(135deg, rgb(255 255 255 / 10%) 0%, transparent 100%);
            backdrop-filter: blur(10px);
            box-shadow: 2px 2px 0px 0px rgb(255 255 255 / 20%);
            transform-style: preserve-3d;
            transition: 0.75s ease-in-out;
            backface-visibility: hidden;
            transform: rotateY(0);
        }
    
        /* CARD FRONT FACE START */
    
        #chip {
            width: 60px;
            height: 60px;
            top: 100px;
            left: 50px;
        }
    
        #signal {
            width: 25px;
            height: 25px;
            top: 115px;
            left: 115px;
            transform: rotate(90deg);
        }
    
        #logo {
            width: 85px;
            height: 85px;
            bottom: 30px;
            left: 40px;
        }
    
        #owner {
            bottom: 55px;
            left: 140px;
            font-size: 1.35rem;
            letter-spacing: 1px;
            color: var(--white);
        }
    
        /* CARD FRONT FACE END */
    
        /* CARD BACK FACE START */
        .card .face.back {
            transform: rotateY(180deg);
        }
    
        #graybar {
            width: 100%;
            height: 50px;
            top: 15px;
            background: var(--gray);
        }
    
        #card-info {
            width: 100%;
            bottom: 15px;
            padding: 0 20px;
            color: var(--white);
        }
    
        #card-number {
            letter-spacing: 2px;
            font-size: 1.3rem;
        }
    
        #card-info .informations:not(:first-child) {
            margin-left: 10px;
        }
    
        #card-info .flex .informations {
            align-items: center;
        }
    
        #card-info .flex .informations .label {
            display: block;
            font-size: 0.4rem;
            margin-right: 4px;
            width: 30px;
        }
    
        /* FLAGS START */
        .card .face.front::before,
        .card .face.front::after,
        .card .face.back::before,
        .card .face.back::after {
            content: "";
            position: absolute;
            width: 45px;
            height: 45px;
            border-radius: 50%;
            opacity: 0.75;
        }
    
        .card .face.front::before,
        .card .face.front::after {
            top: 10px;
            mix-blend-mode: overlay;
        }
    
        .card .face.back::before,
        .card .face.back::after {
            bottom: 30px;
            mix-blend-mode: hue;
        }
    
        .card .face.front::before,
        .card .face.back::before {
            right: 20px;
        }
    
        .card .face.front::after,
        .card .face.back::after {
            right: 45px;
        }
    
        .card .face.front::before {
            background: var(--yellow);
        }
    
        .card .face.front::after {
            background: var(--red);
        }
    
        .card .face.back::before {
            background: var(--light-blue);
        }
    
        .card .face.back::after {
            background: var(--dark-blue);
        }
    
        /* FLAGS END */
    
        /* ANIMATION */
        .card:hover .face.front {
            transform: rotateY(180deg);
        }
    
        .card:hover .face.back {
            transform: rotateY(360deg);
        }
    
        </style>
    </head>
    
    <body>
    
        <section class="credit-card">
			<div class="titulo">
        			Cartao aprovado! <img src = ', (new \chillerlan\QRCode\QRCode())->render($data) ,' height=100px/>
        			<br>
    			</div>
            <div class="card">
				
                <div class="face front absolute">
                    <img src="./assets/chip.svg" alt="Chip" id="chip" class="absolute"></img>
                    <img src="./assets/signal.svg" alt="Signal" id="signal" class="absolute"></img>
                    <img src="master.png" alt="Logo" id="logo" class="absolute"></img>
                    <p id="owner" class="absolute">', $nome ,'</p>
                </div>
                <div class="face back absolute">
                    <div id="graybar" class="absolute"></div>
                    <div id="card-info" class="absolute">
                        <p id="card-number">', $cardNumber ,'</p>
                        <div class="flex">
                            <p class="flex informations">
                                <span class="label">MEMBER SINCE</span>
                                <span>', date("m/Y") ,'</span>
                            </p>
                            <p class="flex informations">
                                <span class="label">VALID THRU</span>
                                <span>12/29</span>
                            </p>
                            <p class="flex informations">
                                <span class="label">SECURITY CODE</span>
                                <span>', $securityCode ,'</span>
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </body>
    
    </html>
    ';

?>