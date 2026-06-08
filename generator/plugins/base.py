class StackPlugin:
    name      : str = ""      # unique id  e.g. "react"
    label     : str = ""      # display    e.g. "React + TypeScript"
    stack     : str = ""      # category   e.g. "frontend"
    templates : str = ""      # subfolder  e.g. "frontend"
    types     : dict = {}     # same TYPES format as in interactive.py

    def get_types(self) -> dict:
        return self.types

    def get_template_dir(self) -> str:
        return self.templates

    def describe(self) -> str:
        return f"[{self.stack.upper()}] {self.label}"