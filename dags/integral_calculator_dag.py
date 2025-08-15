from airflow.decorators import dag
from tasks.convert_function_to_code import convert_function_to_code

@dag(
    max_active_runs=1,
    schedule_interval=None,
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

    convert_function_to_code_task = convert_function_to_code(function='x**2')
    
    convert_function_to_code_task
    
integral_calculator()