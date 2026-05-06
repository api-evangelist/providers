---
aid: scalr
name: Scalr
description: Scalr is an enterprise-grade, drop-in replacement for Terraform Cloud and a remote Terraform operations backend that provides cost estimation, policy enforcement, and collaborative infrastructure management. Scalr features a hierarchical account-environment-workspace model, full compatibility with the TFC API and Terraform/OpenTofu CLI, OIDC authentication, GitOps workflows, OPA policy enforcement, and a comprehensive REST API for managing infrastructure as code operations at scale.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - FinOps
  - GitOps
  - Infrastructure as Code
  - Kubernetes
  - OPA
  - OpenTofu
  - Policy
  - Terraform
url: https://raw.githubusercontent.com/api-evangelist/scalr/refs/heads/main/apis.yml
created: '2026-05-02'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: scalr:scalr-user-api
    name: Scalr User API
    description: The Scalr User API provides programmatic access to user-level resources including farms, farm roles, servers, events, cloud locations, cost centers, and scaling metrics. This is the legacy cloud management API (v1beta0) for managing cloud infrastructure resources across multiple cloud providers.
    humanURL: https://api-explorer.scalr.com/
    tags:
      - Cloud Management
      - Farms
      - Infrastructure
      - Scalr
      - Servers
    properties:
      - type: Documentation
        url: https://api-explorer.scalr.com/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/scalr/refs/heads/main/openapi/scalr-user-openapi.yml
  - aid: scalr:scalr-account-api
    name: Scalr Account API
    description: The Scalr Account API provides programmatic access to account-level resources including environments, roles, images, orchestration rules, and account-wide configuration. This is the legacy cloud management API (v1beta0).
    humanURL: https://api-explorer.scalr.com/
    tags:
      - Account Management
      - Cloud Management
      - Environments
      - Roles
      - Scalr
    properties:
      - type: Documentation
        url: https://api-explorer.scalr.com/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/scalr/refs/heads/main/openapi/scalr-account-openapi.yml
  - aid: scalr:scalr-global-api
    name: Scalr Global API
    description: The Scalr Global API provides programmatic access to global-level resources including images and roles that span the entire Scalr installation.
    humanURL: https://api-explorer.scalr.com/
    tags:
      - Cloud Management
      - Global
      - Images
      - Roles
      - Scalr
    properties:
      - type: Documentation
        url: https://api-explorer.scalr.com/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/scalr/refs/heads/main/openapi/scalr-global-openapi.yml
  - aid: scalr:scalr-iac-api
    name: Scalr IaC Management API
    description: The Scalr IaC Management API (TFC-compatible) provides programmatic control over workspaces, environments, runs, state, variables, policies, and provider configurations. Fully compatible with Terraform Cloud API and Terraform/OpenTofu CLI. Authenticates using Bearer tokens (personal or service account). Supports OIDC for GitHub, GitLab, AWS, Azure, and other identity providers.
    humanURL: https://docs.scalr.io/reference/overview-1
    tags:
      - Infrastructure as Code
      - OpenTofu
      - Policy
      - Runs
      - Scalr
      - Terraform
      - Workspaces
    properties:
      - type: Documentation
        url: https://docs.scalr.io/reference/overview-1
      - type: Getting Started
        url: https://docs.scalr.io/docs/introduction
      - type: Authentication
        url: https://docs.scalr.io/reference/api-tokens
common:
  - type: Website
    url: https://scalr.com/
  - type: Documentation
    url: https://docs.scalr.io/
  - type: API Reference
    url: https://docs.scalr.io/reference/overview-1
  - type: API Explorer
    url: https://api-explorer.scalr.com/
  - type: GitHub
    url: https://github.com/scalr
  - type: Blog
    url: https://scalr.com/blog/
  - type: Changelog
    url: https://updates.scalr.io/
  - type: MCP Server
    url: https://docs.scalr.io/docs/mcp-server
  - type: Terraform Provider
    url: https://registry.terraform.io/providers/Scalr/scalr/latest/docs
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/scalr/refs/heads/main/vocabulary/scalr-vocabulary.yml
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/scalr/refs/heads/main/json-schema/scalr-workspace-schema.json
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/scalr/refs/heads/main/json-schema/scalr-run-schema.json
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/scalr/refs/heads/main/json-ld/scalr-context.jsonld
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/scalr/refs/heads/main/rules/scalr-rules.yml
  - type: NaftikoCapabilities
    url: https://raw.githubusercontent.com/api-evangelist/scalr/refs/heads/main/capabilities/infrastructure-as-code.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
