---
aid: azure-dev-ops
name: Azure DevOps
description: Azure DevOps provides developer services for support teams to plan work, collaborate on code development, and build and deploy applications through a comprehensive set of REST APIs covering builds, releases, Git, pipelines, work items, test management, and artifacts.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Azure
  - CI/CD
  - DevOps
  - Project Management
  - Version Control
url: https://raw.githubusercontent.com/api-evangelist/azure-dev-ops/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: azure-dev-ops:azure-devops-rest-api
    name: Azure DevOps REST API
    description: REST API for Azure DevOps Services and Azure DevOps Server.
    humanURL: https://learn.microsoft.com/en-us/rest/api/azure/devops/
    baseURL: https://dev.azure.com/{organization}
    tags:
      - CI/CD
      - DevOps
      - REST
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/azure/devops/
      - type: Authentication
        url: https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/azure-dev-ops/refs/heads/main/openapi/azure-dev-ops-openapi.yaml
  - aid: azure-dev-ops:azure-devops-pipelines-api
    name: Azure DevOps Pipelines API
    description: API for managing CI/CD pipelines, runs, and pipeline resources.
    humanURL: https://learn.microsoft.com/en-us/rest/api/azure/devops/pipelines/
    baseURL: https://dev.azure.com/{organization}/{project}/_apis/pipelines
    tags:
      - Automation
      - CI/CD
      - Pipelines
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/azure/devops/pipelines/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/azure-dev-ops/refs/heads/main/openapi/azure-dev-ops-openapi.yaml
common:
  - type: Portal
    url: https://dev.azure.com/
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/devops/
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/azure/devops/
  - type: Authentication
    url: https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate
  - type: Status
    url: https://status.dev.azure.com/
  - type: Support
    url: https://azure.microsoft.com/en-us/support/devops/
  - type: Blog
    url: https://devblogs.microsoft.com/devops/
  - type: Terms of Service
    url: https://azure.microsoft.com/en-us/support/legal/
  - type: Privacy Policy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/azure-dev-ops/refs/heads/main/rules/azure-dev-ops-spectral-rules.yml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/azure-dev-ops/refs/heads/main/vocabulary/azure-dev-ops-vocabulary.yaml
  - type: JSONLD
    url: https://raw.githubusercontent.com/api-evangelist/azure-dev-ops/refs/heads/main/json-ld/azure-dev-ops-context.jsonld
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/azure-dev-ops/refs/heads/main/capabilities/azure-dev-ops-management.yaml
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/azure-dev-ops/refs/heads/main/capabilities/shared/azure-dev-ops.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
