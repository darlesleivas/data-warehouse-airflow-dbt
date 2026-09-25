with source as (
    select * from {{ source('postgres_source', 'minha_tabela') }}
)

select
    *
from source