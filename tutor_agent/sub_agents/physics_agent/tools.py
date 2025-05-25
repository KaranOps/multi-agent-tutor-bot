"""
Physics Constants Tool

This module provides a tool for retrieving fundamental physics constants.
"""

from typing import Dict, Any
import time

def get_physics_constant(constant_name: str) -> Dict[str, Any]:
    """""
    Retrieve a physics constant's value and description.

    Args:
        constant_name (str): Name of the constant (e.g., "speed of light").
    
    Returns:
        Dict[str,Any] : Dictionary with constant data or error message.
    """
    try:
        constants = {
            "speed_of_light": {
                "value": 300000000,
                "unit": "m/s",
                "description": "Speed of light in a vacuum"
            },
            "gravitational_constant": {
                "value": 6.67430e-11,
                "unit": "m³ kg⁻¹ s⁻²",
                "description": "Universal gravitational constant"
            },
            "planck_constant": {
                "value": 6.62607015e-34,
                "unit": "J·s",
                "description": "Planck's constant"
            }
        }

        normalized_name = constant_name.strip().lower().replace(" ","_")

        if normalized_name in constants:
            const_data = constants[normalized_name]
            return{
                "result": {
                    "constant": normalized_name,
                    "value": f"{const_data['calue']}{const_data['unit']}",
                    "description": const_data["description"]
                },
                "status": "success",
                "additional_info": {
                    "data_format": "dictionary",
                    "collection_timestamp": time.time()
                }
            }
        else:
            available = list(constants.keys())
            return {
                "result": {"error": f"Constant '{constant_name}' not found."},
                "status": "error",
                "additional_info":{
                    "available_constants": available,
                    "note": "Use exact names like 'speed_of_light'"
                }
            }
    except Exception as e:
        return {
            "result": {"error": f"Unexpected error: {str(e)}"},
            "status": "error",
            "additional_info": {"error_type": str(type(e).__name__)}
        }