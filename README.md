# Airflow-dags

## Overview
- This airflow dags repo is a part of project [Running Airflow on Kubernetes](https://github.com/heraclex/kubernetes-playground/tree/main/airflow-v2-kind-cluster).
- The repo contains airflow examples and also some guideline how to debug airflow locally.

## Prerequisite
- Python version 3.x
- Using one of virtual environment management:
  * [pyenv](https://github.com/pyenv/pyenv) (recommended)
  * [conda](https://docs.conda.io/en/latest/)
  * [poetry](https://python-poetry.org/)
- Python IDE:
  * [Pycharm](https://www.jetbrains.com/pycharm/) (recommended)
  * [VSCode](https://code.visualstudio.com/)

## How Airflow dags can be loaded to airflow?
- All DAGs will be in sync with airflow cluster running on kubernetes. There is a git-hook to periodically check all repo chances to load latest dags to airflow.
- When you commit DAGs to repo, it will need 3-5min to be loaded to airflow.
- Once it's loaded, you will see from airflow-ui.

## How to debug Airflow dags locally?
1. You need to install all airflow dependency packages in your virtual environment.
2. Use `airflow test` command to test
```bash
# create virtual environment with pyenv
pyenv virtualenv 3.9.1 airflowv2_3.9 

# activate virtual env
pyenv activate airflowv2_3.9

# install airflow package
pip install apache-airflow==2.4.1

# starts one DAG Run with DebugExecutor.
airflow dags test {dag-id} {execution-date} 
# eg: airflow dags test example_branch_operator 2022-04-01

# starts one tasks.
airflow tasks test {task-id}
```
3. Using DagBag
```python
from airflow.model.dagbag import DagBag
dag_file_path = "/home/test-user/dags/dag-file.py"
dagbag = DagBag(dag_folder=dag_file_path)
dagbag.dags['test-dag-id'].task_dict['task-id'].execute({})
```
4. Note: Run the command `airflow db init` to init sql-lite database  



