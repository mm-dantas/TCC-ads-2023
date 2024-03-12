<?php
    $user = $_POST["cxuser"];
    $senha = $_POST["cxsenha"];


if (($user == "rafael@etec.com" && $senha == "1234") || ($user == "a@etec.com" && $senha == "1111"))
{
    echo "
    <script>
    window.location.href='../model/paginaInicial.php'
    </script>";
}

else
{
    echo "
    <script>
     alert ('usuário e senha incorretos')
     window.location.href='../index.php'

    </script>
    ";
}

?>