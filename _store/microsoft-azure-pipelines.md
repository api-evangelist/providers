---
aid: microsoft-azure-pipelines
url: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-pipelines/refs/heads/main/apis.yml
apis:
- name: Azure Pipelines REST API
  description: REST API for managing and interacting with Azure Pipelines including creating, listing, and getting pipelines, triggering and monitoring pipeline runs, and retrieving pipeline run logs. Provides programmatic access to the core CI/CD pipeline orchestration capabilities in Azure DevOps.
  image: https://azure.microsoft.com/svghandler/devops/?width=600&height=315
  humanURL: https://learn.microsoft.com/en-us/rest/api/azure/devops/pipelines/
  baseURL: https://dev.azure.com/{organization}/{project}/_apis
  tags:
  - CI/CD
  - Pipelines
  - REST
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/rest/api/azure/devops/pipelines/
  - type: OpenAPI
    url: https://dev.azure.com/{organization}/_apis/public/api
  - type: Authentication
    url: https://learn.microsoft.com/en-us/azure/devops/integrate/get-started/authentication/authentication-guidance
  - type: Quickstart
    url: https://learn.microsoft.com/en-us/azure/devops/pipelines/create-first-pipeline
  - type: Client Libraries
    url: https://learn.microsoft.com/en-us/azure/devops/integrate/concepts/dotnet-client-libraries
  - type: Change Log
    url: https://learn.microsoft.com/en-us/azure/devops/release-notes/features-timeline-released
  - type: YAML Schema
    url: https://learn.microsoft.com/en-us/azure/devops/pipelines/yaml-schema/
  contact:
  - type: Support
    url: https://azure.microsoft.com/en-us/support/devops/
  - type: Twitter
    url: https://twitter.com/AzureDevOps
- name: Azure Pipelines Build REST API
  description: REST API for managing build definitions, queuing builds, and retrieving build results, artifacts, tags, and logs. Supports the full lifecycle of continuous integration builds in Azure DevOps, including creating and updating build definitions from templates, listing and tagging builds, and downloading build artifacts.
  image: https://azure.microsoft.com/svghandler/devops/?width=600&height=315
  humanURL: https://learn.microsoft.com/en-us/rest/api/azure/devops/build/
  baseURL: https://dev.azure.com/{organization}/{project}/_apis/build
  tags:
  - Artifacts
  - Build
  - Continuous Integration
  - Definitions
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/rest/api/azure/devops/build/
  - type: Authentication
    url: https://learn.microsoft.com/en-us/azure/devops/integrate/get-started/authentication/authentication-guidance
- name: Azure Pipelines Release REST API
  description: REST API for managing release definitions, creating and tracking releases, and configuring deployment approvals. Enables programmatic control of the continuous delivery process including defining release pipelines with multiple environments, triggering deployments, and managing approval workflows.
  image: https://azure.microsoft.com/svghandler/devops/?width=600&height=315
  humanURL: https://learn.microsoft.com/en-us/rest/api/azure/devops/release/
  baseURL: https://vsrm.dev.azure.com/{organization}/{project}/_apis/release
  tags:
  - Approvals
  - Continuous Delivery
  - Deployment
  - Release
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/rest/api/azure/devops/release/
  - type: Authentication
    url: https://learn.microsoft.com/en-us/azure/devops/integrate/get-started/authentication/authentication-guidance
- name: Azure Pipelines Approvals and Checks REST API
  description: REST API for managing pipeline approvals and checks on resources such as environments, service connections, agent pools, variable groups, and secure files. Provides the ability to create and modify check configurations, manage approval workflows, query check evaluation details, and control pipeline permissions for protected resources.
  image: https://azure.microsoft.com/svghandler/devops/?width=600&height=315
  humanURL: https://learn.microsoft.com/en-us/rest/api/azure/devops/approvalsandchecks/
  baseURL: https://dev.azure.com/{organization}/{project}/_apis/pipelines
  tags:
  - Approvals
  - Checks
  - Governance
  - Security
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/rest/api/azure/devops/approvalsandchecks/
  - type: Authentication
    url: https://learn.microsoft.com/en-us/azure/devops/integrate/get-started/authentication/authentication-guidance
name: Azure Pipelines
tags:
- Automation
- Build
- CI/CD
- Deployment
- DevOps
- Pipelines
type: Contract
image: https://azure.microsoft.com/svghandler/devops/?width=600&height=315
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Azure Pipelines is a cloud service that you can use to automatically build and test your code project and make it available to other users. It works with just about any language or project type.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

