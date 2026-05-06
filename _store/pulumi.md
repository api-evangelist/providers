---
aid: pulumi
name: Pulumi
description: Pulumi is a modern infrastructure as code platform that allows you to use familiar programming languages to build, deploy, and manage cloud infrastructure. The Pulumi Cloud REST API enables programmatic access to manage organizations, stacks, deployments, environments, policy packs, webhooks, and other Pulumi Cloud resources.
type: Index
position: Consumer
access: 3rd-Party
image: https://www.pulumi.com/logos/brand/logo-on-white.png
tags:
  - Automation
  - Cloud
  - DevOps
  - Infrastructure as Code
  - Multi-Cloud
  - Stacks
  - Deployments
  - Policy
created: '2025-01-08'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/pulumi/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: pulumi:pulumi-cloud
    name: Pulumi Cloud REST API
    description: 'The Pulumi Cloud REST API exposes 446+ endpoints across 28 categories, including access tokens, AI/agents, audit logs, change gates and requests, deployments, environments (ESC), insights, OIDC issuers, organizations, policy groups and packs, registry, resource search, stacks, and webhooks. Authentication is via the `Authorization: token {token}` header.'
    humanURL: https://www.pulumi.com/docs/pulumi-cloud/cloud-rest-api/
    baseURL: https://api.pulumi.com
    tags:
      - Cloud
      - DevOps
      - Infrastructure as Code
      - Stacks
      - Deployments
    properties:
      - type: Documentation
        url: https://www.pulumi.com/docs/pulumi-cloud/cloud-rest-api/
      - type: OpenAPI
        url: https://api.pulumi.com/api/openapi/pulumi-spec.json
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/pulumi/refs/heads/main/openapi/pulumi-openapi.json
      - type: Authentication
        url: https://www.pulumi.com/docs/pulumi-cloud/access-management/access-tokens/
  - aid: pulumi:automation-api
    name: Pulumi Automation API
    description: The Automation API enables you to build custom cloud interfaces for your technical end users. Build self-service developer portals, CLIs, frameworks, and more, programmatically driving Pulumi from Go, Node.js, Python, .NET, and Java.
    humanURL: https://www.pulumi.com/automation/
    tags:
      - Automation
      - SDK
    properties:
      - type: Documentation
        url: https://www.pulumi.com/automation/
      - type: GitHub
        url: https://github.com/pulumi/pulumi
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
common:
  - url: https://www.pulumi.com
    type: Website
  - url: https://www.pulumi.com/docs/
    type: Documentation
  - url: https://www.pulumi.com/blog/
    type: Blog
  - url: https://github.com/pulumi
    type: GitHub Organization
  - url: https://app.pulumi.com/signup
    type: Sign Up
  - url: https://app.pulumi.com/signin
    type: Login
  - url: https://www.pulumi.com/pricing/
    type: Pricing
  - url: https://status.pulumi.com/
    type: Status
  - url: https://www.pulumi.com/terms/
    type: Terms of Service
  - url: https://www.pulumi.com/privacy/
    type: Privacy Policy
  - url: https://app.pulumi.com/account/tokens
    type: Authentication
---
