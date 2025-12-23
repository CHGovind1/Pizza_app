from fastapi import FastAPI
from pydantic import BaseModel
import uuid

app = FastAPI()
orders = {}

class MCPRequest(BaseModel):
    method: str
    params: dict = {}

@app.post("/mcp/call")
def mcp_call(request: MCPRequest):
    if request.method == "place_order":
        order_id = f"ORD-{uuid.uuid4().hex[:6].upper()}"
        orders[order_id] = {"status": "preparing", **request.params}
        return {"order_id": order_id, "eta": "25 mins"}

@app.get("/")
def root():
    return {"status": "running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
