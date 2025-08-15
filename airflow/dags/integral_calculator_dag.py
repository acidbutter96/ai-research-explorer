import sys
import os
from airflow.decorators import dag

sys.path.append(os.path.dirname(__file__))
from tasks.convert_function_to_code import convert_function_to_code




@dag(
    max_active_runs=1,
    schedule=None,
    tags=['example', 'calculus'],
    catchup=False,
)
def integral_calculator():
    """
    This DAG is designed to calculate the integral of a function using the
    `integral_calculator` operator.
    """
    # from operators.integral_calculator import IntegralCalculatorOperator

    # # Define the function to integrate
    # def function_to_integrate(x):
    #     return x ** 2

    # # Create an instance of the IntegralCalculatorOperator
    # integral_calculator = IntegralCalculatorOperator(
    #     task_id='calculate_integral',
    #     function=function_to_integrate,
    #     lower_bound=0,
    #     upper_bound=10,
    #     num_points=1000,
    # )
    
    def _print_current_dir():
        return (
            f"Current working directory: {os.getcwd()}\n"
            f"DAG file directory: {os.path.dirname(__file__)}"
        )

    def _list_dir_contents():
        dag_dir = os.path.dirname(__file__)
        try:
            entries = os.listdir(dag_dir)
        except OSError as e:
            return f"Could not list directory '{dag_dir}': {e}"
        dirs = sorted([e for e in entries if os.path.isdir(os.path.join(dag_dir, e))])
        files = sorted([e for e in entries if os.path.isfile(os.path.join(dag_dir, e))])
        lines = [f"Directory contents for: {dag_dir}", "Directories:"]
        if dirs:
            lines += [f"  - {d}" for d in dirs]
        else:
            lines.append("  (none)")
        lines.append("Files:")
        if files:
            lines += [f"  - {f}" for f in files]
        else:
            lines.append("  (none)")
        return "\n".join(lines)

    # raise Exception(_list_dir_contents())

    convert_function_to_code_task = convert_function_to_code(function='x**2')

    convert_function_to_code_task


integral_calculator()
