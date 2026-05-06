---
aid: cycloid
name: Cycloid
x-type: company
description: Cycloid is a unified Internal Developer Portal & Platform combining self-service Service Catalogs (Stacks and StackForms), Infrastructure as Code orchestration, multi-cloud asset inventory (Asset Inventory and InfraView), CI/CD pipeline centralization, FinOps and GreenOps cost / carbon dashboards, RBAC governance, and an MCP server for natural-language interaction. Cycloid exposes a public HTTP REST API at http-api.cycloid.io for programmatic management of organizations, projects, environments, stacks, pipelines, credentials, config repositories, and cloud cost dashboards. Authentication is via API key or OAuth2 with token refresh; the canonical Swagger / Redoc reference is published at docs.cycloid.io.
url: https://raw.githubusercontent.com/api-evangelist/cycloid/refs/heads/main/apis.yml
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
type: Index
access: 3rd-Party
position: Consumer
created: '2026-03-27'
modified: '2026-04-28'
specificationVersion: '0.20'
tags:
  - Asset Inventory
  - CI/CD
  - Cloud Cost Management
  - Cloud Management
  - Developer Experience
  - DevOps
  - FinOps
  - GitOps
  - GreenOps
  - Infrastructure as Code
  - Internal Developer Platform
  - Internal Developer Portal
  - Multi-Cloud
  - Platform Engineering
  - RBAC
  - Self-Service
  - Service Catalog
  - StackForms
  - Terraform
apis:
  - aid: cycloid:http-api
    name: Cycloid HTTP API
    description: The Cycloid HTTP API is the programmatic surface of the Cycloid Internal Developer Portal & Platform. It manages organizations, members, teams, projects, environments, stacks (Service Catalog), pipelines, infrastructure resources, credentials, config repositories, cloud cost dashboards, and inventory. Authentication uses an API key or OAuth2 with token refresh.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://docs.cycloid.io/
    baseURL: https://http-api.cycloid.io
    tags:
      - API Key
      - Cloud Cost
      - Credentials
      - Inventory
      - OAuth2
      - Organizations
      - Pipelines
      - Projects
      - Service Catalog
      - Stacks
    properties:
      - type: Documentation
        url: https://docs.cycloid.io/
      - type: GettingStarted
        url: https://docs.cycloid.io/getting-started
      - type: OpenAPI
        url: openapi/cycloid-api-openapi.yml
      - type: Capabilities
        url: capabilities/cycloid-api-capabilities.yml
      - type: Rules
        url: rules/cycloid-api-rules.yml
common:
  - type: Website
    url: https://www.cycloid.io
  - type: Documentation
    url: https://docs.cycloid.io
  - type: Pricing
    url: https://www.cycloid.io/pricing
  - type: GitHubOrganization
    url: https://github.com/cycloidio
  - type: Blog
    url: https://www.cycloid.io/blog
  - type: Status
    url: https://status.cycloid.io
  - type: Login
    url: https://console.cycloid.io
  - type: TermsOfService
    url: https://www.cycloid.io/legal/terms-and-conditions
  - type: PrivacyPolicy
    url: https://www.cycloid.io/legal/privacy-policy
  - type: Contact
    url: https://www.cycloid.io/contact
  - type: JSON-LD
    url: json-ld/cycloid-context.jsonld
  - type: JSONSchema
    url: json-schema/cycloid-organization-schema.json
  - type: JSONSchema
    url: json-schema/cycloid-stack-schema.json
  - type: Vocabulary
    url: vocabulary/cycloid-vocabulary.yml
  - type: Capabilities
    url: capabilities/cycloid-api-capabilities.yml
  - type: Rules
    url: rules/cycloid-api-rules.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
