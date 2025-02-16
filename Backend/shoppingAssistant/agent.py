import os
import warnings

from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
from langchain_openai import OpenAI

from tools import search_products, estimate_shipping, check_discount, compare_prices, check_return_policy

from dotenv import load_dotenv

load_dotenv()

# Suppress warnings
warnings.filterwarnings("ignore", category=UserWarning, module="langchain")

# Load OpenAI API key from environment variable
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("Missing OPENAI_API_KEY. Set it in your environment variables.")

# Create Tool Wrappers
tools = [
    Tool(name="Product Search", func=search_products, description="Search for products based on filters."),
    Tool(name="Discount Checker", func=check_discount, description="Verify and apply discount codes."),
    Tool(name="Shipping Estimator", func=estimate_shipping, description="Estimate delivery times."),
    Tool(name="Price Comparison", func=compare_prices, description="Compare competitor prices."),
    Tool(name="Return Policy Checker", func=check_return_policy, description="Check return policies of online stores."),
]

# Initialize LLM Agent
llm = OpenAI(model="gpt-3.5-turbo", api_key=OPENAI_API_KEY)

# client = OpenAI(api_key=OPENAI_API_KEY)  # Replace with your actual API key
# models = client.models.list()
# for model in models.data:
#     print(model.id)

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,  # Uses ReAct (reasoning + acting)
    verbose=True
)
