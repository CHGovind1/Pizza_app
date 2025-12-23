import requests

PIZZA_MCP_URL = "http://localhost:8000/mcp/call"

class PizzaAgent:
    def call_mcp(self, method, params=None):
        resp = requests.post(PIZZA_MCP_URL, json={
            "method": method,
            "params": params or {}
        })
        return resp.json()
    
    def parse_order(self, user_input):
        return {"pizza": "Margherita", "size": "large"}
    
    def handle_order(self, user_input):
        order_details = self.parse_order(user_input)
        return self.call_mcp("place_order", order_details)

agent = PizzaAgent()
