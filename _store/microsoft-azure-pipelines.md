---
name: Azure Pipelines
description: Azure Pipelines is a cloud service that you can use to automatically build and test your code project and make it available to other users. It works with just about any language or project type.
image: https://azure.microsoft.com/svghandler/devops/?width=600&height=315
tags:
  - Automation
  - Build
  - CI/CD
  - Deployment
  - DevOps
  - Pipelines
created: '2024'
modified: '2026-04-28'
specificationVersion: '0.18'
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
common:
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started/what-is-azure-pipelines
  - type: Portal
    url: https://dev.azure.com/
  - type: Pricing
    url: https://azure.microsoft.com/en-us/pricing/details/devops/azure-devops-services/
  - type: Status
    url: https://status.dev.azure.com/
  - type: Blog
    url: https://devblogs.microsoft.com/devops/
  - type: Terms of Service
    url: https://azure.microsoft.com/en-us/support/legal/
  - type: Privacy Policy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/devops/pipelines/
  - type: Website
    url: https://azure.microsoft.com/en-us/products/devops
  - type: Sign Up
    url: https://azure.microsoft.com/en-us/products/devops
  - type: Login
    url: https://dev.azure.com/
  - type: Support
    url: https://azure.microsoft.com/en-us/support/devops/
  - type: Change Log
    url: https://learn.microsoft.com/en-us/azure/devops/release-notes/features-timeline-released
  - type: Client Libraries
    url: https://learn.microsoft.com/en-us/azure/devops/integrate/concepts/dotnet-client-libraries
  - type: Community
    url: https://developercommunity.visualstudio.com/AzureDevOps
  - type: GitHub Organization
    url: https://github.com/MicrosoftDocs
  - type: GitHubRepository
    url: https://github.com/MicrosoftDocs/azure-devops-docs
  - type: Stack Overflow
    url: https://stackoverflow.com/questions/tagged/azure-devops
  - type: Marketplace
    url: https://marketplace.visualstudio.com/azuredevops
  - type: CLI
    url: https://github.com/Azure/azure-devops-cli-extension
  - type: Task Reference
    url: https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/reference/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
endpoints:
  pipelines:
    - name: List Pipelines
      method: GET
      path: /pipelines
      description: Get a list of pipelines
    - name: Get Pipeline
      method: GET
      path: /pipelines/{pipelineId}
      description: Gets a pipeline, optionally at the specified version
    - name: Create Pipeline
      method: POST
      path: /pipelines
      description: Create a pipeline
  runs:
    - name: List Runs
      method: GET
      path: /pipelines/{pipelineId}/runs
      description: Gets top 10000 runs for a particular pipeline
    - name: Get Run
      method: GET
      path: /pipelines/{pipelineId}/runs/{runId}
      description: Gets a run for a particular pipeline
    - name: Run Pipeline
      method: POST
      path: /pipelines/{pipelineId}/runs
      description: Runs a pipeline
  artifacts:
    - name: List Artifacts
      method: GET
      path: /build/builds/{buildId}/artifacts
      description: Get all artifacts for a build
    - name: Get Artifact
      method: GET
      path: /build/builds/{buildId}/artifacts/{artifactName}
      description: Get a specific artifact for a build
  logs:
    - name: Get Log
      method: GET
      path: /pipelines/{pipelineId}/runs/{runId}/logs/{logId}
      description: Get a specific log from a pipeline run
    - name: List Logs
      method: GET
      path: /pipelines/{pipelineId}/runs/{runId}/logs
      description: Get a list of logs from a pipeline run
---
