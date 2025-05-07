"""Session context for managing user authentication and wiki configuration."""

from contextvars import ContextVar
from typing import Dict

_username: ContextVar[str] = ContextVar("username", default="")
_wiki_configs: ContextVar[Dict[str, Dict[str, str]]] = ContextVar("wiki_configs", default={})

class UserSessionContext:
    """Manage user and wiki configurations within request context."""

    @classmethod
    def set_session(cls, username: str, wiki_configs: Dict[str, Dict[str, str]]):
        """Set user session."""
        _username.set(username)
        _wiki_configs.set(wiki_configs)

    @classmethod
    def get_username(cls) -> str:
        """Get the username from the session."""
        return _username.get()

    @classmethod
    def get_wiki_configs(cls) -> Dict[str, Dict[str, str]]:
        """Get wiki configuration from the session."""
        return _wiki_configs.get()