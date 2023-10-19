use sistemavenda;

create table cliente(
id int not null primary key auto_increment,
nome varchar(45),
endereco varchar(45)
);

drop table loja;
create table loja(
id int not null primary key auto_increment,
nome varchar(45) not null,
CNPJ varchar(45) not null unique
);

drop table loja;
create table venda(
n_nfe int not null primary key auto_increment,
data_venda date DEFAULT NOW(),
valor_total decimal(10,2),
loja_id int not null,
cliente_id int not null
);

create table ProdutoVenda(

);

create table produto(
id int not null primary key auto_increment,
nome varchar(45) not null,
descricao varchar(255)
);

create table fornecedor(
id int not null primary key auto_increment,
nome varchar(45),
cnpj varchar(20) unique,
endereco varchar(60)
);