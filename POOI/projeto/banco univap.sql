create database univap;
use univap;

create table professores(registro int not null primary key,
nomeprof varchar(50),
telefoneprof varchar(30),
idadeprof int,
salarioprof float);

create TABLE disciplinasxprofessores(codigodisciplinanocurso varchar(10) not null primary key,
coddisciplina int,
codprofessor int,
curso int,
cargahoraria int,
anoletivo int);

create table disciplinas(codigodisc int not null primary key,
nomedisc varchar(50));

ALTER TABLE disciplinasxprofessores ADD CONSTRAINT fk_disciplinas FOREIGN KEY (coddisciplina) REFERENCES disciplinas (codigodisc) ;
ALTER TABLE disciplinasxprofessores ADD CONSTRAINT fk_professores FOREIGN KEY (codprofessor) REFERENCES professores (registro) ;

