"""
Calculator Tool

This module provides a tool for performing basic arithmetic calculations.
"""

from typing import Dict, Any
def calculator(expression: str) -> Dict[str, Any]:
    """
    Evaluate a basic arithmetic expression.

    Args:
        expression (str): The mathematical expression to evaluate (e.g., "2 + 3 * 4").

    Returns:
        Dict[str, Any]: Dictionary with calculation result and status, formatted for ADK.
    """
    try:
        allowed_names = {
            'abs' : abs,
            'round': round,
            'min' : min,
            'max' : max,
            'pow' : pow
        }

        result = eval(expression,{"__builtins__": {}}, allowed_names)
        return {
            "result":{
                "expression": expression,
                "value": result
            },
            "status": "success",
            "additional_info": {
                "data_format": "dictionary",
                "note": "Supports +, -, *, /, **, and basic math function"
            }
        }
    except Exception as e:
        return {
            "result" : {"error": f"Failed to evaluate expressions: {str(e)}"},
            "status" : "error",
            "additional_info": {
                "error_type": str(type(e).__name__)
            }
        }

