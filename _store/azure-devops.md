---
aid: azure-devops
name: Azure DevOps
description: Learn the basic patterns for using the REST APIs for Azure DevOps Services and Azure DevOps Server.
url: https://raw.githubusercontent.com/api-evangelist/azure-devops/refs/heads/main/apis.yml
image: https://raw.githubusercontent.com/api-evangelist/azure-devops/refs/heads/main/image.png
tags:
  - Azure
  - CI/CD
  - DevOps
  - Pipelines
  - Work Items
created: '2024-01-01'
modified: '2026-04-18'
specificationVersion: '0.19'
type: Index
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
        type: APIReference
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
        type: APIReference
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
        type: APIReference
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
        type: APIReference
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
        type: APIReference
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
        type: APIReference
      - url: https://learn.microsoft.com/en-us/azure/devops/integrate/how-to/call-rest-api?view=azure-devops
        type: GettingStarted
    description: The Azure DevOps Release API provides REST endpoints for managing release pipelines, deployments, and environments. APIs support release definition management, deployment approvals, environment configuration, and release history tracking for continuous delivery workflows.
common:
  - url: https://azure.microsoft.com/en-us/products/devops
    type: Documentation
  - url: https://learn.microsoft.com/en-us/rest/api/azure/devops/
    type: Portal
  - url: https://learn.microsoft.com/en-us/rest/api/azure/devops/?view=azure-devops-rest-7.2
    type: APIReference
  - url: https://learn.microsoft.com/en-us/azure/devops/integrate/how-to/call-rest-api?view=azure-devops
    type: GettingStarted
  - url: https://learn.microsoft.com/en-us/azure/devops/integrate/get-started/authentication/authentication-guidance?view=azure-devops
    type: Authentication
  - url: https://learn.microsoft.com/en-us/azure/devops/integrate/concepts/rate-limits?view=azure-devops
    type: RateLimits
  - url: https://learn.microsoft.com/en-us/azure/devops/release-notes/features-timeline-released
    type: ChangeLog
  - url: https://learn.microsoft.com/en-us/azure/devops/dev-resources/?view=azure-devops
    type: Documentation
  - type: Features
    data:
      - name: Work Item Tracking
        description: Create, update, query, and manage work items across Azure Boards
      - name: CI/CD Pipelines
        description: Build, test, and deploy with YAML-based and classic pipelines
      - name: Git Repositories
        description: Host and manage Git repositories with branch policies and pull requests
      - name: Artifacts
        description: Package management for NuGet, npm, Maven, Python, and Universal Packages
      - name: Test Plans
        description: Comprehensive test management with automated and manual testing
      - name: Release Management
        description: Multi-stage deployment pipelines with approval workflows
  - type: UseCases
    data:
      - name: Agile Project Management
        description: Track work items, sprints, and backlogs for Agile development teams
      - name: CI/CD Automation
        description: Automate build, test, and deployment workflows across environments
      - name: Code Review
        description: Enforce branch policies and manage pull request workflows
  - type: Integrations
    data:
      - name: GitHub
        description: Import repositories and trigger pipelines from GitHub events
      - name: Slack
        description: Notifications for pipeline runs and work item updates
      - name: Jira
        description: Bidirectional sync of work items with Jira issues
  - type: GitHubOrganization
    url: https://github.com/microsoft
  - type: SDK
    url: https://github.com/microsoft/azure-devops-node-api
    title: Node.js SDK
  - type: SDK
    url: https://github.com/microsoft/azure-devops-python-api
    title: Python SDK
  - type: SDK
    url: https://github.com/microsoft/azure-devops-go-api
    title: Go SDK
  - type: SDK
    url: https://github.com/microsoft/azure-devops-java-api
    title: Java SDK
  - type: CLI
    url: https://github.com/Azure/azure-devops-cli-extension
    title: Azure DevOps CLI Extension
  - type: OpenAPI
    url: openapi/azure-devops-work-items-openapi.yml
  - type: OpenAPI
    url: openapi/azure-devops-pipelines-openapi.yml
  - type: JSONSchema
    url: json-schema/azure-devops-pipelines-create-pipeline-request-schema.json
    title: Create Pipeline Request Schema
  - type: JSONSchema
    url: json-schema/azure-devops-pipelines-error-schema.json
    title: Pipelines Error Schema
  - type: JSONSchema
    url: json-schema/azure-devops-pipelines-pipeline-run-schema.json
    title: Pipeline Run Schema
  - type: JSONSchema
    url: json-schema/azure-devops-pipelines-pipeline-schema.json
    title: Pipeline Schema
  - type: JSONSchema
    url: json-schema/azure-devops-pipelines-run-pipeline-request-schema.json
    title: Run Pipeline Request Schema
  - type: JSONSchema
    url: json-schema/azure-devops-work-items-error-schema.json
    title: Work Items Error Schema
  - type: JSONSchema
    url: json-schema/azure-devops-work-items-json-patch-operation-schema.json
    title: JSON Patch Operation Schema
  - type: JSONSchema
    url: json-schema/azure-devops-work-items-wiql-result-schema.json
    title: WIQL Result Schema
  - type: JSONSchema
    url: json-schema/azure-devops-work-items-work-item-field-schema.json
    title: Work Item Field Schema
  - type: JSONSchema
    url: json-schema/azure-devops-work-items-work-item-relation-schema.json
    title: Work Item Relation Schema
  - type: JSONSchema
    url: json-schema/azure-devops-work-items-work-item-schema.json
    title: Work Item Schema
  - type: JSONSchema
    url: json-schema/azure-devops-workitem-schema.json
    title: Work Item Schema (Legacy)
  - type: JSONLD
    url: json-ld/azure-devops-context.jsonld
    title: Azure DevOps JSON-LD Context
  - type: JSONLD
    url: json-ld/azure-devops-pipelines-context.jsonld
    title: Pipelines JSON-LD Context
  - type: JSONLD
    url: json-ld/azure-devops-work-items-context.jsonld
    title: Work Items JSON-LD Context
  - type: Vocabulary
    url: vocabulary/azure-devops-vocabulary.yaml
    title: Azure DevOps Vocabulary
  - type: Rules
    url: rules/azure-devops-spectral-rules.yml
    title: Spectral Rules
  - type: Capabilities
    url: capabilities/devops-project-management.yaml
    title: DevOps Project Management Workflow
  - type: Capabilities
    url: capabilities/shared/work-items.yaml
    title: Work Items Shared Capability
  - type: Capabilities
    url: capabilities/shared/pipelines.yaml
    title: Pipelines Shared Capability
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
