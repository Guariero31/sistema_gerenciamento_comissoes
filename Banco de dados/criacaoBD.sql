create database Clientes;

use Sistema;

drop table Clientes;

create table Clientes(
id int not null primary key auto_increment,
nome varchar(8) not null,
sobrenome varchar(10) not null,
email varchar(25) not null,
data_nascimento date not null
);
insert into Clientes(id, nome, sobrenome, email, data_nascimento) value (null, 'Gustavo', 'gay', 'gustavogay@gmail.com', '1998-05-08');

create table Produtos(
	id int not null primary key auto_increment,
    nome_produto varchar(20) not null,
    preco float not null,
    descricao varchar(100),
    categoria varchar(50) not null
);

create table Pedidos(
id int not null primary key auto_increment,
data_pedido date,
id_cliente int not null,
status_pedido varchar(20) not null,
foreign key(id_cliente) references Clientes(id)
);

create table ItensPedidos (
id int not null primary key auto_increment,
id_pedidos int not null,
id_produtos int not null,
foreign key(id_pedidos) references Pedidos(id),
foreign key(id_produtos) references Produtos(id),
quantidade int not null
);

create table Categoria(
id int not null primary key auto_increment,
nome_categoria varchar(20) not null
);

create table Funcionarios(
id int not null primary key auto_increment,
nome_categoria varchar(20) not null,
sobrenome varchar(20) not null,
cargo varchar(20) not null,
data_contratacao date not null,
salario float not null
);


