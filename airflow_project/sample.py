# Import the modules
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime
from hello_world import print_hello_world

# Define the default arguments
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 8, 31),
    'retries': 1,
}

# Define the DAG
dag = DAG(
    dag_id='hello_world',
    default_args=default_args,
    schedule='@daily',
)

# Define the tasks
task_1 = BashOperator(
    task_id='print_hello',
    bash_command='echo "Hello World from Bash!!"',
    dag=dag,
)

task_2 = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag,
)

task_3 = PythonOperator(
    task_id='print_hello_python',
    python_callable= print_hello_world,
    dag=dag,
)

# Define the dependencies
task_1 >> [task_2, task_3]
 