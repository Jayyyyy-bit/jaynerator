from generator.plugins.base import StackPlugin

TYPES = {
    "1": {
        "key":         "fastapi_route",
        "label":       "FastAPI Route",
        "description": "REST API endpoints — GET, POST, PUT, DELETE. Ginagamit sa web apps, mobile backends, ML APIs",
        "examples":    "UserRoute, ProductRoute, AuthRoute",
    },
    "2": {
        "key":         "fastapi_model",
        "label":       "FastAPI Model",
        "description": "Pydantic model — para sa request/response validation ng API mo",
        "examples":    "UserModel, ProductModel, TokenModel",
    },
    "3": {
        "key":         "scraper",
        "label":       "Web Scraper",
        "description": "Mag-e-extract ng data galing sa websites — useful sa research, monitoring, automation",
        "examples":    "ShoppingScraper, NewsScraper, PriceScraper",
    },
    "4": {
        "key":         "neural_net",
        "label":       "Neural Network",
        "description": "PyTorch model — ready to train. Para sa image classification, text analysis, ML projects",
        "examples":    "ImageClassifier, SentimentModel, FraudDetector",
    },
    "5": {
        "key":         "cli",
        "label":       "CLI Tool",
        "description": "Command-line tool using Typer — para sa automation scripts at developer tools",
        "examples":    "FileTool, DeployTool, MigrationTool",
    },
    "6": {
        "key":         "cyber",
        "label":       "Cyber / Recon Tool",
        "description": "Network scanner, recon, at security tools — para sa ethical hacking at security research",
        "examples":    "PortScanner, DomainRecon, SubnetMapper",
    },
}


class PythonPlugin(StackPlugin):
    name      = "python"
    label     = "Python Backend"
    stack     = "backend"
    templates = "python"
    types     = TYPES