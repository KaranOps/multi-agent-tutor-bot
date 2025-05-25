"""
Math Agent

This agent is responsible for solving mathematical problems using the calculator tool.
"""

from google.adk.agents import Agent
from .tools import calculator

math_agent = Agent(
    name="mathAgent",
    model="gemini-2.0-flash",
    description="Solves math expressions using a calculator tool.",
    instruction="""You are a Math Agent.

    When asked a mathematical question, you should:
    1.Use the 'calculator' tool to compute the answer.
    2.Analyze the returned dictionary:
        - result: contains the expressions and computed value
        - status: indicates success or error
        - additional_info: notes about the result
    3.Format a clear response with:
        - The original expression
        - The final result
        - Any helpful notes if available

    IMPORTANT: You MUST call the calculator tool. Do not guess or create your own answers.
    """,
    tools=[calculator],
    output_key="math_solution"
)