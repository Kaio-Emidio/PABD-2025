/*1. Liste nome e cidade de todos os alunos, ordenando por nome*/
select nome, cidade 
from alunos 
order by nome ASC;

/*2. Mostre aluno_id, nome e email dos alunos cujo nome começa com “A”.*/
select aluno_id, nome, email 
from alunos 
where nome like 'A%';

/*3. Traga nome, cidade, nota_media dos alunos com nota_media > 8.0.*/
select nome, cidade, nota_media 
from alunos 
where nota_media > 8;

/*4. Liste nome, nota_media dos alunos com nota_media < 7.0.*/
select nome, nota_media 
from alunos 
where nota_media < 7;

/*5. Conte quantos alunos são da cidade de Natal.*/
select count(*) 
from alunos 
where cidade = 'Natal';

/*6. Liste nome do aluno, nome do curso e status de todas as matrículas.*/
select alunos.nome as 'Nome do aluno', cursos.nome as 'Nome do curso', matriculas.status 
from alunos, cursos, matriculas 
where alunos.aluno_id = matriculas.aluno_id and 
	matriculas.curso_id = cursos.curso_id 
order by alunos.nome;

/*7. Mostre aluno, curso, data_matricula das matrículas Ativas em cursos com preco > 700.*/
select alunos.nome as 'Nome do aluno', cursos.nome as 'Nome do curso', matriculas.data_matricula 
from alunos, cursos, matriculas 
where alunos.aluno_id = matriculas.aluno_id and 
	matriculas.curso_id = cursos.curso_id and
	matriculas.status = 'Ativa' and 
	cursos.preco > 700;

/*8. Liste aluno, curso, status das matrículas em cursos cuja area contenha “Tecnologia”.*/
select alunos.nome as 'Nome do aluno', cursos.nome as 'Nome do curso', matriculas.status 
from alunos, cursos, matriculas 
where alunos.aluno_id = matriculas.aluno_id and 
	matriculas.curso_id = cursos.curso_id and
	cursos.area = 'Tecnologia';

/*9. Exiba, por cidade, quantos alunos existem. Mostre cidade e total_alunos, ordenando do maior para o menor.*/
select cidade, count(*) as 'Número de alunos'
from alunos
group by cidade
order by NumeroAlunos DESC;

/*10. Mostre, para cada curso, a quantidade de matrículas e quantas estão Concluídas. Exiba curso, total_matriculas, matriculas_concluidas.*/
