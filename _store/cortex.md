---
aid: cortex
name: Cortex
x-type: company
description: Cortex is an Engineering Operations (EngOps) platform and internal developer portal that helps engineering teams catalog services, enforce production readiness with scorecards, automate self-service workflows, and surface engineering intelligence across their organization. Cortex centralizes data from observability, CI/CD, source control, on-call, and SaaS tooling and exposes it through a REST API used to integrate the catalog with platform engineering and SRE workflows.
url: https://raw.githubusercontent.com/api-evangelist/cortex/refs/heads/main/apis.yml
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
type: Index
access: Public
position: Provider
tags:
  - Catalog
  - Custom Data
  - Dependencies
  - Deploys
  - Developer Experience
  - EngOps
  - Engineering Intelligence
  - Initiatives
  - Internal Developer Portal
  - On-call
  - Platform Engineering
  - Scorecards
  - Service Catalog
  - SRE
  - Workflows
created: '2026-03-16'
modified: '2026-04-28'
specificationVersion: '0.20'
apis:
  - aid: cortex:cortex-rest-api
    name: Cortex REST API
    description: The Cortex REST API exposes the service catalog, scorecards, initiatives, entity relationships and dependencies, on-call assignments, custom data, and deployments managed in a Cortex workspace. Authentication is via personal or service access tokens, and entity descriptors can be retrieved as OpenAPI documents through a per-entity endpoint.
    humanURL: https://docs.cortex.io/
    properties:
      - type: Documentation
        url: https://docs.cortex.io/
      - type: GettingStarted
        url: https://docs.cortex.io/docs/getting-started
      - type: APIReference
        url: https://docs.cortex.io/reference
    tags:
      - Catalog
      - Dependencies
      - Deploys
      - REST
      - Scorecards
  - aid: cortex:cortex-mcp
    name: Cortex MCP Server
    description: Cortex exposes a Model Context Protocol (MCP) server that lets AI coding assistants and IDE agents query the service catalog, look up ownership, check scorecard scores, and run workflows directly from developer tools.
    humanURL: https://docs.cortex.io/
    properties:
      - type: Documentation
        url: https://docs.cortex.io/
    tags:
      - AI
      - IDE
      - MCP
common:
  - type: Website
    url: https://www.cortex.io/
  - type: Documentation
    url: https://docs.cortex.io/
  - type: Product
    url: https://www.cortex.io/product
  - type: ServiceCatalog
    url: https://www.cortex.io/product/service-catalog
  - type: Scorecards
    url: https://www.cortex.io/product/scorecards
  - type: Workflows
    url: https://www.cortex.io/product/workflows
  - type: Pricing
    url: https://www.cortex.io/pricing
  - type: Customers
    url: https://www.cortex.io/customers
  - type: Blog
    url: https://www.cortex.io/blog
  - type: GitHubOrganization
    url: https://github.com/cortexapps
  - type: Integrations
    url: https://docs.cortex.io/docs/integrations
  - type: ChangeLog
    url: https://docs.cortex.io/changelog
  - type: Status
    url: https://status.cortex.io/
  - type: LinkedIn
    url: https://www.linkedin.com/company/cortexapp/
  - type: Twitter
    url: https://twitter.com/cortexapp
  - type: Contact
    url: https://www.cortex.io/contact
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
