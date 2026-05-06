---
aid: circleci
name: CircleCI
url: https://raw.githubusercontent.com/api-evangelist/circleci/refs/heads/main/apis.yml
created: '2025-03-05'
modified: '2026-05-04'
type: Index
access: 3rd-Party
position: Consumer
specificationVersion: '0.19'
tags:
  - CI/CD
  - Continuous Integration
  - Continuous Deployment
  - DevOps
  - Pipelines
  - Workflows
description: CircleCI is a continuous integration and continuous delivery (CI/CD) platform that automates software build, test, and deployment pipelines. Their developer surface includes the REST API v2 (the recommended modern interface), the legacy v1 REST API, a Self-Hosted Runner API, webhooks for real-time event notifications, and the Orbs Registry of reusable configuration packages. Authentication is via a personal or project Circle-Token sent in the Circle-Token header; responses are JSON.
apis:
  - aid: circleci:rest-api-v2
    name: CircleCI REST API V2
    tags:
      - CI/CD
      - Continuous Integration
      - DevOps
      - Pipelines
      - Workflows
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://circleci.com/api/v2
    humanURL: https://circleci.com/docs/api/v2/
    properties:
      - url: https://circleci.com/docs/api/v2/
        type: Documentation
      - url: openapi/circleci-rest-api-v2-openapi.yml
        type: OpenAPI
    description: The CircleCI REST API v2 provides programmatic access to CircleCI services for managing pipelines, projects, workflows, jobs, and users. Developers can trigger pipelines, retrieve build status, manage contexts and environment variables, and access usage reports. The API uses token-based authentication via a Circle-Token header and returns JSON responses. It supports operations for project configuration, workflow management, artifact retrieval, and insights into build performance.
  - aid: circleci:rest-api-v1
    name: CircleCI REST API V1
    tags:
      - Builds
      - CI/CD
      - Continuous Integration
      - Legacy
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://circleci.com/api/v1.1
    humanURL: https://circleci.com/docs/api/v1/
    properties:
      - url: https://circleci.com/docs/api/v1/
        type: Documentation
      - url: openapi/circleci-rest-api-v1-openapi.yml
        type: OpenAPI
    description: The CircleCI REST API v1 is the legacy API that provides access to build information, project details, and user data. While still available, CircleCI recommends migrating to the v2 API for newer features and improved functionality. The v1 API supports operations for retrieving build details, triggering builds, managing SSH keys, and accessing test metadata. Authentication is handled through API tokens passed as query parameters or HTTP headers.
  - aid: circleci:runner-api
    name: CircleCI Self-Hosted Runner API
    tags:
      - CI/CD
      - Infrastructure
      - Runners
      - Self-Hosted
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://runner.circleci.com
    humanURL: https://circleci.com/docs/runner-api/
    properties:
      - url: https://circleci.com/docs/runner-api/
        type: Documentation
      - url: openapi/circleci-runner-api-openapi.yml
        type: OpenAPI
    description: The CircleCI Self-Hosted Runner API enables management and execution of jobs on self-hosted runner infrastructure. It provides endpoints for listing available runners, managing runner tasks, and querying resource classes. The API is hosted separately from the main CircleCI API at runner.circleci.com and supports multiple authentication methods depending on the endpoint. Developers can use this API to integrate self-hosted runner management into their infrastructure automation workflows.
  - aid: circleci:webhooks
    name: CircleCI Webhooks
    tags:
      - CI/CD
      - Events
      - Notifications
      - Webhooks
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://circleci.com/docs/webhooks/
    properties:
      - url: https://circleci.com/docs/webhooks/
        type: Documentation
      - url: asyncapi/circleci-webhooks-asyncapi.yml
        type: AsyncAPI
    description: CircleCI Webhooks allow developers to receive real-time notifications about events in their CI/CD pipelines by configuring HTTP callbacks. Webhooks can be set up through project settings to notify external services when workflows and jobs complete, fail, or change status. This enables integration with monitoring systems, chat platforms, and custom automation workflows. Webhooks deliver JSON payloads containing event details to configured endpoint URLs.
  - aid: circleci:orbs
    name: CircleCI Orbs Registry
    tags:
      - CI/CD
      - Configuration
      - Packages
      - Reusable
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://circleci.com/developer/orbs
    properties:
      - url: https://circleci.com/developer/orbs
        type: Documentation
    description: CircleCI Orbs are shareable, reusable packages of CircleCI configuration that simplify build setup and integration with third-party tools. The Orbs Registry on the CircleCI Developer Hub provides a searchable catalog of community and certified orbs. Developers can browse, publish, and consume orbs to automate repeated processes, speed up project configuration, and integrate services like AWS, Docker, Slack, and Kubernetes into their CI/CD pipelines.
common:
  - type: Website
    url: https://circleci.com/
  - type: Portal
    url: https://circleci.com/developer
  - type: Documentation
    url: https://circleci.com/docs/
  - type: Status
    url: https://status.circleci.com/
  - type: Support
    url: https://support.circleci.com/
  - type: Blog
    url: https://circleci.com/blog/
  - type: Privacy Policy
    url: https://circleci.com/privacy/
  - type: Terms of Service
    url: https://circleci.com/terms-of-service/
  - type: Login
    url: https://app.circleci.com/
  - type: JSON-LD
    url: json-ld/circleci-context.jsonld
  - type: JSONSchema
    url: json-schema/circleci-pipeline-schema.json
  - type: JSONSchema
    url: json-schema/circleci-workflow-schema.json
  - type: JSONSchema
    url: json-schema/circleci-webhook-event-schema.json
  - type: Spectral
    url: rules/circleci-rules.yml
  - type: Naftiko Capabilities
    url: capabilities/circleci-capabilities.yml
  - type: Features
    data:
      - 'Free: 30K credits/mo, 6K build minutes, 5 active users'
      - 'Performance from $15/mo: 30K credits + $15/25K credits, 80x concurrency'
      - 'Scale: custom annual, 200 GB storage, GPU, SSO, config policies'
      - REST API v2 at circleci.com/api/v2
      - Default 3,000 req/min API rate limit
      - Self-hosted runners (Linux, Windows, macOS, Arm)
      - Docker layer caching (Performance+)
      - Orbs marketplace for reusable config
      - Webhooks for pipeline events
      - OAuth 2.0 + personal API tokens
      - Test splitting and parallel execution
      - GPU executors (Scale)
      - Insights API for build analytics
      - OIDC token federation for cloud auth
      - Config policies for governance (Scale)
      - SOC 2, FedRAMP Moderate (Scale)
    sources:
      - https://circleci.com/pricing/
    updated: '2026-05-04'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
