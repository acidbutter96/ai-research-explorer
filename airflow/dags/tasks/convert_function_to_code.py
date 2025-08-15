from airflow.decorators import task


@task
def convert_function_to_code(function):
    """
    Converts a string representing a math function (e.g., 'x**2') to a Python lambda function.
    
    Args:
        function (str): The string representation of the function (e.g., 'x**2').
        
    Returns:
        callable: A lambda function representing the math expression.
    """
    return eval(f"lambda x: {function}")
