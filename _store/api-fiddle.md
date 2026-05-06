---
aid: api-fiddle
name: API-Fiddle
description: API-Fiddle is an interactive, collaborative API design platform for creating professional APIs based on OpenAPI. It provides first-class support for OpenAPI 3.x, data transfer objects, API versioning, suggested response codes, parameter serialization, pagination patterns, and response structuring best practices. API-Fiddle enables seamless sharing of API definitions with teams without requiring user accounts, making it accessible for collaboration throughout the API design lifecycle.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Design
  - OpenAPI
  - Collaboration
  - Documentation
  - Platform
url: https://raw.githubusercontent.com/api-evangelist/api-fiddle/refs/heads/main/apis.yml
created: '2025-01-08'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: api-fiddle:api-fiddle
    name: API-Fiddle
    description: The API Fiddle API provides programmatic access to the API Fiddle design platform, enabling management of projects, specifications, workspaces, sharing, and export capabilities. It allows developers to automate API design workflows, collaborate on OpenAPI specifications, and integrate API Fiddle into their development pipelines.
    humanURL: https://api-fiddle.com/
    tags:
      - API Design
      - OpenAPI
      - Collaboration
    properties:
      - type: Documentation
        url: https://api-fiddle.com/
      - type: OpenAPI
        url: openapi/api-fiddle-api-fiddle-openapi.yml
      - type: JSONSchema
        url: json-schema/api-fiddle-project-schema.json
      - type: JSONSchema
        url: json-schema/api-fiddle-specification-schema.json
      - type: JSONSchema
        url: json-schema/api-fiddle-workspace-schema.json
      - type: JSONLD
        url: json-ld/api-fiddle-context.jsonld
common:
  - type: Website
    url: https://api-fiddle.com/
  - type: Blog
    url: https://blog.api-fiddle.com/
  - type: GitHubRepository
    url: https://github.com/apps/api-fiddle
  - type: Features
    data:
      - name: OpenAPI-First Design
        description: Design professional REST APIs directly in the OpenAPI specification format with first-class support for OpenAPI 3.x standards.
      - name: Collaborative Playground
        description: Share API definitions with teams without requiring user accounts, enabling frictionless collaboration across the API design process.
      - name: Data Transfer Object Support
        description: First-class support for data transfer objects, enabling well-structured API schemas and reusable component definitions.
      - name: API Versioning
        description: Built-in guidance and support for API versioning strategies to help teams manage API evolution over time.
      - name: Best Practice Guidance
        description: Provides extensive guidance on parameter serialization, pagination patterns, response structuring, and suggested response codes.
      - name: Automation-Optimized
        description: Specifications are optimized for automation and code generation, enabling integration into CI/CD pipelines and developer toolchains.
  - type: UseCases
    data:
      - name: API Design and Prototyping
        description: Design and prototype REST APIs using OpenAPI before implementation, enabling API-first development workflows.
      - name: Team Collaboration on API Specs
        description: Collaborate with distributed teams on OpenAPI specifications without requiring accounts, reducing friction in the review process.
      - name: API Documentation
        description: Generate and publish professional API documentation from OpenAPI specifications with integrated tooling.
  - type: Integrations
    data:
      - name: GitHub
        description: GitHub App integration for connecting API Fiddle projects to GitHub repositories for version control and CI/CD workflows.
      - name: OpenAPI Ecosystem
        description: Exports standard OpenAPI 3.x specifications compatible with the full OpenAPI tooling ecosystem including generators, validators, and documentation tools.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
