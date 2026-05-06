---
aid: apidog
url: https://raw.githubusercontent.com/api-evangelist/apidog/refs/heads/main/apis.yml
name: Apidog
description: Apidog is a complete set of tools that connects the entire API lifecycle, helping R&D teams implement best practices for API Design-first development. It provides API design, debugging, testing, mocking, and documentation capabilities in a single collaborative platform with multi-protocol support including HTTP, GraphQL, gRPC, WebSocket, and SOAP.
tags:
  - API Design
  - API Lifecycle
  - API Testing
  - Collaboration
  - Design-First
  - Documentation
  - Mocking
  - Platform
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-01-08'
modified: '2026-04-19'
position: Consumer
specificationVersion: '0.19'
apis:
  - aid: apidog:apidog
    name: Apidog
    description: Apidog's public REST API allows developers to programmatically interact with Apidog projects for importing and exporting API specifications, managing endpoints, schemas, environments, and more. All API URLs begin with the base URL https://api.apidog.com. Authentication is via Bearer Token passed in the Authorization header.
    humanURL: https://apidog.com/
    baseURL: https://api.apidog.com
    tags:
      - API Design
      - API Lifecycle
      - Documentation
      - Import
      - Export
    properties:
      - url: https://openapi.apidog.io/
        type: Documentation
      - url: https://docs.apidog.com/overview-644404m0
        type: GettingStarted
      - url: openapi/apidog-apidog-openapi.yml
        type: OpenAPI
      - url: https://legal.apidog.com/
        type: TermsOfService
      - url: https://apidog.com/pricing/
        type: Pricing
      - url: json-schema/apidog-project-schema.json
        type: JSONSchema
      - url: json-schema/apidog-import-result-schema.json
        type: JSONSchema
      - url: json-schema/apidog-export-result-schema.json
        type: JSONSchema
      - url: json-schema/apidog-error-schema.json
        type: JSONSchema
      - url: json-ld/apidog-context.jsonld
        type: JSON-LD
common:
  - url: https://apidog.com/
    type: Website
  - url: https://docs.apidog.com/
    type: Documentation
  - url: https://docs.apidog.com/overview-644404m0
    type: GettingStarted
  - url: https://apidog.com/pricing/
    type: Pricing
  - url: https://apidog.com/blog/
    type: Blog
  - url: https://apidog.com/blog/product-updates/
    type: ReleaseNotes
  - url: https://apidog.com/articles/
    type: Articles
  - url: https://legal.apidog.com/
    type: TermsOfService
  - url: https://trust.apidog.com/
    type: Security
  - url: https://docs.apidog.com/apidog-support-center-748035m0
    type: Support
  - url: https://github.com/Apidog
    type: GitHubOrganization
  - type: Features
    data:
      - name: API Design
        description: Visual OpenAPI/Swagger editor with JSON Schema support, reusable schemas, Git integration, and sprint branches for collaborative development.
      - name: API Debugging
        description: Multi-protocol support for HTTP, REST, GraphQL, SOAP, WebSocket with auto-validation of responses against API specs and database connectivity.
      - name: API Testing
        description: Visual test scenarios with CI/CD integration, data-driven testing with CSV/JSON datasets, performance testing, and AI-generated test cases.
      - name: API Mocking
        description: Zero-configuration smart mock generation from specs, cloud-based and local mock servers, and custom mock rules.
      - name: API Documentation
        description: Auto-generated interactive docs with custom domains, auto-generated SSL certificates, Markdown support, and versioning control.
      - name: Team Collaboration
        description: Real-time synchronization, sprint branches for parallel development, role-based access control, and SSO support.
      - name: Enterprise Security
        description: SOC 2 Type II certified, GDPR and ISO 27001 compliant, TLS 1.3+ encryption in transit, AES-256 encryption at rest.
  - type: UseCases
    data:
      - name: API Design-First Development
        description: Design APIs visually before writing code, enabling frontend and backend teams to work in parallel.
      - name: Automated API Testing
        description: Build comprehensive regression test suites with CI/CD integration for automated API quality assurance.
      - name: API Documentation Publishing
        description: Automatically generate and publish interactive developer documentation from API specifications.
      - name: Mock Server Development
        description: Enable frontend development independent of backend completion using intelligent mock data generation.
  - type: Integrations
    data:
      - name: OpenAPI/Swagger
        description: Import and export OpenAPI/Swagger specifications for interoperability with other API tools.
      - name: Postman
        description: 100% compatible Postman collection import and scripting syntax support.
      - name: CI/CD Platforms
        description: Integration with Jenkins, GitLab CI, GitHub Actions, and Bitbucket Pipelines for automated testing.
      - name: Databases
        description: Connect to MySQL, PostgreSQL, Oracle, SQLServer, and ClickHouse for dynamic test data.
      - name: Credential Vaults
        description: Integration with HashiCorp Vault, Azure Key Vault, and AWS Secrets Manager for secure credential management.
      - name: Enterprise SSO
        description: Support for SAML 2.0, Microsoft Active Directory, OIDC, and SCIM for enterprise identity management.
      - name: IntelliJ IDEA Plugin
        description: IDEA plugin for JavaDoc annotation parsing and API definition generation.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
