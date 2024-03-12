

<?php
// Inclua o arquivo de conexão com o banco de dados (conexao.php)
include_once 'conexao.php';

if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['num_atendi'])) {
    $numAtendimento = mysqli_real_escape_string($conn, $_POST['num_atendi']);
    
    // Execute a consulta SQL para mover o atendimento para inativo
    $query = "UPDATE tbAtendimento SET status = 'inativo' WHERE num_atendi = '$numAtendimento'";
    
    if (mysqli_query($conn, $query)) {
        // Redirecione de volta para a página inicial ou outra página relevante
        header("Location:../model/paginaInicial.php");
    } else {
        echo "Erro ao mover atendimento para inativo: " . mysqli_error($conn);
    }
}
?>
