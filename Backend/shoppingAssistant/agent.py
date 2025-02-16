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

# Define the AI Model
# llm = OpenAI(temperature=0.5, api_key=OPENAI_API_KEY)

# Define tools (wrapping API functions in LangChain-compatible format)
# search_tool = Tool(
#     name="Product Search",
#     func=lambda query, max_price, size: search_products(query, max_price, size),
#     description="Search for products based on name, price, and size."
# )
#
# shipping_tool = Tool(
#     name="Shipping Estimator",
#     func=lambda destination, deadline: estimate_shipping(destination, deadline),
#     description="Get shipping cost and estimated delivery date."
# )
#
# discount_tool = Tool(
#     name="Discount Checker",
#     func=lambda code, price: check_discount(code, price),
#     description="Apply a discount code to a given price."
# )
#
# price_comparison_tool = Tool(
#     name="Competitor Price Comparison",
#     func=lambda product_name: compare_prices(product_name),
#     description="Compare prices of a product across multiple e-commerce platforms."
# )
#
# return_policy_tool = Tool(
#     name="Return Policy Checker",
#     func=lambda site: check_return_policy(site),
#     description="Get the return policy of a given e-commerce site."
# )

# Create the agent with access to all tools
# agent = initialize_agent(
#     agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
#     tools=[search_tool, shipping_tool, discount_tool, price_comparison_tool, return_policy_tool],
#     llm=llm,
#     verbose=True
# )

# Function to interact with the agent
# def ask_agent(user_query: str):
#     return agent.run(user_query)


# Create Tool Wrappers

tools = [
    Tool(name="Product Search", func=search_products, description="Search for products based on filters."),
    Tool(name="Discount Checker", func=check_discount, description="Verify and apply discount codes."),
    Tool(name="Shipping Estimator", func=estimate_shipping, description="Estimate delivery times."),
    Tool(name="Price Comparison", func=compare_prices, description="Compare competitor prices."),
    Tool(name="Return Policy Checker", func=check_return_policy, description="Check return policies of online stores."),
]

# Initialize LLM Agent
llm = OpenAI(model="gpt-4", api_key=os.environ["OPENAI_API_KEY"])

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,  # Uses ReAct (reasoning + acting)
    verbose=True
)
