
from airflow.models.dagbag import DagBag

# https://stackoverflow.com/questions/65059259/debugging-airflow-tasks-using-airflow-test-vs-using-debugexecutor
if __name__ == '__main__':

    dag_file_path = "example_bash_operator.py"
    dagbag = DagBag(dag_folder=dag_file_path)
    dagbag.dags['example_bash_operator'].task_dict['run_after_loop'].execute({})