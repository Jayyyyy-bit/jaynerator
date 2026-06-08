from typing import Callable

_hooks: dict[str, list[Callable]] = {
    "before_generate": [],
    "after_generate": [],
    "before_write": [],
    "after_write": [],
}


def register(event: str, fn: Callable) -> None:
    """Register a functtion to a lifecycle event."""
    if event not in _hooks:
        raise ValueError(
            f"Unknown event '{event}'. Valid: {list(_hooks.keys())}")
    _hooks[event].append(fn)


def fire(event: str, **kwargs) -> None:
    """Fire all registered hooks for an event."""
    for fn in _hooks.get(event, []):
        fn(**kwargs)
