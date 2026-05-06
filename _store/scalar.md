---
aid: scalar
name: Scalar
description: Scalar is an open-source API platform built around the OpenAPI standard. It provides API documentation (API References), an offline-first API client, a centralized API registry for managing OpenAPI documents, JSON schemas and Spectral rules, and automated SDK generation for TypeScript, Python, Go, PHP, Java, and Ruby. Used by teams at SmartBear, Microsoft ASP.NET, and 30+ framework ecosystems including Express, FastAPI, NestJS, and Spring Boot. The platform has 14.9k GitHub stars and is MIT licensed. Scalar is backed by a strong open-source community and positions itself as the modern, open alternative to Swagger UI and Postman.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/scalar/refs/heads/main/apis.yml
tags:
  - API Client
  - API Documentation
  - API References
  - Code Generation
  - Developer Tools
  - OpenAPI
  - Registry
  - SDKs
  - Swagger
type: Index
access: 3rd-Party
position: Consumer
created: '2025-01-08'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: scalar:scalar-api-references
    name: Scalar API References
    description: Scalar API References renders modern, interactive API documentation from OpenAPI and Swagger specifications. Features include multiple themes, custom styling, dark mode, mobile responsiveness, built-in search, and an interactive request panel for testing APIs directly in the docs. Supports OpenAPI 3.0 and 3.1, $ref resolution, allOf/oneOf/anyOf, and authentication schemes. Framework integrations include React, Vue, FastAPI, ASP.NET Core, Spring Boot, NestJS, Express, and 30+ others.
    tags:
      - Documentation
      - Interactive
      - OpenAPI
      - References
      - Swagger
    humanURL: https://scalar.com/products/api-references/getting-started
    properties:
      - type: GettingStarted
        url: https://scalar.com/products/api-references/getting-started
      - type: Documentation
        url: https://guides.scalar.com/scalar/scalar-api-references/getting-started
      - type: GitHub
        url: https://github.com/scalar/scalar
      - type: NPM
        url: https://www.npmjs.com/package/@scalar/api-reference
  - aid: scalar:scalar-api-client
    name: Scalar API Client
    description: Scalar API Client is a fully open-source, offline-first REST API client built on the OpenAPI standard. Supports collections, environments, pre/post-response scripting, test results, and collection runners. Available for Windows, macOS, and Linux as a desktop application and as a browser-based version at client.scalar.com. Imports OpenAPI files to auto-generate request collections with authentication pre-configured.
    tags:
      - API Client
      - Collections
      - OpenAPI
      - REST
      - Testing
    humanURL: https://scalar.com/products/api-client/getting-started
    properties:
      - type: GettingStarted
        url: https://scalar.com/products/api-client/getting-started
      - type: Application
        url: https://client.scalar.com/
      - type: Download
        url: https://scalar.com/download
      - type: GitHub
        url: https://github.com/scalar/scalar
  - aid: scalar:scalar-docs
    name: Scalar Docs
    description: Scalar Docs enables teams to create and publish developer documentation that stays in sync with their API and code. Supports writing with a WYSIWYG editor, pulling Markdown and MDX files from repositories, and generating API references from OpenAPI documents with Git Sync and CI/CD integration. Custom domains, team collaboration, and versioning are available on paid plans.
    tags:
      - Developer Portal
      - Documentation
      - Git Sync
      - Markdown
      - MDX
    humanURL: https://scalar.com/products/docs/getting-started
    properties:
      - type: GettingStarted
        url: https://scalar.com/products/docs/getting-started
      - type: Portal
        url: https://docs.scalar.com/
      - type: Documentation
        url: https://guides.scalar.com/scalar/scalar-docs/getting-started
      - type: GitHubActions
        url: https://scalar.com/products/docs/github-actions
  - aid: scalar:scalar-registry
    name: Scalar Registry
    description: 'Scalar Registry provides centralized management and versioning of OpenAPI Documents, JSON Schemas, and Spectral Rules with deep Git integration. Serves as the single source of truth for API definitions across teams. Supports both private and public registries with CI/CD workflows via CLI and GitHub Actions. Publish via the scalar CLI: `scalar registry publish`.'
    tags:
      - Git Integration
      - Governance
      - JSON Schema
      - OpenAPI
      - Registry
      - Spectral
      - Versioning
    humanURL: https://scalar.com/products/registry/getting-started
    properties:
      - type: GettingStarted
        url: https://scalar.com/products/registry/getting-started
      - type: Documentation
        url: https://guides.scalar.com/scalar/scalar-registry/getting-started
      - type: CLI
        url: https://guides.scalar.com/scalar/scalar-cli/getting-started
      - type: GitHubActions
        url: https://scalar.com/scalar/scalar-registry/github-actions
  - aid: scalar:scalar-sdks
    name: Scalar SDKs
    description: Scalar SDKs generates type-safe client libraries from OpenAPI specifications. Supported languages include TypeScript, Python, Golang, PHP, Java, and Ruby. Features include automated GitHub workflows, code samples, full OpenAPI auth support, file streaming, and webhook support. SDK generation is $100 per month per language on paid plans.
    tags:
      - Code Generation
      - Go
      - Java
      - PHP
      - Python
      - Ruby
      - SDKs
      - TypeScript
    humanURL: https://scalar.com/products/sdks/getting-started
    properties:
      - type: GettingStarted
        url: https://scalar.com/products/sdks/getting-started
      - type: Documentation
        url: https://guides.scalar.com/scalar/scalar-sdks/getting-started
      - type: Pricing
        url: https://guides.scalar.com/scalar/pricing
  - aid: scalar:scalar-cli
    name: Scalar CLI
    description: The Scalar CLI is a command-line interface for managing OpenAPI files, generating documentation, running mock servers, validating specs, and publishing to the Scalar Registry. Enables CI/CD integration and automation of the API documentation workflow.
    tags:
      - CLI
      - Developer Tools
      - Mock Server
      - OpenAPI
      - Validation
    humanURL: https://guides.scalar.com/scalar/scalar-cli/getting-started
    properties:
      - type: GettingStarted
        url: https://guides.scalar.com/scalar/scalar-cli/getting-started
      - type: Documentation
        url: https://guides.scalar.com/scalar/scalar-cli/getting-started
      - type: NPM
        url: https://www.npmjs.com/package/@scalar/cli
common:
  - type: Website
    url: https://scalar.com/
    name: Scalar Website
  - type: Documentation
    url: https://guides.scalar.com/scalar/introduction
    name: Scalar Documentation
  - type: Pricing
    url: https://guides.scalar.com/scalar/pricing
    name: Scalar Pricing
  - type: GitHub
    url: https://github.com/scalar/scalar
    name: Scalar GitHub Repository
  - type: Discord
    url: https://discord.gg/scalar
    name: Scalar Discord Community
  - type: Blog
    url: https://scalar.com/blog
    name: Scalar Blog
  - type: ChangeLog
    url: https://github.com/scalar/scalar/releases
    name: Scalar Changelog
  - type: Support
    url: mailto:support@scalar.com
    name: Scalar Support
  - type: Dashboard
    url: https://dashboard.scalar.com/
    name: Scalar Dashboard
  - type: SpectralRules
    url: https://github.com/api-evangelist/scalar/blob/main/rules/scalar-rules.yml
    name: Scalar Spectral Rules
  - type: JSONSchema
    url: https://github.com/api-evangelist/scalar/blob/main/json-schema/scalar-openapi-document-schema.json
    name: Scalar OpenAPI Document JSON Schema
  - type: JSONStructure
    url: https://github.com/api-evangelist/scalar/blob/main/json-structure/scalar-openapi-document-structure.json
    name: Scalar OpenAPI Document JSON Structure
  - type: JSONLDContext
    url: https://github.com/api-evangelist/scalar/blob/main/json-ld/scalar-context.jsonld
    name: Scalar JSON-LD Context
  - type: Vocabulary
    url: https://github.com/api-evangelist/scalar/blob/main/vocabulary/scalar-vocabulary.yml
    name: Scalar Vocabulary
  - type: Examples
    url: https://github.com/api-evangelist/scalar/blob/main/examples/
    name: Scalar Usage Examples
segments:
  - SDKs
  - Clients
  - Documentation
  - Registries
  - Developer Tools
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---
