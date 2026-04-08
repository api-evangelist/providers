---
aid: azure-dev-ops
url: https://raw.githubusercontent.com/api-evangelist/azure-dev-ops/refs/heads/main/apis.yml
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
name: Azure DevOps
tags:
- Azure
- CI/CD
- DevOps
- Project Management
- Version Control
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Azure DevOps provides developer services for support teams to plan work, collaborate on code development, and build and deploy applications through a comprehensive set of REST APIs covering builds, releases, Git, pipelines, work items, test management, and artifacts.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

