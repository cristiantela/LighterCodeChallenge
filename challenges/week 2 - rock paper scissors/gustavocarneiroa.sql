-- SET @a e SET @b devem ser alimentados, pois não há uma forma de fazer via CLI
-- Caracteres 258
SET @a:='';
SET @b:='';

SELECT CASE WHEN (3+a-b)%3 = 0 THEN 'Não há vencedores' ELSE CONCAT('Jogador ',(3+a-b)%3) END FROM (SELECT 
CASE WHEN @a='pedra' THEN 0 WHEN @a='papel' THEN 1 ELSE 2 END a,
CASE WHEN @b='pedra' THEN 0 WHEN @b='papel' THEN 1 ELSE 2 END b) w
