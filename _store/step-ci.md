---
aid: step-ci
name: Step CI
description: Step CI is an open source API testing and monitoring framework that uses YAML-based workflows to define and run automated API test scenarios. It supports REST, GraphQL, gRPC, tRPC, and SOAP protocols in a single unified testing framework. Step CI is language-agnostic, self-hosted, and integrates with all major CI/CD platforms.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Testing
  - Functional Testing
  - Testing
  - CI/CD
  - Quality Assurance
  - Automation
  - Open Source
url: https://raw.githubusercontent.com/api-evangelist/step-ci/refs/heads/main/apis.yml
created: '2026-03-25'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: step-ci:step-ci
    name: Step CI
    description: Step CI is an open source API Quality Assurance framework that is language-agnostic and configured using YAML, JSON, or JavaScript. It supports REST, GraphQL, gRPC, tRPC, and SOAP, enabling tests across different API types in a single workflow. The framework is self-hosted and integrates with GitHub Actions, GitLab CI/CD, CircleCI, Jenkins, Azure Pipelines, AWS CodeBuild, and more.
    humanURL: https://stepci.com
    tags:
      - API Testing
      - Functional Testing
      - Testing
      - CI/CD
      - Quality Assurance
      - Open Source
    properties:
      - type: Documentation
        url: https://docs.stepci.com
      - type: GitHub Repository
        url: https://github.com/stepci/stepci
      - type: npm Package
        url: https://www.npmjs.com/package/stepci
      - type: Workflow Syntax
        url: https://docs.stepci.com/reference/workflow-syntax
common:
  - type: Website
    url: https://stepci.com
  - type: Documentation
    url: https://docs.stepci.com
  - type: GitHub Organization
    url: https://github.com/stepci
  - type: Discord
    url: https://discord.gg/KqJJzJ3BTu
  - type: npm
    url: https://www.npmjs.com/package/stepci
features:
  - name: Multi-Protocol Support
    description: Test REST, GraphQL, gRPC, tRPC, SOAP, and SSE APIs in a single workflow
  - name: YAML-Based Workflows
    description: Define test scenarios using readable YAML configuration
  - name: Self-Hosted
    description: Run tests locally, on-network, or in CI/CD environments
  - name: Load Testing
    description: Built-in load testing with configurable phases and performance thresholds
  - name: Contract Testing
    description: Validate API responses against OpenAPI schemas and JSON schemas
  - name: Data Captures
    description: Extract values from responses using JSONPath, XPath, regex, headers, and cookies
  - name: OAuth 2.0 Testing
    description: Built-in OAuth 2.0 authentication flow testing support
  - name: SSL Testing
    description: Certificate validation and SSL configuration testing
  - name: OpenAPI Import
    description: Import OpenAPI specifications to auto-generate test workflows
useCases:
  - name: API Integration Testing
    description: Validate that APIs behave as expected across multiple endpoints and workflows
  - name: Continuous Integration
    description: Run automated API tests in CI/CD pipelines on every commit
  - name: Performance Testing
    description: Load test APIs with configurable ramp-up periods and performance thresholds
  - name: API Monitoring
    description: Continuously monitor API availability and correctness in production
  - name: Contract Testing
    description: Ensure API responses conform to defined schemas and contracts
integrations:
  - name: GitHub Actions
    description: Official GitHub Actions integration for CI/CD pipelines
    url: https://github.com/marketplace/actions/step-ci-action
  - name: GitLab CI/CD
    description: Built-in support for GitLab pipelines
  - name: CircleCI
    description: CircleCI orb for Step CI integration
  - name: Jenkins
    description: Jenkins pipeline step integration
  - name: Azure Pipelines
    description: Azure DevOps pipeline task support
  - name: AWS CodeBuild
    description: AWS CodeBuild integration for serverless CI
  - name: Docker
    description: Official Docker image for containerized testing
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
