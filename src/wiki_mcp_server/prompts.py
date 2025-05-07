"""MCP Prompts for guiding wiki operations."""

from wiki_mcp_server.server import mcp
from mcp.server.fastmcp.prompts import base


@mcp.prompt()
def manage_wiki_prompt() -> str:
    """Prompt for basic wiki operations guidance."""
    return (
        "You are managing knowledge pages across multiple Confluence knowledge bases.\n\n"
        "Available wiki types:\n"
        "- alm_confluence: Global shared public knowledge base (default).\n"
        "- wpb_confluence: WPB department internal knowledge base.\n\n"
        "Choose the correct wiki_type based on user instruction. Default to 'alm' if uncertain.\n"
    )


@mcp.prompt()
def infer_wiki_type_prompt() -> list[base.Message]:
    """Prompt for inferring the wiki_type from a natural language query."""
    return [
        base.UserMessage("Given a user query, determine the most appropriate wiki knowledge base."),
        base.UserMessage(
            "- Use 'alm' if the query mentions 'gsna', 'global', or 'alm-confluence'.\n"
            "- Use 'wpb' if the query mentions 'wpb' or 'wealth'.\n"
            "- Otherwise, default to 'alm'.\n\n"
            "Only output the wiki_type keyword without extra text."
        ),
        base.AssistantMessage("Understood. I'll infer the appropriate wiki_type accordingly."),
    ]