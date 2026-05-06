---
aid: apimatic
name: APIMatic
description: APIMatic is a developer experience platform for APIs that specializes in automated SDK generation, API documentation portal creation, specification validation and linting, and API format transformation. It supports 15+ API specification formats and generates idiomatic SDKs in 7+ programming languages with CI/CD integration for automating the developer experience suite.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Transformation
  - Code Generation
  - Developer Experience
  - Documentation
  - SDK Generation
url: https://raw.githubusercontent.com/api-evangelist/apimatic/refs/heads/main/apis.yml
created: '2025-01-08'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: apimatic:apimatic-platform-api
    name: APIMatic Platform API
    description: The APIMatic Platform API provides programmatic access to APIMatic's capabilities including SDK generation, API documentation portal generation, API specification validation and linting, and API specification transformation. Integrate APIMatic into your CI/CD workflows to automate your developer experience suite.
    humanURL: https://docs.apimatic.io/platform-api/
    baseURL: https://api.apimatic.io
    tags:
      - Code Generation
      - Documentation
      - SDK Generation
      - Transformation
      - Validation
    properties:
      - type: Documentation
        url: https://docs.apimatic.io/platform-api/
      - type: GettingStarted
        url: https://docs.apimatic.io/platform-api/#/http/getting-started
      - type: OpenAPI
        url: openapi/apimatic-platform-api.yaml
      - type: JSONSchema
        url: json-schema/apimatic-api-entity-schema.json
      - type: JSONSchema
        url: json-schema/apimatic-sdk-generation-schema.json
      - type: JSON-LD
        url: json-ld/apimatic-context.jsonld
  - aid: apimatic:apimatic-api-transformer-api
    name: APIMatic API Transformer API
    description: APIMatic API Transformer converts API definition files between more than 15 supported API specification formats including OpenAPI, RAML, API Blueprint, WSDL, WADL, and Postman Collections.
    humanURL: https://www.apimatic.io/solution/transformer
    baseURL: https://api.apimatic.io
    tags:
      - API Conversion
      - Format Transformation
      - OpenAPI
      - Postman
      - RAML
    properties:
      - type: Documentation
        url: https://docs.apimatic.io/api-transformer/overview-transformer/
common:
  - type: Website
    url: https://www.apimatic.io/
  - type: Documentation
    url: https://docs.apimatic.io/
  - type: GettingStarted
    url: https://docs.apimatic.io/getting-started/importing-api-spec/
  - type: Pricing
    url: https://www.apimatic.io/pricing
  - type: Blog
    url: https://www.apimatic.io/blog
  - type: SignUp
    url: https://app.apimatic.io/account/register
  - type: Login
    url: https://app.apimatic.io/account/login
  - type: ChangeLog
    url: https://docs.apimatic.io/changelog/
  - type: Support
    url: https://support.apimatic.io/hc/en-us
  - type: GitHubOrganization
    url: https://github.com/apimatic
  - type: LinkedIn
    url: https://www.linkedin.com/company/apimatic-limited/
  - type: X
    url: https://x.com/APIMatic
  - type: CLI
    url: https://www.npmjs.com/package/@apimatic/cli
  - type: TermsOfService
    url: https://www.apimatic.io/terms
  - type: PrivacyPolicy
    url: https://www.apimatic.io/privacy
  - type: Features
    data:
      - name: Idiomatic SDK Generation
        description: Generate production-ready SDKs in Python, Java, C# .NET, TypeScript, PHP, Ruby, and Go from any API specification.
      - name: API Documentation Portals
        description: Generate interactive developer documentation portals with code samples, guided walkthroughs, and code playground.
      - name: API Specification Validation
        description: Validate and lint API specifications with detailed error reports and best practice recommendations.
      - name: API Format Transformation
        description: Convert API definitions between 15+ formats including OpenAPI 3.0, Swagger 2.0, RAML, API Blueprint, and Postman Collections.
      - name: MCP Server Generation
        description: Generate Model Context Protocol (MCP) servers from API specifications for AI agent integration.
      - name: DX as Code
        description: Define and automate your entire developer experience pipeline as code with CI/CD integration.
      - name: OpenAPI Linter GitHub App
        description: Automatically validate OpenAPI specifications in GitHub pull requests via the APIMatic linter GitHub App.
  - type: UseCases
    data:
      - name: Automated SDK Publishing
        description: Automatically generate and publish SDKs to npm, PyPI, Maven, and other package registries on every API change.
      - name: Developer Portal Generation
        description: Generate and host comprehensive API documentation portals with interactive examples and code playground.
      - name: API Specification Migration
        description: Transform legacy Swagger 2.0 or RAML specs to OpenAPI 3.0 for modern tooling compatibility.
      - name: CI/CD API Governance
        description: Integrate API validation and linting into CI/CD pipelines to enforce quality gates on API changes.
  - type: Integrations
    data:
      - name: MuleSoft
        description: APIMatic integration for generating SDKs from MuleSoft API definitions.
      - name: Redocly
        description: Integration for enhanced API documentation workflows.
      - name: GitHub Actions
        description: CI/CD integration for automated SDK generation and API validation in GitHub workflows.
  - type: Solutions
    data:
      - name: Free Plan
        description: Basic SDK generation and API validation for individual developers.
      - name: Team Plan
        description: Advanced SDK generation, portal publishing, and team collaboration features.
      - name: Enterprise Plan
        description: Full developer experience automation, custom branding, SLA, and dedicated support.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
