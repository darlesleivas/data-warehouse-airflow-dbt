with staging as (
    select * from {{ ref('stg_minha_tabela') }}
),

transformed as (
    select
        id,
        nome,
        -- Exemplo de regra de negócio: adicionando uma coluna calculada ou tratamento
        current_timestamp as carregado_em
    from staging
)

select * from transformed