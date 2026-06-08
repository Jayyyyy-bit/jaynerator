import importlib
import pkgutil
from generator.plugins.base import StackPlugin

class PluginRegistry:
    def __init__(self):
        self._plugins: dict[str, StackPlugin] = {}

    def load_plugins(self) -> None:
        """Auto-discover and load all plugins in stacks/ folder."""
        import generator.plugins.stacks as stacks_pkg

        for _, module_name, _ in pkgutil.iter_modules(stacks_pkg.__path__):
            module = importlib.import_module(
                f"generator.plugins.stacks.{module_name}"
            )

            # Find all StackPlugin subclasses in module 
            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                if (
                    isinstance(attr, type)
                    and issubclass(attr, StackPlugin)
                    and attr is not StackPlugin
                ):
                    instance = attr()
                    self._plugins[instance.name] = instance

    def get(self, name: str) -> StackPlugin | None:
        return self._plugins.get(name)

    def all(self) -> dict[str, StackPlugin]:
        return self._plugins

    def by_stack(self, stack: str) -> list[StackPlugin]:
        return [p for p in self._plugins.values() if p.stack == stack]


#  Global registry instance 
registry = PluginRegistry()
registry.load_plugins()