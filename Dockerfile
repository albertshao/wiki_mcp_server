# Dockerfile for Wiki MCP Server
FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/ src/

CMD ["uvicorn", "wiki_mcp_server.server:app", "--host", "0.0.0.0", "--port", "9999"]
