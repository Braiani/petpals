CREATE DATABASE IF NOT EXISTS petpals;
USE petpals;

CREATE TABLE users (
    id_user int auto_increment primary key,
    name varchar(200) not null,
    email varchar(200) not null,
    password varchar(200) not null,
    use_terms tinyint default 0,
    policies tinyint default 0
);

CREATE TABLE categories (
    id_category int auto_increment primary key,
    title varchar(200) not null,
    image varchar(255) not null
);

CREATE TABLE products (
    id_product int auto_increment primary key,
    title varchar(200) not null,
    image varchar(255) not null,
    price float default 0,
    id_category int,
    foreign key fk_category(id_category) references categories(id_category)
);

CREATE TABLE statuses (
    id_status int auto_increment primary key,
    description varchar(200) not null
);

CREATE TABLE carts (
    id_cart int auto_increment primary key,
    id_user int,
    id_status int,
    foreign key fk_user(id_user) references users(id_user),
    foreign key fk_status(id_status) references statuses(id_status)
);

CREATE TABLE cart_product (
    id_cart_product int auto_increment primary key,
    discount float,
    id_product int,
    id_cart int,
    foreign key fk_product(id_product) references products(id_product),
    foreign key fk_cart(id_cart) references carts(id_cart)
);

INSERT INTO statuses (id_status, description) VALUES
(1, 'Pendente'),
(2, 'Cancelado'),
(3, 'Em espera'),
(4, 'Finalizado');

INSERT INTO categories (id_category, title, image) VALUES
(1, 'Acessórios', 'http'),
(2, 'Alimentação', 'http'),
(3, 'Brinquedos', 'http'),
(4, 'Higiene', 'http');

INSERT INTO products (title, image, price, id_category) VALUES
('Cotonete', '', 19.99, 4),
('Pomada Neodexa', '', 59.99, 4),
('Shamposhi', '', 99.99, 4),
('Pet carrier', '', 29.99, 4),
('Pasta dental', '', 29.99, 4);