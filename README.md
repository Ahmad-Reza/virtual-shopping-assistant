# Virtual Shopping Assistant
Virtual Shopping Assistant that assists online shoppers in navigating multiple fashion e-commerce platforms. The agent should interpret user requests, decide which external tools to utilize, and integrate the obtained information to provide coherent and helpful responses.

# Virtual Shopping Assistant – Agent Flowchart  

## 1. Overview  
This flowchart illustrates the workflow of the **Virtual Shopping Assistant**, detailing how the **LLM-powered agent** processes user queries, utilizes external tools, and generates intelligent responses.  

## 2. Flowchart Representation  
![Virtual Shopping Assistant Flowchart](https://github.com/Ahmad-Reza/virtual-shopping-assistant/blob/master/virtual_shopping_agent_flowchart.png)  

## 3. Flowchart Breakdown  

### **Step 1: User Input**  
- The user enters a query in text or image format (e.g., *"Find a black leather jacket under $150"*).  
- If an image is provided, the **Visual Search Tool** extracts fashion attributes.  

### **Step 2: LLM Reasoning & Planning**  
- The **LLM Agent** determines the best approach to fulfill the query.  
- It decides which tools to invoke based on reasoning models like **ReAct, Toolformer, and Chain of Tools**.  

### **Step 3: Tool Utilization**  
- The assistant calls relevant tools based on query requirements:  
  - **E-commerce Search Aggregator** – Retrieves matching products.  
  - **Price Comparison Tool** – Fetches price data from competitors.  
  - **Shipping Estimator** – Checks delivery feasibility.  
  - **Discount Checker** – Applies promo codes to calculate the final price.  
  - **Return Policy Checker** – Provides return conditions from retailers.  

### **Step 4: Data Integration & Response Generation**  
- The assistant **integrates outputs** from multiple tools.  
- It filters and ranks products based on **relevance, price, and availability**.  
- A **coherent, structured response** is generated for the user.  

### **Step 5: User Interaction & Refinement**  
- The user can refine the search (e.g., adjust budget, add filters).  
- The system **remembers past interactions** and **improves recommendations dynamically**.  

## 4. Conclusion  
This flowchart demonstrates how the **Virtual Shopping Assistant** leverages **agentic reasoning and tool integration** to assist users in making informed shopping decisions across multiple online platforms.  

---
