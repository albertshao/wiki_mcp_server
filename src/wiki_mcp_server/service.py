"""Service layer for interacting with Confluence APIs.

This module provides helper functions to create, update, delete, and search wiki pages
on Confluence using REST APIs.

Author: Shawn
"""

import logging
import requests
from typing import Optional, Dict

logger = logging.getLogger(__name__)

def build_auth(username: str, api_token: str) -> tuple:
    """Build basic authentication tuple for requests.

    Args:
        username (str): Confluence username/email.
        api_token (str): Confluence API token.

    Returns:
        tuple: Authentication credentials for requests.
    """
    return (username, api_token)

def create_page(base_url: str, username: str, api_token: str, space_key: str, title: str, content: str) -> Dict:
    """Create a new page in Confluence.

    Args:
        base_url (str): Confluence REST API base URL.
        username (str): Username for authentication.
        api_token (str): API token for authentication.
        space_key (str): Target space key.
        title (str): Title of the new page.
        content (str): Page content in HTML format.

    Returns:
        Dict: Response JSON containing page metadata.
    """
    url = f"{base_url}/content"
    headers = {"Content-Type": "application/json"}
    payload = {
        "type": "page",
        "title": title,
        "space": {"key": space_key},
        "body": {
            "storage": {
                "value": content,
                "representation": "storage"
            }
        }
    }

    logger.info(f"Creating page '{title}' in space '{space_key}'...")
    response = requests.post(url, auth=build_auth(username, api_token), headers=headers, json=payload)
    response.raise_for_status()

    return response.json()

def update_page(base_url: str, username: str, api_token: str, page_id: str, title: str, content: str, version: int) -> Dict:
    """Update an existing Confluence page.

    Args:
        base_url (str): Confluence REST API base URL.
        username (str): Username for authentication.
        api_token (str): API token for authentication.
        page_id (str): ID of the page to update.
        title (str): New title for the page.
        content (str): Updated content.
        version (int): Current version of the page (must increment).

    Returns:
        Dict: Response JSON containing updated page metadata.
    """
    url = f"{base_url}/content/{page_id}"
    headers = {"Content-Type": "application/json"}
    payload = {
        "id": page_id,
        "type": "page",
        "title": title,
        "version": {"number": version + 1},
        "body": {
            "storage": {
                "value": content,
                "representation": "storage"
            }
        }
    }

    logger.info(f"Updating page '{page_id}' to title '{title}'...")
    response = requests.put(url, auth=build_auth(username, api_token), headers=headers, json=payload)
    response.raise_for_status()

    return response.json()

def delete_page(base_url: str, username: str, api_token: str, page_id: str) -> None:
    """Delete a Confluence page.

    Args:
        base_url (str): Confluence REST API base URL.
        username (str): Username for authentication.
        api_token (str): API token for authentication.
        page_id (str): ID of the page to delete.

    Returns:
        None
    """
    url = f"{base_url}/content/{page_id}"
    logger.info(f"Deleting page '{page_id}'...")
    response = requests.delete(url, auth=build_auth(username, api_token))
    response.raise_for_status()

def search_page(base_url: str, username: str, api_token: str, space_key: str, keyword: str) -> Dict:
    """Search for pages in a space matching a keyword.

    Args:
        base_url (str): Confluence REST API base URL.
        username (str): Username for authentication.
        api_token (str): API token for authentication.
        space_key (str): Confluence space key.
        keyword (str): Keyword to search.

    Returns:
        Dict: Search results.
    """
    url = f"{base_url}/content/search"
    headers = {"Content-Type": "application/json"}
    params = {
        "cql": f"space = \"{space_key}\" AND text ~ \"{keyword}\""
    }

    logger.info(f"Searching pages with keyword '{keyword}' in space '{space_key}'...")
    response = requests.get(url, auth=build_auth(username, api_token), headers=headers, params=params)
    response.raise_for_status()

    return response.json()