---
aid: swagger
name: Swagger
description: Swagger is an open-source framework by SmartBear for designing, building, documenting, and consuming RESTful APIs using the OpenAPI Specification. Originally created by Wordnik in 2011, Swagger became the OpenAPI Specification (OAS) in 2016 under the OpenAPI Initiative. The Swagger toolset includes Swagger UI for interactive documentation, Swagger Editor for writing OpenAPI specs, and Swagger Codegen for generating client SDKs and server stubs. The latest OpenAPI standard version is 3.2.0 (released September 2025).
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Design
  - Documentation
  - Open Source
  - OpenAPI
  - REST
  - Standard
  - Swagger
url: https://raw.githubusercontent.com/api-evangelist/swagger/refs/heads/main/apis.yml
created: '2025-01-01'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: swagger:swagger-ui
    name: Swagger UI
    description: Swagger UI renders OpenAPI specifications as interactive API documentation, allowing developers to explore and test API endpoints directly in the browser. It generates a rich HTML interface with try-it-out functionality from any OpenAPI 2.0, 3.0, or 3.1 specification.
    humanURL: https://swagger.io/tools/swagger-ui/
    tags:
      - Documentation
      - Interactive Docs
      - Open Source
      - OpenAPI
      - UI
    properties:
      - type: Documentation
        url: https://swagger.io/docs/open-source-tools/swagger-ui/usage/installation/
      - type: Getting Started
        url: https://swagger.io/docs/open-source-tools/swagger-ui/usage/installation/
      - type: GitHub Repository
        url: https://github.com/swagger-api/swagger-ui
      - type: Docker
        url: https://hub.docker.com/r/swaggerapi/swagger-ui
      - type: npm
        url: https://www.npmjs.com/package/swagger-ui
  - aid: swagger:swagger-editor
    name: Swagger Editor
    description: Swagger Editor is a browser-based editor for writing and validating OpenAPI and AsyncAPI specifications with real-time preview and validation. Available as a standalone web application and as Swagger Editor Next (v5).
    humanURL: https://swagger.io/tools/swagger-editor/
    tags:
      - API Design
      - Editor
      - Open Source
      - OpenAPI
    properties:
      - type: Documentation
        url: https://swagger.io/docs/open-source-tools/swagger-editor/
      - type: GitHub Repository
        url: https://github.com/swagger-api/swagger-editor
      - type: Live Demo
        url: https://editor.swagger.io/
  - aid: swagger:swagger-codegen
    name: Swagger Codegen
    description: Swagger Codegen generates server stubs, client SDKs, and API documentation from OpenAPI specifications in over 40 languages including Python, Java, JavaScript, Go, Ruby, C#, Swift, and TypeScript.
    humanURL: https://swagger.io/tools/swagger-codegen/
    tags:
      - Code Generation
      - Open Source
      - OpenAPI
      - SDK
    properties:
      - type: Documentation
        url: https://swagger.io/docs/open-source-tools/swagger-codegen/
      - type: GitHub Repository
        url: https://github.com/swagger-api/swagger-codegen
      - type: Docker
        url: https://hub.docker.com/r/swaggerapi/swagger-codegen-cli-v3
      - type: Generator API
        url: https://generator3.swagger.io/
  - aid: swagger:swagger-parser
    name: Swagger Parser
    description: Swagger Parser (swagger-parser) is a JavaScript library for parsing, validating, and dereferencing OpenAPI 2.0 and 3.x specifications. Available as an npm package.
    humanURL: https://github.com/swagger-api/swagger-parser
    tags:
      - JavaScript
      - OpenAPI
      - Parser
      - Tooling
    properties:
      - type: GitHub Repository
        url: https://github.com/swagger-api/swagger-parser
      - type: npm
        url: https://www.npmjs.com/package/swagger-parser
  - aid: swagger:openapi-specification
    name: OpenAPI Specification
    description: The OpenAPI Specification (formerly Swagger Specification) is a language-agnostic standard for describing HTTP APIs. The current versions are OAS 3.1.1 (stable) and OAS 3.2.0 (latest). Governed by the OpenAPI Initiative (OAI) under the Linux Foundation.
    humanURL: https://swagger.io/specification/
    tags:
      - OpenAPI
      - REST
      - Standard
    properties:
      - type: Specification
        url: https://swagger.io/specification/
      - type: GitHub Repository
        url: https://github.com/OAI/OpenAPI-Specification
      - type: OpenAPI 3.2
        url: https://spec.openapis.org/oas/v3.2.0.html
      - type: OpenAPI 3.1
        url: https://spec.openapis.org/oas/v3.1.0.html
      - type: OpenAPI 2.0
        url: https://swagger.io/specification/v2/
common:
  - type: Website
    url: https://swagger.io
  - type: Documentation
    url: https://swagger.io/docs/
  - type: GitHub Organization
    url: https://github.com/swagger-api
  - type: Blog
    url: https://swagger.io/blog/
  - type: Tools
    url: https://swagger.io/tools/
  - type: OpenAPI Specification
    url: https://swagger.io/specification/
  - type: OpenAPI Initiative
    url: https://www.openapis.org/
  - type: Community
    url: https://community.smartbear.com/
  - type: Twitter
    url: https://twitter.com/SwaggerApi
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
