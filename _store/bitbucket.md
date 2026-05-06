---
aid: bitbucket
name: Bitbucket
description: Bitbucket is a Git-based source code repository hosting service owned by Atlassian offering both commercial plans and free accounts with unlimited private repositories, along with CI/CD pipelines, code reviews via pull requests, and code collaboration tools for development teams.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Atlassian
  - CI/CD
  - Code Collaboration
  - Code Review
  - DevOps
  - Git
  - Pull Requests
  - Repository Hosting
  - Version Control
url: https://raw.githubusercontent.com/api-evangelist/bitbucket/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-05-04'
specificationVersion: '0.19'
apis:
  - aid: bitbucket:bitbucket-cloud-rest-api
    name: Bitbucket Cloud REST API
    description: The REST API for Bitbucket Cloud allows you to build apps using any language, exposing operations on repositories, pull requests, commits, pipelines, workspaces, projects, webhooks, issues, and users.
    humanURL: https://developer.atlassian.com/bitbucket/api/2/reference/
    baseURL: https://api.bitbucket.org/2.0
    tags:
      - Commits
      - Pipelines
      - Pull Requests
      - Repositories
      - REST
      - Webhooks
      - Workspaces
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/bitbucket/api/2/reference/
      - type: Authentication
        url: https://developer.atlassian.com/cloud/bitbucket/rest/intro/#authentication
      - type: OpenAPI
        url: openapi/bitbucket-cloud-rest-api-openapi.json
      - type: JSONSchema
        url: json-schema/bitbucket-cloud-rest-api-repository-schema.json
      - type: JSONSchema
        url: json-schema/bitbucket-cloud-rest-api-pullrequest-schema.json
      - type: JSONSchema
        url: json-schema/bitbucket-cloud-rest-api-pipeline-schema.json
      - type: JSONSchema
        url: json-schema/bitbucket-cloud-rest-api-commit-schema.json
      - type: JSONStructure
        url: json-structure/bitbucket-cloud-rest-api-repository-structure.json
      - type: JSONStructure
        url: json-structure/bitbucket-cloud-rest-api-pullrequest-structure.json
      - type: JSONStructure
        url: json-structure/bitbucket-cloud-rest-api-pipeline-structure.json
      - type: JSONStructure
        url: json-structure/bitbucket-cloud-rest-api-commit-structure.json
      - type: Example
        url: examples/bitbucket-cloud-rest-api-repository-example.json
      - type: Example
        url: examples/bitbucket-cloud-rest-api-pullrequest-example.json
      - type: Example
        url: examples/bitbucket-cloud-rest-api-pipeline-example.json
      - type: Example
        url: examples/bitbucket-cloud-rest-api-commit-example.json
common:
  - type: Portal
    url: https://developer.atlassian.com/
  - type: StatusPage
    url: https://status.atlassian.com/
  - type: TermsOfService
    url: https://www.atlassian.com/legal/cloud-terms-of-service
  - type: PrivacyPolicy
    url: https://www.atlassian.com/legal/privacy-policy
  - type: SignUp
    url: https://bitbucket.org/account/signup/
  - type: Blog
    url: https://bitbucket.org/blog/
  - type: GitHubOrganization
    url: https://github.com/atlassian
  - type: Support
    url: https://support.atlassian.com/bitbucket-cloud/
  - type: JSON-LD
    url: json-ld/bitbucket-cloud-rest-api-context.jsonld
  - type: SpectralRules
    url: rules/bitbucket-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/code-collaboration.yaml
  - type: Vocabulary
    url: vocabulary/bitbucket-vocabulary.yaml
  - type: Features
    data:
      - 'Free: 5 users, 1 GB, 50 build minutes/mo'
      - 'Standard at $3.65/user/mo: unlimited users/storage, 2,500 build minutes'
      - 'Premium at $7.25/user/mo: 3,500 minutes, AI PR, IP allowlisting, 99.9% SLA'
      - REST API v2 at api.bitbucket.org/2.0
      - 1,000 req/hr per user, 60K req/hr per IP
      - Pipelines for CI/CD
      - 'Pipeline concurrency: 1 Free, 10 Standard, 20 Premium'
      - OAuth 2.0 + repository/workspace access tokens
      - Webhooks for repository, PR, pipeline events
      - Code insights for static analysis integration
      - Self-hosted runners (1 slot Standard, 2 Premium)
      - Deployment environments tracking
      - Native Jira integration
      - Atlassian Marketplace apps
      - Git LFS support (5 GB Standard, 10 GB Premium)
      - Forge / Connect framework for apps
    sources:
      - https://www.atlassian.com/software/bitbucket/pricing
    updated: '2026-05-04'
  - type: UseCases
    data:
      - name: Code Review Workflows
        description: Enforce code quality through structured pull request reviews with required approvals.
      - name: CI/CD Automation
        description: Automate build, test, and deployment pipelines triggered by code changes.
      - name: Team Collaboration
        description: Enable distributed development teams to collaborate on code with workspaces and projects.
      - name: Release Management
        description: Manage releases with deployment tracking and environment promotion.
      - name: Security Scanning
        description: Integrate security scanning into CI/CD pipelines for vulnerability detection.
  - type: Integrations
    data:
      - name: Jira Software
        description: Deep integration with Jira for issue tracking and project management.
      - name: Trello
        description: Connect Bitbucket with Trello for visual project management.
      - name: Slack
        description: Receive Bitbucket notifications in Slack channels.
      - name: Confluence
        description: Link documentation in Confluence with code in Bitbucket.
      - name: AWS
        description: Deploy to AWS services using Bitbucket Pipelines.
      - name: Azure
        description: Deploy to Azure services using Bitbucket Pipelines.
      - name: Google Cloud
        description: Deploy to Google Cloud using Bitbucket Pipelines.
      - name: Docker
        description: Build and push Docker images using Bitbucket Pipelines.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
