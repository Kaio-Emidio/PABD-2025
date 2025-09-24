show databases;
use brasil;

select nome 
from cidade 
where uf='20';

select uf, ddd 
from estado 
where uf='SP';

/*começa com b*/
select nome 
from pais 
where nome like 'B%';

/*termina com b*/
select nome 
from pais 
where nome like '%B'; 

/*% -> 0 ou mais caracteres
_ -> determinada quantidade de caracteres*/

select nome 
from cidade 
where nome 
like '%santa%';

/*ordem alfabetica*/
select nome 
from cidade 
where nome like '%santa%' 
order by nome ASC;
/*asc para ascendente
desc para decendente*/

/*mostrar apenas as tantas primeiras cidades*/
select nome 
from cidade 
where nome like '%santa%' 
order by nome asc 
limit 3;

/*count mostra apenas a quantidade e não os dados
as é usado caso queira apelidar a coluna*/
select count(*) 
as NumPais 
from pais;

select nome 
as CidadesComSanta 
from cidade 
where nome like '%santa%' 
order by nome ASC;

/*Mostrar os resultados ao relacionar duas tabelas é usado where com os complementos sendo pk=fk
Nesse modelo, caso as colunas possuam nomes iguais, é utilizado tabela.nome*/
select cidade.nome, estado.uf 
from cidade, estado 
where estado.id = cidade.uf 
and estado.uf='RN';