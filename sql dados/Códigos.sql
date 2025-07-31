USE concessionaria;

insert into fabrica (cnpj, cidade, estado) values
('1', 'Natal', 'RN'),
('2', 'Rio de Janeiro', 'RJ'),
('3', 'João Pessoa', 'PB'),
('4', 'Ceará-Mirim', 'RN');

insert into  telefoneFabrica (cnpjFabrica, telefone) values
('1', '12345678912'),
('1', '23456789123'),
('2', '34567891234'),
('2', '45678912345'),
('3', '56789123456'),
('3', '67891234567'),
('4', '78912345678'),
('4', '89123456789');

update fabrica
set cidade='São Paulo', estado='SP'
where cnpj='4';

delete from telefoneFabrica
where cnpjFabrica='3';