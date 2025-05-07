"""MCP Tools for wiki page operations.

This module provides tools for creating, updating, deleting, and searching wiki pages.
"""

from wiki_mcp_server.resources import WikiPage
from wiki_mcp_server.server import mcp
from wiki_mcp_server.utils import infer_wiki_type_from_query
from wiki_mcp_server.session_context import UserSessionContext
from wiki_mcp_server.service import create_page as svc_create_page
from wiki_mcp_server.service import update_page as svc_update_page
from wiki_mcp_server.service import delete_page as svc_delete_page
from wiki_mcp_server.service import search_page as svc_search_page

@mcp.tool()
def create_page(space_key: str, title: str, content: str, user_query: str = "", wiki_type: str = "") -> WikiPage:
    """Create a new wiki page."""
    selected_wiki_type = wiki_type or infer_wiki_type_from_query(user_query)
    username = UserSessionContext.get_username()
    wiki_configs = UserSessionContext.get_wiki_configs()
    config = wiki_configs.get(selected_wiki_type)

    result = svc_create_page(
        base_url=config["base_url"],
        username=username,
        api_token=config["api_token"],
        space_key=space_key,
        title=title,
        content=content
    )

    return WikiPage(
        id=result["id"],
        title=result["title"],
        url=f"{config['base_url']}/pages/{result['id']}",
        space=space_key
    )

@mcp.tool()
def update_page(page_id: str, title: str, content: str, version: int, user_query: str = "", wiki_type: str = "") -> WikiPage:
    """Update an existing wiki page."""
    selected_wiki_type = wiki_type or infer_wiki_type_from_query(user_query)
    username = UserSessionContext.get_username()
    wiki_configs = UserSessionContext.get_wiki_configs()
    config = wiki_configs.get(selected_wiki_type)

    result = svc_update_page(
        base_url=config["base_url"],
        username=username,
        api_token=config["api_token"],
        page_id=page_id,
        title=title,
        content=content,
        version=version
    )

    return WikiPage(
        id=result["id"],
        title=result["title"],
        url=f"{config['base_url']}/pages/{result['id']}",
        space=result["space"]["key"]
    )

@mcp.tool()
def delete_page(page_id: str, user_query: str = "", wiki_type: str = "") -> str:
    """Delete a wiki page."""
    selected_wiki_type = wiki_type or infer_wiki_type_from_query(user_query)
    username = UserSessionContext.get_username()
    wiki_configs = UserSessionContext.get_wiki_configs()
    config = wiki_configs.get(selected_wiki_type)

    svc_delete_page(
        base_url=config["base_url"],
        username=username,
        api_token=config["api_token"],
        page_id=page_id
    )

    return f"Page {page_id} successfully deleted."

@mcp.tool()
def search_page(space_key: str, keyword: str, user_query: str = "", wiki_type: str = "") -> dict:
    """Search wiki pages by keyword."""
    selected_wiki_type = wiki_type or infer_wiki_type_from_query(user_query)
    username = UserSessionContext.get_username()
    wiki_configs = UserSessionContext.get_wiki_configs()
    config = wiki_configs.get(selected_wiki_type)

    result = svc_search_page(
        base_url=config["base_url"],
        username=username,
        api_token=config["api_token"],
        space_key=space_key,
        keyword=keyword
    )

    return {"results": result.get("results", [])}