from dataclasses import dataclass, field


@dataclass
class GenerationContext:
    gen_type: str
    name: str
    plugin_name: str
    stack_dir: str = ""
    extension: str = ""
    base_path: str = ""
    component_file: str = ""
    index_file: str = ""
    content: str = ""
    dry_run: bool = False
    overwrite: bool = False

    def is_valid(self) -> bool:
        return bool(self.gen_type and self.name and self.plugin_name)

    def __str__(self) -> str:
        return f"GenerationContext({self.plugin_name}/{self.gen_type}/{self.name})"
