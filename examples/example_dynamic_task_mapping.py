import dagfactory


config_file = "/usr/local/airflow/dags/example_dynamic_task_mapping.yml"
example_dag_factory = dagfactory.DagFactory(config_file)

# Creating task dependencies
example_dag_factory.clean_dags(globals())
example_dag_factory.generate_dags(globals())
