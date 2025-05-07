"""Middleware for extracting authentication and wiki configuration from request headers.

This module sets up user session context based on incoming request headers.
"""

import logging
from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from wiki_mcp_server.session_context import UserSessionContext

logger = logging.getLogger(__name__)

class AuthMiddleware(BaseHTTPMiddleware):
    """Middleware to extract user authentication and wiki configuration."""

    async def dispatch(self, request: Request, call_next):
        logger.info("Processing request...")
        logger.info(f"Request headers: {request.headers}")
        # user_name = request.headers.get("user_name", "").strip()

        # if not user_name:
        #     logger.error("Missing 'user_name' in request headers.")
        #     raise HTTPException(status_code=400, detail="Missing 'user_name' in headers.")

        # wiki_configs = {}
        # for key, value in request.headers.items():
        #     if key.endswith("_confluence_base_url") and value.strip():
        #         prefix = key.replace("_confluence_base_url", "").lower()
        #         base_url = value.strip()
        #         api_token = request.headers.get(f"{prefix}_confluence_api_token", "").strip()

        #         if not api_token:
        #             logger.error(f"Missing API token for wiki_type '{prefix}'.")
        #             raise HTTPException(status_code=400, detail=f"Missing '{prefix}_confluence_api_token' in headers.")

        #         wiki_configs[prefix] = {
        #             "base_url": base_url,
        #             "api_token": api_token
        #         }

        # if not wiki_configs:
        #     logger.error("No valid wiki configurations found.")
        #     raise HTTPException(status_code=400, detail="No valid wiki configurations provided in headers.")

        # # Save session information
        # UserSessionContext.set_session(username=user_name, wiki_configs=wiki_configs)

        # logger.info(f"Session initialized for user: {user_name}, wiki_types: {list(wiki_configs.keys())}")

        response = await call_next(request)
        return response