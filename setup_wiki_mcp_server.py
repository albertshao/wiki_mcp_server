import os

BASE_DIR = "wiki_mcp_server"
SRC_DIR = os.path.join(BASE_DIR, "src/wiki_mcp_server")

# 要创建的目录
dirs = [
    SRC_DIR,
]

# 每个文件及其初始内容
files = {
    os.path.join(SRC_DIR, "__init__.py"): "",
    os.path.join(SRC_DIR, "server.py"): '''"""MCP Server main entry point."""

from mcp_sdk import MCPServer
from wiki_mcp_server.prompts import manage_wiki_prompt, infer_wiki_type_prompt
from wiki_mcp_server.tools import create_page, update_page, delete_page, search_page
from wiki_mcp_server.resources import WikiPage

mcp = MCPServer(name="Wiki MCP Server", port=9999, host="0.0.0.0")

mcp.add_prompt(manage_wiki_prompt)
mcp.add_prompt(infer_wiki_type_prompt)
mcp.add_resource(WikiPage)
mcp.add_tool(create_page)
mcp.add_tool(update_page)
mcp.add_tool(delete_page)
mcp.add_tool(search_page)

app = mcp.app
''',
    os.path.join(SRC_DIR, "tools.py"): '''"""MCP Tools for managing wiki pages."""
# Placeholder for create_page, update_page, delete_page, search_page functions
''',
    os.path.join(SRC_DIR, "prompts.py"): '''"""MCP Prompts for wiki_type guidance."""
# Placeholder for manage_wiki_prompt, infer_wiki_type_prompt
''',
    os.path.join(SRC_DIR, "resources.py"): '''"""MCP Resources for wiki operations."""
# Placeholder for WikiPage resource
''',
    os.path.join(SRC_DIR, "utils.py"): '''"""Utility functions like wiki_type inference."""
# Placeholder for local keyword matching and LLM-based inference
''',
    os.path.join(BASE_DIR, "requirements.txt"): '''fastapi
uvicorn
requests
mcp-sdk
''',
    os.path.join(BASE_DIR, "Dockerfile"): '''# Dockerfile for Wiki MCP Server
FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/ src/

CMD ["uvicorn", "wiki_mcp_server.server:app", "--host", "0.0.0.0", "--port", "9999"]
''',
    os.path.join(BASE_DIR, "README.md"): "# Wiki MCP Server\n\nMCP server implementation for managing wiki pages.",
    os.path.join(BASE_DIR, "pyproject.toml"): '''# Placeholder pyproject.toml
[tool.poetry]
name = "wiki-mcp-server"
version = "0.1.0"
description = "A Model Context Protocol server for Wiki management."
''',
    os.path.join(BASE_DIR, "smithery.yaml"): '''# Smithery deployment config
mcpServer:
  name: wiki-mcp-server
  command: uvicorn
  args:
    - src/wiki_mcp_server/server:app
''',
    os.path.join(BASE_DIR, ".gitignore"): '''__pycache__/
*.pyc
.env
''',
}

def create_structure():
    for d in dirs:
        os.makedirs(d, exist_ok=True)
        print(f"Created directory: {d}")

    for path, content in files.items():
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as f:
            f.write(content)
        print(f"Created file: {path}")

if __name__ == "__main__":
    create_structure()