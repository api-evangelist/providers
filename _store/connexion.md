---
aid: connexion
url: https://raw.githubusercontent.com/api-evangelist/connexion/refs/heads/main/apis.yml
name: Connexion
x-type: opensource
description: 'Connexion is an open source Python framework that automatically handles HTTP requests based on OpenAPI specifications. Connexion 3 provides AsyncApp, FlaskApp, and ConnexionMiddleware as primary entry points, with built-in routing, request and response validation, parameter parsing, security enforcement, content negotiation, error handling, lifespan, and Swagger UI integration. Connexion takes a contract-first, design-first approach: the OpenAPI specification is the source of truth and Python handlers are resolved from operationId or via configurable resolvers.'
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Design
  - ASGI
  - Design-First
  - Flask
  - OpenAPI
  - Python
  - Validation
  - WSGI
created: '2026-03-25'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: connexion:framework
    name: Connexion Python Framework
    description: Connexion is a contract-first Python web framework that loads an OpenAPI specification and routes requests to Python handlers based on operationId. It performs request validation, parameter parsing, and response validation against the specification, with first-class support for security schemes and Swagger UI.
    humanURL: https://connexion.readthedocs.io/en/latest/
    baseURL: https://connexion.readthedocs.io
    tags:
      - Framework
      - OpenAPI
      - Python
      - Validation
    properties:
      - type: Documentation
        url: https://connexion.readthedocs.io/en/latest/
      - type: Documentation
        url: https://connexion.readthedocs.io/en/latest/quickstart.html
      - type: GitHubRepository
        url: https://github.com/spec-first/connexion
      - type: License
        url: https://github.com/spec-first/connexion/blob/main/LICENSE
      - type: Issue Tracker
        url: https://github.com/spec-first/connexion/issues
    x-features:
      - AsyncApp, FlaskApp, and ConnexionMiddleware entry points
      - Native ASGI server support and Flask compatibility
      - Automatic routing from operationId via RestyResolver
      - Request and response validation against OpenAPI
      - Security middleware honoring OpenAPI security schemes
      - Swagger UI mounted from the framework
      - Pythonic snake_case parameter conversion
      - Strict parameter validation modes
    x-useCases:
      - Build Python APIs from an OpenAPI 3.x specification
      - Migrate Flask applications to a contract-first model
      - Add request and response validation to an existing ASGI app
      - Generate Swagger UI alongside your API automatically
      - Compose multiple OpenAPI specifications under a single app
  - aid: connexion:middleware
    name: Connexion Middleware Stack
    description: Connexion 3 introduces a stack of pluggable ASGI middlewares that handle exceptions, server errors, lifespan, security, routing, request validation, response validation, Swagger UI, and context propagation. The middleware stack can be applied to any ASGI or WSGI application via ConnexionMiddleware.
    humanURL: https://connexion.readthedocs.io/en/latest/middleware.html
    baseURL: https://connexion.readthedocs.io
    tags:
      - ASGI
      - Middleware
      - WSGI
    properties:
      - type: Documentation
        url: https://connexion.readthedocs.io/en/latest/middleware.html
      - type: Reference
        url: https://github.com/spec-first/connexion/tree/main/connexion/middleware
    x-features:
      - Routing, security, request, and response validation middleware
      - SwaggerUIMiddleware for interactive docs
      - LifespanMiddleware for startup and shutdown hooks
      - ContextMiddleware to propagate request context
    x-useCases:
      - Add Connexion validation to FastAPI or Starlette
      - Wrap an existing WSGI application without rewriting handlers
      - Customize the middleware stack for a specific deployment
common:
  - type: Website
    url: https://connexion.readthedocs.io/
  - type: Documentation
    url: https://connexion.readthedocs.io/en/latest/quickstart.html
  - type: GitHubRepository
    url: https://github.com/spec-first/connexion
  - type: GitHub Organization
    url: https://github.com/spec-first
  - type: Issue Tracker
    url: https://github.com/spec-first/connexion/issues
  - type: Change Log
    url: https://github.com/spec-first/connexion/releases
  - type: License
    url: https://github.com/spec-first/connexion/blob/main/LICENSE
  - type: PyPI
    url: https://pypi.org/project/connexion/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
