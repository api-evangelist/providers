---
aid: apiary
name: Apiary
description: Apiary is an API design and documentation platform, now part of Oracle Cloud Infrastructure. With 486,000+ users and 591,000+ APIs managed, it uses API Blueprint and Swagger/OpenAPI specifications to produce interactive API documentation, mock servers, automated testing, and collaborative API design workflows. Apiary enables teams to design APIs before writing code, generate documentation automatically, and validate implementations against specifications.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Blueprint
  - API Design
  - API Testing
  - Collaboration
  - Design First
  - Documentation
  - Mock Servers
  - Oracle
url: https://raw.githubusercontent.com/api-evangelist/apiary/refs/heads/main/apis.yml
created: '2026-03-25'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: apiary:apiary-api
    name: Apiary API
    description: The Apiary API provides programmatic access to manage API projects, documentation, and team collaboration. It allows creating and updating API Blueprint and Swagger/OpenAPI documents, managing team members, and integrating Apiary workflows into CI/CD pipelines.
    humanURL: https://apiary.io
    tags:
      - API Blueprint
      - API Design
      - Collaboration
      - Documentation
      - Mock Servers
    properties:
      - type: Documentation
        url: https://help.apiary.io
      - type: GettingStarted
        url: https://help.apiary.io/tools/apiary-cli/
  - aid: apiary:api-blueprint
    name: API Blueprint
    description: API Blueprint is a high-level API design language created by Apiary for designing and documenting web APIs. It uses a Markdown-based syntax that is human-readable and machine-parseable, enabling teams to design APIs collaboratively and generate documentation, mock servers, and tests from a single source of truth.
    humanURL: https://apiblueprint.org
    tags:
      - API Blueprint
      - API Design
      - Documentation
      - Open Source
      - Specification
    properties:
      - type: Documentation
        url: https://apiblueprint.org/documentation/
      - type: GitHubRepository
        url: https://github.com/apiaryio/api-blueprint
      - type: Specification
        url: https://apiblueprint.org/documentation/specification.html
common:
  - type: Website
    url: https://apiary.io
  - type: Documentation
    url: https://help.apiary.io
  - type: GitHubOrganization
    url: https://github.com/apiaryio
  - type: Blog
    url: https://blog.apiary.io
  - type: Pricing
    url: https://apiary.io/plans
  - type: Login
    url: https://login.apiary.io
  - type: SignUp
    url: https://login.apiary.io/register
  - type: Support
    url: https://help.apiary.io
  - type: PrivacyPolicy
    url: https://www.oracle.com/legal/privacy/
  - type: TermsOfService
    url: https://www.oracle.com/legal/terms.html
  - type: Features
    data:
      - name: API Blueprint Support
        description: Native support for API Blueprint, a high-level Markdown-based API description language for collaborative design.
      - name: OpenAPI/Swagger Support
        description: Import and work with Swagger and OpenAPI specifications alongside API Blueprint documents.
      - name: Interactive API Documentation
        description: Auto-generate interactive documentation from API specs with a built-in API console for live testing.
      - name: Mock Servers
        description: Instant mock servers generated from API specs allowing frontend development before backend is ready.
      - name: Automated API Testing
        description: Run automated tests against API implementations using Dredd, the open-source API testing framework.
      - name: Collaborative Workflows
        description: Team-based API design with version history, commenting, and shared workspaces.
      - name: CLI Integration
        description: Apiary CLI for integrating API design and testing workflows into CI/CD pipelines.
      - name: Open Source Tooling
        description: Maintains Dredd (testing), Gavel (validation), and API Blueprint as open-source projects.
  - type: UseCases
    data:
      - name: Design-First API Development
        description: Design APIs in API Blueprint or OpenAPI before writing code, enabling parallel frontend and backend development.
      - name: API Documentation Generation
        description: Automatically generate interactive API documentation from API specifications for developer consumption.
      - name: Mock Server Prototyping
        description: Generate instant mock servers from specs to enable frontend development without a live backend.
      - name: Contract Testing
        description: Validate API implementations against their specifications using Dredd to catch regressions.
      - name: Team API Governance
        description: Collaborate on API design standards and review API changes in a shared workspace.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
