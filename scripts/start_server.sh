#!/bin/bash

# -------------------------------------
# Script to start Wiki MCP Server
# Author: Shawn
# -------------------------------------

# Move to project root directory
cd "$(dirname "$0")/.."

echo "✅ Current directory: $(pwd)"
echo "✅ Setting PYTHONPATH to include src/"

export PYTHONPATH=./src

echo "✅ Starting Uvicorn server..."

uvicorn wiki_mcp_server.server:app --host 0.0.0.0 --port 9999 --reload