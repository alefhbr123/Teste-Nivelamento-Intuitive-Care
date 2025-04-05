CREATE TABLE demonstracoes_contabeis (
    id SERIAL PRIMARY KEY,
    data_informacao DATE,
    reg VARCHAR(50),
    conta VARCHAR(50),
    descricao TEXT,
    vl_saldo_inicial NUMERIC(15,2),
    vl_saldo_final NUMERIC(15,2)
);

CREATE TABLE demonstracoes_staging (
    data_informacao TEXT,
    reg TEXT,
    conta TEXT,
    descricao TEXT,
    vl_saldo_inicial TEXT,
    vl_saldo_final TEXT
);

\copy demonstracoes_contabeis(data_informacao, reg, conta, descricao, vl_saldo_inicial, vl_saldo_final) FROM 'C:/Users/User/Documents/TesteDeNivelamento/1T2023_mod.csv' WITH (FORMAT csv, HEADER true, DELIMITER ';', ENCODING 'UTF8');
\copy demonstracoes_contabeis(data_informacao, reg, conta, descricao, vl_saldo_inicial, vl_saldo_final) FROM 'C:/Users/User/Documents/TesteDeNivelamento/1T2024_mod.csv' WITH (FORMAT csv, HEADER true, DELIMITER ';', ENCODING 'UTF8');\copy demonstracoes_contabeis(data_informacao, reg, conta, descricao, vl_saldo_inicial, vl_saldo_final) FROM 'C:/Users/User/Documents/TesteDeNivelamento/4T2023_mod.csv' WITH (FORMAT csv, HEADER true, DELIMITER ';', ENCODING 'UTF8');
\copy demonstracoes_contabeis(data_informacao, reg, conta, descricao, vl_saldo_inicial, vl_saldo_final) FROM 'C:/Users/User/Documents/TesteDeNivelamento/2T2024_mod.csv' WITH (FORMAT csv, HEADER true, DELIMITER ';', ENCODING 'UTF8');
\copy demonstracoes_contabeis(data_informacao, reg, conta, descricao, vl_saldo_inicial, vl_saldo_final) FROM 'C:/Users/User/Documents/TesteDeNivelamento/2T2023_mod.csv' WITH (FORMAT csv, HEADER true, DELIMITER ';', ENCODING 'UTF8');
\copy demonstracoes_contabeis(data_informacao, reg, conta, descricao, vl_saldo_inicial, vl_saldo_final) FROM 'C:/Users/User/Documents/TesteDeNivelamento/3T2024_mod.csv' WITH (FORMAT csv, HEADER true, DELIMITER ';', ENCODING 'UTF8');
\copy demonstracoes_contabeis(data_informacao, reg, conta, descricao, vl_saldo_inicial, vl_saldo_final) FROM 'C:/Users/User/Documents/TesteDeNivelamento/3T2023_mod.csv' WITH (FORMAT csv, HEADER true, DELIMITER ';', ENCODING 'UTF8');
\copy demonstracoes_contabeis(data_informacao, reg, conta, descricao, vl_saldo_inicial, vl_saldo_final) FROM 'C:/Users/User/Documents/TesteDeNivelamento/4T2024_mod.csv' WITH (FORMAT csv, HEADER true, DELIMITER ';', ENCODING 'UTF8');
\copy demonstracoes_contabeis(data_informacao, reg, conta, descricao, vl_saldo_inicial, vl_saldo_final) FROM 'C:/Users/User/Documents/TesteDeNivelamento/4T2023_mod.csv' WITH (FORMAT csv, HEADER true, DELIMITER ';', ENCODING 'UTF8');


SELECT COUNT(*) FROM demonstracoes_contabeis;

SELECT reg AS operadora,
       SUM(vl_saldo_final) AS total_despesa
FROM demonstracoes_contabeis
WHERE descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO-HOSPITALAR'
  AND data_informacao BETWEEN '2023-10-01' AND '2023-12-31'
GROUP BY reg
ORDER BY total_despesa DESC
LIMIT 10;



SELECT reg AS operadora,
       SUM(vl_saldo_final) AS total_despesa
FROM demonstracoes_contabeis
WHERE descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO-HOSPITALAR'
  AND data_informacao BETWEEN '2023-01-01' AND '2023-12-31'
GROUP BY reg
ORDER BY total_despesa DESC
LIMIT 10;
