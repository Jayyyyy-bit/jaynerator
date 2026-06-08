from generator.plugins.base import StackPlugin

TYPES = {
    "1": {
        "key":         "express_route",
        "label":       "Express Route",
        "description": "REST API endpoints using Express — pinaka-common na Node.js framework",
        "examples":    "UserRoute, ProductRoute, AuthRoute",
    },
    "2": {
        "key":         "fastify_route",
        "label":       "Fastify Route",
        "description": "REST API endpoints using Fastify — mas mabilis, mas modern kaysa Express",
        "examples":    "UserRoute, ProductRoute, OrderRoute",
    },
    "3": {
        "key":         "nestjs_controller",
        "label":       "NestJS Controller",
        "description": "Controller using NestJS — enterprise-level, TypeScript-first na framework",
        "examples":    "UserController, AuthController, ProductController",
    },
}


class NodePlugin(StackPlugin):
    name = "node"
    label = "Node.js Backend"
    stack = "backend"
    templates = "node"
    types = TYPES
