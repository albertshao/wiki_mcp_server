"""MCP Resources for wiki operations.

This module defines resources representing wiki pages and standard responses.
"""
from wiki_mcp_server.server import mcp

from pydantic import BaseModel

@mcp.resource()
class WikiPage(BaseModel):
    """Resource representing a Confluence wiki page."""
    id: str
    title: str
    url: str
    space: str
