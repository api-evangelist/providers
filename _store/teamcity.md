---
name: TeamCity
description: JetBrains TeamCity is a powerful continuous integration and deployment server that helps development teams build, test, and deploy software efficiently. TeamCity provides a comprehensive REST API for automating CI/CD workflows, managing projects, build configurations, agents, and infrastructure.
image: https://www.jetbrains.com/teamcity/img/teamcity-logo.svg
url: https://github.com/api-evangelist/teamcity
humanURL: https://www.jetbrains.com/teamcity/
baseURL: https://teamcity.example.com/app/rest
tags:
  - Build Automation
  - CI/CD
  - Continuous Integration
  - Deployment
  - DevOps
  - Testing
created: '2024-01-01'
modified: '2026-04-18'
specificationVersion: '0.18'
type: Index
aid: teamcity
access: 3rd-Party
apis:
  - name: TeamCity REST API
    description: The primary REST API for interacting with TeamCity server, allowing you to manage builds, projects, build configurations, agents, users, VCS roots, changes, tests, investigations, mutes, cloud infrastructure, and more.
    image: https://www.jetbrains.com/teamcity/img/teamcity-logo.svg
    humanURL: https://www.jetbrains.com/help/teamcity/rest-api.html
    baseURL: https://teamcity.example.com/app/rest
    tags:
      - Agents
      - Automation
      - Builds
      - CI/CD
      - Projects
      - REST
      - Testing
    properties:
      - type: Documentation
        url: https://www.jetbrains.com/help/teamcity/rest-api.html
      - type: APIReference
        url: https://www.jetbrains.com/help/teamcity/rest-api-reference.html
      - type: Authentication
        url: https://www.jetbrains.com/help/teamcity/rest-api.html#REST+Authentication
      - type: OpenAPI
        url: openapi/teamcity-rest-api.yml
      - type: JSONSchema
        url: json-schema/teamcity-rest-api.json
      - type: JSONLD
        url: json-ld/teamcity-rest-api.jsonld
    contact:
      - type: Support
        url: https://www.jetbrains.com/support/teamcity/
common:
  - type: GettingStarted
    url: https://www.jetbrains.com/help/teamcity/getting-started-with-teamcity.html
  - type: Documentation
    url: https://www.jetbrains.com/help/teamcity/teamcity-documentation.html
  - type: Pricing
    url: https://www.jetbrains.com/teamcity/buy/
  - type: Blog
    url: https://blog.jetbrains.com/teamcity/
  - type: X
    url: https://twitter.com/teamcity
  - type: GitHubOrganization
    url: https://github.com/JetBrains
  - type: GitHubRepository
    url: https://github.com/JetBrains/teamcity-rest-client
  - type: StatusPage
    url: https://teamcity-support.jetbrains.com/hc/en-us/categories/200595559-Known-Issues
  - type: Marketplace
    url: https://plugins.jetbrains.com/teamcity
  - type: Support
    url: https://www.jetbrains.com/support/teamcity/
  - type: ChangeLog
    url: https://www.jetbrains.com/help/teamcity/what-s-new-in-teamcity.html
  - type: CLI
    url: https://github.com/JetBrains/teamcity-cli
    title: TeamCity CLI
    description: Command-line interface for TeamCity. Manage builds, logs, agents, agent terminals, and queues from the terminal.
  - type: SDK
    url: https://github.com/JetBrains/teamcity-rest-client
    title: TeamCity REST Client (Kotlin)
    description: Official Kotlin client library for the TeamCity REST API.
  - type: SDK
    url: https://github.com/JetBrains/terraform-provider-teamcity
    title: Terraform Provider for TeamCity
    description: Terraform provider to manage TeamCity resources as infrastructure as code.
  - type: Features
    data:
      - name: Build Pipelines
        description: Define multi-stage build pipelines with dependencies and parallel execution.
      - name: Build Chains
        description: Create complex build chains with snapshot and artifact dependencies between configurations.
      - name: Branch Building
        description: Automatically detect and build feature branches from VCS repositories.
      - name: Build Templates
        description: Reusable build configuration templates for standardizing pipeline patterns.
      - name: Personal Builds
        description: Run builds with local code changes before committing to the repository.
      - name: Cloud Agents
        description: Dynamically provision build agents in the cloud for elastic scaling.
      - name: Kotlin DSL Configuration
        description: Define build configurations as code using Kotlin DSL.
      - name: Test History and Flaky Tests
        description: Track test history across builds and automatically detect flaky tests.
      - name: Investigation Management
        description: Assign responsibility for failing builds and tests to team members.
      - name: Build Cache
        description: Cache build dependencies and artifacts for faster subsequent builds.
      - name: Composite Builds
        description: Aggregate results from multiple build configurations into a single view.
      - name: Audit Trail
        description: Complete audit logging of all administrative actions and configuration changes.
  - type: UseCases
    data:
      - name: Continuous Integration
        description: Automatically build and test code on every commit or pull request.
      - name: Continuous Deployment
        description: Deploy applications to staging and production environments automatically.
      - name: Multi-Platform Builds
        description: Build and test across Linux, Windows, and macOS using diverse agent pools.
      - name: Monorepo CI
        description: Manage CI/CD for monorepos with selective triggering based on changed paths.
      - name: Microservices Pipelines
        description: Orchestrate build and deploy pipelines for microservices architectures.
      - name: Release Management
        description: Manage release branches, versioning, and deployment gates.
      - name: Infrastructure as Code Testing
        description: Validate Terraform, Kubernetes, and other IaC configurations in CI pipelines.
      - name: Mobile App CI/CD
        description: Build, test, and distribute mobile applications for iOS and Android.
      - name: Compliance and Audit
        description: Maintain audit trails and enforce build policies for regulatory compliance.
  - type: Integrations
    data:
      - name: GitHub
        description: Pull request building, commit status publishing, and webhook triggers from GitHub.
      - name: GitLab
        description: Integration with GitLab repositories for VCS operations and merge request builds.
      - name: Bitbucket
        description: Bitbucket Cloud and Server integration for source code and pull request builds.
      - name: Docker
        description: Build and push Docker images as part of CI/CD pipelines.
      - name: Kubernetes
        description: Deploy to Kubernetes clusters and use Kubernetes pods as build agents.
      - name: AWS
        description: AWS S3 artifact storage, EC2/ECS cloud agents, and CodeDeploy integration.
      - name: Azure
        description: Azure cloud agents, Azure DevOps integration, and Azure deployment targets.
      - name: Jira
        description: Link builds to Jira issues and track deployments.
      - name: Slack
        description: Build notifications and status updates via Slack channels.
      - name: Terraform
        description: Manage TeamCity infrastructure as code using the official Terraform provider.
      - name: HashiCorp Vault
        description: Secure secrets management integration with HashiCorp Vault.
      - name: SAML SSO
        description: Single sign-on authentication via SAML identity providers like Okta and OneLogin.
      - name: NuGet
        description: NuGet package feed hosting and dependency resolution.
      - name: Maven
        description: Maven build runner and artifact repository integration.
      - name: Gradle
        description: Gradle build runner with build cache and configuration cache support.
      - name: Bazel
        description: Bazel build system support via the TeamCity Bazel plugin.
maintainers:
  - FN: JetBrains
    url: https://www.jetbrains.com
    email: teamcity-support@jetbrains.com
---
