from datetime import datetime
from pathlib import Path
from cosmos import DbtDag, ProjectConfig, ProfileConfig, ExecutionConfig

dbt_project_path = Path("/usr/local/airflow/dags/dw_bootcamp")

my_cosmos_dag = DbtDag(
    project_config=ProjectConfig(
        dbt_project_path=dbt_project_path,
    ),
    profile_config=ProfileConfig(
        profile_name="dw_bootcamp",
        target_name="dev",
        profiles_yml_filepath=dbt_project_path / "profiles.yml",
    ),
    execution_config=ExecutionConfig(
        dbt_executable_path="/usr/local/airflow/venv/bin/dbt",
    ),
    dag_id="dag_dw_bootcamp_dev",
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
)