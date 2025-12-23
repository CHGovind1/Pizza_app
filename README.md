# Pizza MCP Demo

## 1. What This Code Does

This code demonstrates MCP (Model Context Protocol), a standardized protocol that enables AI agents to call external tools and servers through a simple JSON API. When a user inputs a pizza order like "large margherita pizza", the agent parses the request and makes a POST call to the MCP server's `/mcp/call` endpoint with the method "place_order" and parameters containing pizza type and size. The MCP server generates a real UUID-based order ID (like ORD-C9EF8C), stores the order state, and returns the order ID along with an ETA of 25 minutes. The agent then calculates the dynamic pickup time by adding 25 minutes to the current time and displays a complete human-like order confirmation flow showing the parsing, scheduling, and final order placement.

## 2. Keys Used in MCP Protocol

The core MCP interaction uses a POST request to `/mcp/call` endpoint with a JSON body containing "method" (place_order) and "params" object (pizza: "Margherita", size: "large"). The server responds with JSON containing "order_id" (ORD-C9EF8C format using UUID) and "eta" (25 mins). The server maintains stateful order storage in a dictionary where orders[ORD-C9EF8C] holds the status "preparing" and order parameters. This follows MCP standards for method-params-response pattern, enabling any MCP-compatible AI agent to place orders without custom integrations. The server runs on localhost:8000, making it instantly testable.

## 3. How to Setup This Demo

Setup requires installing FastAPI, Uvicorn, Requests, and Pydantic dependencies, then cloning the repository. Run the MCP server in Terminal 1 using `uvicorn pizza_mcp_server:app --reload --port 8000` to start the FastAPI server. In Terminal 2, execute `python demo.py "large margherita pizza"` to trigger the full agent flow. The demo produces realistic output showing user input parsing, A2A scheduling communication, dynamic pickup time calculation, and final order confirmation, exactly mimicking a production pizza ordering system integrated with AI agents via MCP.


