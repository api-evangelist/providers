---
aid: terraform
name: Terraform
description: HashiCorp Terraform is an open-source infrastructure-as-code tool that enables teams to define, provision, and manage cloud infrastructure using a declarative configuration language (HCL). HCP Terraform and Terraform Enterprise expose a comprehensive REST API for automating workspace management, runs, state, policies, and access control.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Infrastructure As Code
  - Cloud Infrastructure
  - DevOps
  - Open Source
  - HashiCorp
url: https://raw.githubusercontent.com/api-evangelist/terraform/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: terraform:hcp-terraform-api
    name: HCP Terraform API
    description: The HCP Terraform API provides programmatic access to all HCP Terraform features including workspace management, runs, state versions, policies, teams, organizations, VCS integrations, and the private module registry. The API follows the JSON API specification and uses bearer token authentication.
    humanURL: https://developer.hashicorp.com/terraform/cloud-docs/api-docs
    baseURL: https://app.terraform.io/api/v2
    tags:
      - Infrastructure As Code
      - Workspaces
      - Runs
      - State Management
      - Policy
    properties:
      - url: https://developer.hashicorp.com/terraform/cloud-docs/api-docs
        type: Documentation
      - url: https://developer.hashicorp.com/terraform/cloud-docs/api-docs/workspaces
        type: Documentation
      - url: https://developer.hashicorp.com/terraform/cloud-docs/api-docs/run
        type: Documentation
      - url: https://developer.hashicorp.com/terraform/cloud-docs/api-docs/state-versions
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/terraform/refs/heads/main/openapi/hcp-terraform-openapi.yml
        type: OpenAPI
  - aid: terraform:terraform-registry-api
    name: Terraform Registry API
    description: The Terraform Registry API enables discovery, listing, versioning, and downloading of modules from the public Terraform Registry. It supports searching by keyword, filtering by provider and namespace, and retrieving download metrics.
    humanURL: https://developer.hashicorp.com/terraform/registry/api-docs
    baseURL: https://registry.terraform.io
    tags:
      - Registry
      - Modules
      - Providers
      - Discovery
    properties:
      - url: https://developer.hashicorp.com/terraform/registry/api-docs
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/terraform/refs/heads/main/openapi/terraform-registry-openapi.yml
        type: OpenAPI
common:
  - name: HashiCorp Developer Portal
    url: https://developer.hashicorp.com/terraform
    type: Portal
  - name: Terraform GitHub Organization
    url: https://github.com/hashicorp/terraform
    type: Repository
  - name: Terraform Registry
    url: https://registry.terraform.io
    type: Portal
  - name: HCP Terraform
    url: https://app.terraform.io
    type: Portal
  - name: Terraform Changelog
    url: https://github.com/hashicorp/terraform/blob/main/CHANGELOG.md
    type: ChangeLog
  - name: Terraform Community Forum
    url: https://discuss.hashicorp.com/c/terraform-core
    type: Forum
  - name: Terraform GitHub CLI
    url: https://github.com/hashicorp/terraform
    type: Repository
  - name: Terraform CDK
    url: https://github.com/hashicorp/terraform-cdk
    type: SDK
  - name: Terraform Go SDK
    url: https://github.com/hashicorp/go-tfe
    type: SDK
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
