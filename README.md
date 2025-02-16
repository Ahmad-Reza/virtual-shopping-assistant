# 🛍️ Virtual Shopping Assistant
Virtual Shopping Assistant that assists online shoppers in navigating multiple fashion e-commerce platforms. The agent should interpret user requests, decide which external tools to utilize, and integrate the obtained information to provide coherent and helpful responses.

# Virtual Shopping Assistant – Agent Flowchart  

## 1. Overview  
This flowchart illustrates the workflow of the **Virtual Shopping Assistant**, detailing how the **LLM-powered agent** processes user queries, utilizes external tools, and generates intelligent responses.  

## 2. Flowchart Representation  
![Virtual Shopping Assistant Flowchart](https://github.com/Ahmad-Reza/virtual-shopping-assistant/blob/master/virtual_shopping_agent_flowchart.png)  

## 🔥 Overview of the Implementation
The **Virtual Shopping Assistant** leverages an **LLM Agent** to perform various shopping-related tasks, including:

✅ **Search for products**  
✅ **Check discounts**  
✅ **Estimate shipping times**  
✅ **Compare competitor prices**  
✅ **Verify return policies**  
✅ **Perform multi-step reasoning**  

---
## 🚀 Main Components

### 🏗️ **FastAPI Backend**
The backend handles the logic and tool integration for shopping assistance.

- **`main.py`** → Defines the FastAPI server and exposes endpoints.
- **`tools.py`** → Implements shopping-related tools (APIs for search, discount, shipping, etc.).
- **`agent.py`** → LLM-based agent that decides which tool(s) to use.

### 📱 **Android Client**
The Android app calls the assistant API and displays results.
- **Uses Retrofit** for API communication.

---

## 🛠 Implementation Steps

### **Step 1: Define Shopping Tools in `tools.py`**
Each tool represents an **API function** the AI assistant can use.

### **Step 2: Define LLM Agent in `agent.py`**
The agent decides which tools to invoke based on the user query.

### **Step 3: Expose API in `main.py`**
Define API routes to interact with the agent.

### **Step 4: Implement API Calls in Android**
Use Retrofit to connect the Android client to the assistant API.

---

## 💡 Example Tasks

### **Task A: Basic Item Search + Price Constraint**
📌 **User Input:**  
> "Find a floral skirt under $40 in size S. Is it in stock, and can I apply a discount code ‘SAVE10’?"

✅ **Agent Workflow:**
1. Calls **Product Search Tool** → Finds Floral Skirt
2. Calls **Discount Checker Tool** → Applies `SAVE10`

---

### **Task B: Shipping Deadline**
📌 **User Input:**  
> "I need white sneakers (size 8) for under $70 that can arrive by Friday."

✅ **Agent Workflow:**
1. Calls **Product Search Tool** → Finds White Sneakers
2. Calls **Shipping Estimator Tool** → Confirms delivery before Friday

---

### **Task C: Competitor Price Comparison**
📌 **User Input:**  
> "I found a ‘casual denim jacket’ at $80 on SiteA. Any better deals?"

✅ **Agent Workflow:**
1. Calls **Price Comparison Tool** → Finds alternative deals

---

🎯 **Goal:** Provide an intelligent, AI-powered virtual shopping experience! 🚀
