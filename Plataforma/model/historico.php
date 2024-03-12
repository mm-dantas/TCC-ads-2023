<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Histórico</title>
    <link rel="stylesheet" type="text/css" href="../css/stylehisto.css">
    <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>


</head>
<body>
<div class="sidebar">
        <div class="logo_details"> 
            <i class="bx bxl-audible icon"> </i>
                <div class="logo_name">CIC</div>
                <i class="bx bx-menu" id="btn"></i>
           
        </div>
        <ul class="nav-list">
            <li>
                <i class="bx bx-search"></i>
                <input type="text" placeholder="pesquisar...">
                <span class="tooltip">Pesquisar</span>
            </li>
            <li>
                <a href="paginaInicial.php">
                  <i class="bx bx-calendar-edit"></i> 
                  <span class="link_name">Inicial</span>
                </a>
                <span class="tooltip">Inicial</span>

            </li>
            <li>
                <a href="historico.php">
                    <i class="bx bx-calendar"></i> 
                    <span class="link_name">Histórico</span>
                  </a>
                  <span class="tooltip">Histórico</span>

            </li>
           
            <li>
                <div class="text1">Outros</div>

                <a href="../view/perfil.php">
                    <i class="bx bx-user"></i> 
                    <span class="link_name">Perfil</span>
                  </a>
                  <span class="tooltip">perfil</span>

            </li>
           
            <section class="profile">

                <div class="profile_details">
                <img src="../img/profili.png" alt="profile image">
                    <div class="profile_content">
                        <div class="name">Nicolle Carvalho</div>

                        <a href="../view/perfil.php"><p class="ir">Ir para o perfil</p> </a>

                    </div>
                    <a href="../index.php"><i class="bx bx-log-out" id="log_out" placeholder="Sair"></i></a>
                </div>
                
               
</section>
            
            <script src="../js/script.js"></script>

        </ul>
    </div>
  
    <script src="../js/script.js"></script>

    
   
</div>

<script type="text/javascript" src="../js/main.js"></script>
<div class="container">
    <nav>
    <div class="dashboard-cont">
    <h2>Tarefas realizadas</h2>
    <table id="tabelaDados">
        
            
        <thead>
    <tr>
        <th>Número Atendimento</th>
        <th>RM Aluno</th>
        <th>Nome Aluno</th>
        <th>Serviço Solicitado</th>
        <th>Data de Entrega</th>
    </tr>
</thead>
<tbody>
    <?php
    include_once '../control/conexao.php';

    $consulta = '
    SELECT tbatendimento.num_atendi, tbaluno.rm_aluno, tbaluno.nome_aluno, tbservico.nome_servico, tbatendimento.data_ate
    FROM tbatendimento
    JOIN atendi_solicita_servico ON tbatendimento.num_atendi = atendi_solicita_servico.num_atendi
    JOIN tbservico ON atendi_solicita_servico.cod_servico = tbservico.cod_servico
    JOIN aluno_retira_data ON tbatendimento.num_atendi = aluno_retira_data.num_atendi
    JOIN tbaluno ON aluno_retira_data.rm_aluno = tbaluno.rm_aluno
    WHERE tbatendimento.status = "inativo";';
    
    $executar = mysqli_query($conn, $consulta);

    while ($exibir = mysqli_fetch_array($executar)) {
        echo "<tr>";
        echo "<td>".$exibir['num_atendi']."</td>";
        echo "<td>".$exibir['rm_aluno']."</td>";
        echo "<td>".$exibir['nome_aluno']."</td>";
        echo "<td>".$exibir['nome_servico']."</td>";
        // Formatando a data no formato "dia/mês/ano"
        $dataFormatada = date('d/m/Y', strtotime($exibir['data_ate']));
        echo "<td>".$dataFormatada."</td>";
        echo "</tr>";
    }
    ?>
</tbody>

    </table>
    </div>

</nav>  
</div>

    
</body>
</html>
