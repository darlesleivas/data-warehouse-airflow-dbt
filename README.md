# Pipeline Analítico End-to-End: Data Warehouse com Docker, dbt e Airflow ✈️📊

> **Desenvolvido por:** Darles Leivas  
> **Contexto:** Projeto prático desenvolvido no âmbito de formação avançada em Engenharia de Dados, aplicando uma *Modern Data Stack* para centralização, modelagem e orquestração de dados analíticos do setor de aviação comercial (~318 mil registos).

---

## 🎯 Visão Geral e Objetivo
O objetivo deste projeto foi projetar e implementar um ecossistema de dados robusto a partir do zero, garantindo reprodutibilidade, escalabilidade e separação de responsabilidades. A solução integra ingestão containerizada, transformação analítica em camadas, orquestração orientada a dependências e validação contínua via CI/CD.

---

## 🏛️ Arquitetura e Stack Tecnológica

O pipeline foi estruturado combinando ferramentas consolidadas no mercado de dados:

* **Armazenamento:** PostgreSQL 17 (executado em contentor Docker isolado).
* **Transformação & Modelagem:** `dbt` (Data Build Tool) sob a **Medallion Architecture**.
* **Orquestração:** Apache Airflow gerido via Astro CLI, utilizando a biblioteca `astronomer-cosmos` para mapear dinamicamente os modelos dbt em tarefas nativas do Airflow.
* **Automação & Qualidade:** GitHub Actions para testes e validação de compilação contínua (CI/CD).
* **Gestão de Ambiente:** Python 3.13 e `uv` para gestão célere de dependências.

### 🔄 Fluxo de Transformação (Medallion Architecture)
1. **Staging (`stg`):** Camada de ingestão que consome os dados brutos, aplicando padronização de tipos e gerando chaves cronológicas (`year_month_key`).
2. **Intermediate (`int`):** Implementação de um **Star Schema**, contendo as dimensões limpas e deduplicadas (`dim_airport`, `dim_carrier`, `dim_month`) e a tabela de factos central (`fct_flight_delays`).
3. **Mart (`mart`):** Visões analíticas agregadas prontas para consumo de BI, englobando KPIs mensais, performance de aeroportos/companhias e análise detalhada de causas de atrasos (*unpivot*).

---

## 📂 Estrutura do Repositório

```text
.
├── .github/workflows/          # Pipeline de CI/CD (GitHub Actions)
├── 1_local_setup/              # Provisionamento do ambiente local (Docker Compose e config do DB)
├── 2_data_warehouse/           # Projeto dbt completo (Staging, Intermediate, Mart e Seeds)
├── 3_airflow/                  # Orquestração (DAGs, Imagem Customizada com Dockerfile e Cosmos)
└── README.md