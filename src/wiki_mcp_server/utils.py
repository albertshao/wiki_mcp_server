"""Utility functions for wiki_type inference and LLM-based inference.

This module provides helper functions to infer the appropriate wiki_type
based on user queries, supporting both local keyword matching and optional
LLM-based inference.

Author: Shawn
"""

import logging
from typing import Optional

# Default wiki_type if none can be inferred
DEFAULT_WIKI_TYPE = "alm"

logger = logging.getLogger(__name__)

def infer_wiki_type_from_query(user_query: Optional[str]) -> str:
    """Infer the wiki_type from the user query using local keyword matching.

    Args:
        user_query (Optional[str]): The natural language user query.

    Returns:
        str: The inferred wiki_type. Defaults to 'alm' if no keywords matched.
    """
    if not user_query:
        logger.info("No user query provided, defaulting to 'alm'.")
        return DEFAULT_WIKI_TYPE

    query = user_query.lower()

    # Local keyword matching
    if "gsna" in query or "global" in query or "alm-confluence" in query:
        logger.info("Matched 'alm' keywords in user query.")
        return "alm"
    if "wpb" in query or "wealth" in query:
        logger.info("Matched 'wpb' keywords in user query.")
        return "wpb"
    if "cmb" in query or "commercial" in query:
        logger.info("Matched 'cmb' keywords in user query.")
        return "cmb"

    logger.info("No keywords matched, defaulting to 'alm'.")
    return DEFAULT_WIKI_TYPE

# (Optional) Placeholder for future LLM-based inference integration
def infer_wiki_type_using_llm(user_query: str) -> str:
    """Placeholder for LLM-based inference (future enhancement).

    Args:
        user_query (str): The user query text.

    Returns:
        str: Inferred wiki_type by LLM (currently not implemented).
    """
    raise NotImplementedError("LLM-based inference is not yet implemented.")
