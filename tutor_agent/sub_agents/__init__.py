"""
Sub-agents package initialization.
Contains Math and Physics specialized agents.
"""

from .math_agent.agent import math_agent
from .physics_agent.agent import physics_agent

__all__ = ['math_agent', 'physics_agent']