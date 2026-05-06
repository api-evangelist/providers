---
aid: apigit
url: https://raw.githubusercontent.com/api-evangelist/apigit/refs/heads/main/apis.yml
name: APIGit
description: APIGit is a Git-native platform for full lifecycle API development that combines version control, API design, documentation generation, governance, testing, and dynamic mock servers in a single integrated environment. Teams can build, publish, share, and secure APIs through Git-based workflows.
tags:
  - API Design
  - API Lifecycle
  - Documentation
  - Git
  - Governance
  - Mocking
  - Platform
  - Testing
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-01-08'
modified: '2026-04-19'
position: Consumer
specificationVersion: '0.19'
apis:
  - aid: apigit:apigit
    name: APIGit
    tags:
      - API Design
      - API Lifecycle
      - Git
      - Mocking
    humanURL: https://apigit.com/
    baseURL: https://api.apigit.com/v1
    properties:
      - url: https://apigit.com/
        type: Documentation
      - url: https://apigit.com/pricing
        type: Pricing
      - url: openapi/apigit-api.yaml
        type: OpenAPI
      - url: json-schema/apigit-repository-schema.json
        type: JSONSchema
      - url: json-schema/apigit-mock-server-schema.json
        type: JSONSchema
      - url: json-ld/apigit-context.jsonld
        type: JSON-LD
    description: APIGit is a Git-native API lifecycle platform providing native Git repositories, visual API design, documentation generation, governance policies, automated testing, and dynamic mock servers for API development.
common:
  - url: https://apigit.com/
    type: Website
  - url: https://apigit.com/doc
    type: Documentation
  - url: https://apigit.com/pricing
    type: Pricing
  - url: https://apigit.com/blog
    type: Blog
  - url: https://github.com/apigitlabs
    type: GitHubOrganization
  - url: https://www.youtube.com/@apigit
    type: YouTube
  - type: Features
    data:
      - name: Native Git Repository
        description: Version-controlled API repositories with Git-native workflows for teams.
      - name: API Design
        description: Visual OpenAPI designer for designing APIs without writing YAML manually.
      - name: API Documentation
        description: Automatic documentation generation and publishing with custom domains.
      - name: API Governance
        description: Policy management and compliance controls for API standards enforcement.
      - name: API Testing
        description: Built-in automated API testing with test case management.
      - name: Dynamic Mock Server
        description: Zero-configuration dynamic mock servers generated from API definitions.
  - type: UseCases
    data:
      - name: Design-First API Development
        description: Design APIs visually before implementation using Git-tracked OpenAPI definitions.
      - name: Parallel Frontend-Backend Development
        description: Enable frontend teams to develop against mock servers while backends are being built.
      - name: Team API Governance
        description: Enforce API standards and policies across teams with built-in governance tools.
  - type: Integrations
    data:
      - name: OpenAPI
        description: Native OpenAPI specification support for API design and documentation.
      - name: Git
        description: Native Git version control for all API definitions and changes.
  - type: Solutions
    data:
      - name: Free Plan
        description: 1 API repository, mock server, and document publication with up to 1,000 mock calls/month.
      - name: Team Plan
        description: $8/user/month with 5 seats, 5 organizations, and 2,000 mock calls/month/seat.
      - name: Enterprise Plan
        description: $18/user/month with 20 organizations, custom domains, SSO, webhooks, and 4,000 mock calls/month/seat.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
