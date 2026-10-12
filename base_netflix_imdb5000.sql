CREATE DATABASE netflix_analise;

USE netflix_analise;

CREATE TABLE netflix_titles01 (
    id VARCHAR(20),
    tipo VARCHAR(20),
    titulo VARCHAR(255),
    diretor TEXT,
    elenco TEXT,
    pais TEXT,
    data_adicao VARCHAR(50),
    ano_lancamento INT,
    classificacao_etaria VARCHAR(20),
    duracao VARCHAR(50),
    generos TEXT,
    descricao TEXT,
    chave_relacionamento VARCHAR(300)
);

CREATE TABLE titles_netflix02 (
    id VARCHAR(20),
    titulo VARCHAR(255),
    tipo VARCHAR(20),
    descricao TEXT,
    ano_lancamento INT,
    classificacao_etaria VARCHAR(20),
    duracao INT,
    generos TEXT,
    pais TEXT,
    temporadas FLOAT,
    id_imdb VARCHAR(30),
    nota_imdb DECIMAL(4,2),
    votos_imdb BIGINT,
    popularidade_tmdb DECIMAL(12,2),
    nota_tmdb DECIMAL(4,2),
    chave_relacionamento VARCHAR(300)
);

CREATE TABLE tmdb_movies (
    id_tmdb INT,
    titulo VARCHAR(255),
    ano_lancamento INT,
    generos LONGTEXT,
    popularidade_tmdb DECIMAL(12,2),
    nota_tmdb DECIMAL(4,2),
    votos_tmdb BIGINT,
    duracao INT,
    orcamento BIGINT,
    receita BIGINT,
    idioma_original VARCHAR(10),
    data_lancamento DATE,
    chave_relacionamento VARCHAR(300)
);

SELECT
    n.titulo,
    n.ano_lancamento,
    n.tipo,
    t.nota_imdb,
    t.nota_tmdb,
    m.popularidade_tmdb
FROM netflix_titles01 n

LEFT JOIN titles_netflix02 t
ON n.chave_relacionamento = t.chave_relacionamento

LEFT JOIN tmdb_movies m
ON n.chave_relacionamento = m.chave_relacionamento;

CREATE VIEW vw_catalogo_completo AS

SELECT
    n.titulo,
    n.tipo,
    n.pais,
    n.generos,
    n.ano_lancamento,
    t.nota_imdb,
    t.votos_imdb,
    t.nota_tmdb,
    m.popularidade_tmdb,
    m.orcamento,
    m.receita
FROM netflix_titles01 n

LEFT JOIN titles_netflix02 t
ON n.chave_relacionamento = t.chave_relacionamento

LEFT JOIN tmdb_movies m
ON n.chave_relacionamento = m.chave_relacionamento;