---
aid: azure-devops
url: https://raw.githubusercontent.com/api-evangelist/azure-devops/refs/heads/main/apis.yml
apis:
- aid: azure-devops:azure-devops-work-item-tracking-api
  name: Azure DevOps Work Item Tracking API
  tags:
  - Azure
  - CI/CD
  - DevOps
  - Project Management
  - Work Items
  image: https://raw.githubusercontent.com/api-evangelist/azure-devops/refs/heads/main/image.png
  humanURL: https://learn.microsoft.com/en-us/rest/api/azure/devops/
  baseURL: https://dev.azure.com/{organization}
  properties:
  - url: https://learn.microsoft.com/en-us/rest/api/azure/devops/wit/?view=azure-devops-rest-7.2
    type: Reference
  - url: https://learn.microsoft.com/en-us/azure/devops/integrate/how-to/call-rest-api?view=azure-devops
    type: GettingStarted
  - url: https://learn.microsoft.com/en-us/azure/devops/integrate/get-started/authentication/authentication-guidance?view=azure-devops
    type: Authentication
  - url: https://raw.githubusercontent.com/api-evangelist/azure-devops/refs/heads/main/openapi/azure-devops-work-items-openapi.yml
    type: OpenAPI
  description: The Azure DevOps Work Item Tracking API provides REST endpoints for creating, updating, querying, and managing work items including bugs, tasks, user stories, epics, and features across Azure Boards. APIs support custom fields, area paths, iteration paths, and link types for Agile, Scrum, and CMMI process templates.
- aid: azure-devops:azure-devops-git-api
  name: Azure DevOps Git Repositories API
  tags:
  - Azure
  - CI/CD
  - DevOps
  - Git
  - Pull Requests
  - Version Control
  image: https://raw.githubusercontent.com/api-evangelist/azure-devops/refs/heads/main/image.png
  humanURL: https://learn.microsoft.com/en-us/rest/api/azure/devops/
  baseURL: https://dev.azure.com/{organization}
  properties:
  - url: https://learn.microsoft.com/en-us/rest/api/azure/devops/git/?view=azure-devops-rest-7.2
    type: Reference
  - url: https://learn.microsoft.com/en-us/azure/devops/integrate/how-to/call-rest-api?view=azure-devops
    type: GettingStarted
  - url: https://learn.microsoft.com/en-us/azure/devops/integrate/get-started/authentication/authentication-guidance?view=azure-devops
    type: Authentication
  description: The Azure DevOps Git Repositories API provides REST endpoints for managing Git repositories, branches, commits, pull requests, and code reviews. APIs enable automation of repository management, pull request workflows, branch policies, and code review processes within Azure Repos.
- aid: azure-devops:azure-devops-pipelines-api
  name: Azure DevOps Pipelines API
  tags:
  - Azure
  - Build
  - CI/CD
  - DevOps
  - Pipelines
  - Release
  image: https://raw.githubusercontent.com/api-evangelist/azure-devops/refs/heads/main/image.png
  humanURL: https://learn.microsoft.com/en-us/rest/api/azure/devops/
  baseURL: https://dev.azure.com/{organization}
  properties:
  - url: https://learn.microsoft.com/en-us/rest/api/azure/devops/pipelines/?view=azure-devops-rest-7.2
    type: Reference
  - url: https://learn.microsoft.com/en-us/azure/devops/integrate/how-to/call-rest-api?view=azure-devops
    type: GettingStarted
  - url: https://learn.microsoft.com/en-us/azure/devops/integrate/get-started/authentication/authentication-guidance?view=azure-devops
    type: Authentication
  - url: https://raw.githubusercontent.com/api-evangelist/azure-devops/refs/heads/main/openapi/azure-devops-pipelines-openapi.yml
    type: OpenAPI
  description: The Azure DevOps Pipelines API provides REST endpoints for managing CI/CD build and release pipelines. APIs support pipeline creation, triggering builds, retrieving build results, managing release definitions, and automating deployment workflows across Azure DevOps organizations.
- aid: azure-devops:azure-devops-artifacts-api
  name: Azure DevOps Artifacts API
  tags:
  - Artifacts
  - Azure
  - CI/CD
  - DevOps
  - Npm
  - NuGet
  - Package Management
  image: https://raw.githubusercontent.com/api-evangelist/azure-devops/refs/heads/main/image.png
  humanURL: https://learn.microsoft.com/en-us/rest/api/azure/devops/
  baseURL: https://pkgs.dev.azure.com/{organization}
  properties:
  - url: https://learn.microsoft.com/en-us/rest/api/azure/devops/artifacts/?view=azure-devops-rest-7.2
    type: Reference
  - url: https://learn.microsoft.com/en-us/azure/devops/integrate/how-to/call-rest-api?view=azure-devops
    type: GettingStarted
  description: The Azure DevOps Artifacts API provides REST endpoints for managing package feeds including NuGet, npm, Maven, Python, and Universal Packages. APIs support feed creation, package publishing, version management, and upstream source configuration for artifact management in DevOps workflows.
- aid: azure-devops:azure-devops-test-plans-api
  name: Azure DevOps Test Plans API
  tags:
  - Azure
  - CI/CD
  - DevOps
  - Test Plans
  - Testing
  image: https://raw.githubusercontent.com/api-evangelist/azure-devops/refs/heads/main/image.png
  humanURL: https://learn.microsoft.com/en-us/rest/api/azure/devops/
  baseURL: https://dev.azure.com/{organization}
  properties:
  - url: https://learn.microsoft.com/en-us/rest/api/azure/devops/testplan/?view=azure-devops-rest-7.2
    type: Reference
  - url: https://learn.microsoft.com/en-us/azure/devops/integrate/how-to/call-rest-api?view=azure-devops
    type: GettingStarted
  description: The Azure DevOps Test Plans API provides REST endpoints for managing test plans, test suites, test cases, and test runs. APIs support automated test management, test result reporting, and integration with CI/CD pipelines for comprehensive quality assurance workflows.
- aid: azure-devops:azure-devops-release-api
  name: Azure DevOps Release API
  tags:
  - Azure
  - CI/CD
  - Deployment
  - DevOps
  - Release Management
  image: https://raw.githubusercontent.com/api-evangelist/azure-devops/refs/heads/main/image.png
  humanURL: https://learn.microsoft.com/en-us/rest/api/azure/devops/
  baseURL: https://vsrm.dev.azure.com/{organization}
  properties:
  - url: https://learn.microsoft.com/en-us/rest/api/azure/devops/release/?view=azure-devops-rest-7.1
    type: Reference
  - url: https://learn.microsoft.com/en-us/azure/devops/integrate/how-to/call-rest-api?view=azure-devops
    type: GettingStarted
  description: The Azure DevOps Release API provides REST endpoints for managing release pipelines, deployments, and environments. APIs support release definition management, deployment approvals, environment configuration, and release history tracking for continuous delivery workflows.
name: Azure Devops
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Learn the basic patterns for using the REST APIs for Azure DevOps Services and Azure DevOps Server.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

