create database bdCIC;

use bdCIC;


 create table tbIA(	
 rede_neural int primary key auto_increment,
 descricao_ia varchar(40),
 nome_ia varchar(30)
 
 );
 
 
create table tbAtendimento(	
 num_atendi int primary key auto_increment,
 tipo_ate  varchar(30),
data_ate date,
rede_neural int, foreign key(rede_neural) references tbIA(rede_neural),
status ENUM('ativo', 'inativo') NOT NULL DEFAULT 'ativo'
 );

create table tbServico(	
 cod_servico int primary key auto_increment,
 nome_servico  varchar(30),
 tipo_servico varchar (30)
 
); 

create table tbFuncionario(	
 cod_fun int primary key auto_increment,
 nome_fun varchar(40),
 tel_fun int(11)
 );

create table executa_func_servico(

cod_fun int, foreign key(cod_fun) references tbfuncionario(cod_fun),
cod_servico int, foreign key(cod_servico) references tbservico(cod_servico)
);

create table tbAluno(	
 rm_aluno int(5) primary key,
 nome_aluno varchar(60),
 tel_aluno int(11));
 
 
 
create table aluno_retira_data(

rm_aluno int, foreign key(rm_aluno) references tbaluno(rm_aluno),
num_atendi int, foreign key(num_atendi) references tbatendimento(num_atendi)
);


create table fornece_aten_servico(

num_atendi int, foreign key(num_atendi) references tbatendimento(num_atendi),
cod_servico int, foreign key(cod_servico) references tbservico(cod_servico)
);

 

 
  create table tbCurso(	
 num_curso int primary key auto_increment,
 periodo_curso varchar(10), 
 ano_curso int,
 nome_curso varchar(10)
 );

create table realiza_aluno_curso(

num_curso int, foreign key(num_curso) references tbcurso(num_curso),
rm_aluno int, foreign key(rm_aluno) references tbaluno(rm_aluno)
);
 


create table atendi_solicita_servico(
cod_servico int, foreign key(cod_servico) references tbservico(cod_servico),
num_atendi int, foreign key(num_atendi) references tbatendimento(num_atendi)
);


insert into tbAluno
(rm_aluno, nome_aluno, tel_aluno)

values
	(10000, 'Nicolle Carvalho Pires de Souza', '11946670205'),
	(20000, 'Angel de Oliveira Garcia', '11946693793'),
	(30000, 'Matheus Alves Aparecido Miguel', '11970113375'),
	(40000, 'Mirella Camargos da Silva', '11941084600'),
	(50000, 'Nicolas Henrique Melo dos Santos', '11967751882'),
	(60000, 'Guilherme de Sa Mita Zampieri', '11962313000'),
	(70000, 'Guilherme Henrique Sena Gomarin', '11947456318'),
	(80000, 'Juliana Rocha', '1197887676'),
	(90000, 'Pedro Amaral Pito', '1198087808'),
    (12000, 'Matheus Dantas Carvalho', '11989687722');
    
select*from tbAluno;

insert into tbAtendimento
(tipo_ate, data_ate)

values 
	('online', '2027-03-10'),
	('online', '2029-03-10'),
	('online', '2021-03-10'),
	('online', '2022-03-10'),
    ('online', '2023-07-08'),
    ('online', '2029-03-10'),
	('online', '2021-03-10'),
	('online', '2022-03-10'),
    ('online', '2023-07-08'),
	('online', '2020-07-08');



select *from tbAtendimento;
insert into tbCurso
( periodo_curso, ano_curso, nome_curso)

values 
	('manhã', 1, 'DS'),
	('manhã', 2, 'DS'),
	('manhã', 3, 'DS'),
	('manhã', 1, 'LOG'),
	('manhã', 2, 'LOG'),
	('manhã', 3, 'LOG'),
    ('manhã', 1, 'ADM'),
	('manhã', 2, 'ADM'),
	('manhã', 3, 'ADM');

select * from tbAtendimento;

insert into tbservico
(nome_servico, tipo_servico)

values 
	('Declaração de Matrícula', 'Documento'),
	('Boletim escolar', 'Documento');

select*from tbservico;

insert into tbFuncionario
(nome_fun, tel_fun)

values 
	('Alexandro Morais', 1197825654),
	('Irineu da Silva', 119676766);


insert into realiza_aluno_curso
(num_curso, rm_aluno)

values 
	(1, 10000),
	(4, 20000),
    (3, 30000),
	(2, 40000),
    (4, 12000),
    (1, 60000),
	(4, 70000),
    (3, 80000),
	(2, 90000);
    

insert into atendi_solicita_servico
(cod_servico, num_atendi)

values 
	(2, 1),
	(1, 5),
    (1, 6),
	(2, 4),
    (2, 2),
	(1, 3),
    (2, 7),
	(1, 8),
    (1, 9),
	(2, 10);
    
select* from atendi_solicita_servico;
   
insert into aluno_retira_data
(rm_aluno, num_atendi)
values 
	(10000,2),
	(20000,1),
    (30000,3),
	(40000,4),
    (50000,6),
	(60000,5),
    (70000,7),
	(80000,8),
    (90000,9);
    
    select* from aluno_retira_data;







