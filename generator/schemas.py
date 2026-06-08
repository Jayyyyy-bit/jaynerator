from pydantic import BaseModel, field_validator
from typing import Optional


class PathsSchema(BaseModel):
    #  Frontend 
    component : str
    page      : str
    form      : str
    layout    : str
    modal     : str
    hook      : str
    # Python backend 
    fastapi_route : str = "src/api/routes"
    fastapi_model : str = "src/api/models"
    scraper       : str = "src/scrapers"
    neural_net    : str = "src/models"
    cli           : str = "src/cli"
    cyber         : str = "src/tools"
    # Node.js backend
    express_route     : str = "src/routes"
    fastify_route     : str = "src/routes"
    nestjs_controller : str = "src/controllers"
    # Rust backend
    axum_route : str = "src/routes"
    systems    : str = "src/systems"

    @field_validator("*")
    @classmethod
    def must_not_be_empty(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError("Path cannot be empty.")
        return v


class GeneratorConfig(BaseModel):
    overwrite: bool = False
    dry_run: bool = False
    log: bool = True
    log_file: str = "generated.log"


class ProjectConfig(BaseModel):
    paths: PathsSchema
    config: Optional[GeneratorConfig] = GeneratorConfig()
