from fastapi import FastAPI
from mcp.server.fastmcp import FastMCP
import logging

logger = logging.getLogger(__name__)

from wiki_mcp_server.middleware import AuthMiddleware

fastapi_app = FastAPI()
fastapi_app.add_middleware(AuthMiddleware)

# Add health check
@fastapi_app.get("/health")
async def health_check():
    return {"status": "ok"}

# Setup MCP Server
mcp = FastMCP(name="Wiki MCP Server", sse_app=fastapi_app)

app = fastapi_app