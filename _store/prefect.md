---
aid: prefect
name: Prefect
segments:
  - Workflows
description: Prefect is a Python-native workflow orchestration tool for building, scheduling, and monitoring data pipelines with fault tolerance. Prefect provides a hybrid execution model where the cloud control plane coordinates workflows while code and data remain in customer infrastructure, offering both a managed cloud platform and a self-hosted open-source server.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Automation
  - Data Pipelines
  - Orchestration
  - Python
  - Workflows
created: '2026-03-03'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/prefect/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: prefect:prefect-cloud-rest-api
    name: Prefect Cloud REST API
    description: The Prefect Cloud REST API provides programmatic access to Prefect Cloud for orchestrating and managing workflows, deployments, flow runs, task runs, artifacts, and automations. The API follows RESTful conventions with pluralized collection names, snake_case route names, and supports an OpenAPI 3.0 compliant specification. Clients authenticate using API keys passed as Bearer tokens in request headers.
    humanURL: https://docs.prefect.io/v3/api-ref/rest-api
    tags:
      - Automations
      - Deployments
      - Flow Runs
      - Orchestration
      - REST API
      - Task Runs
      - Workflows
    properties:
      - type: Documentation
        url: https://docs.prefect.io/v3/api-ref/rest-api
      - type: API Reference
        url: https://app.prefect.cloud/api/docs
      - type: Authentication
        url: https://docs.prefect.io/v3/manage/cloud/manage-users/api-keys
      - type: Getting Started
        url: https://docs.prefect.io/v3/get-started/quickstart
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/prefect/refs/heads/main/openapi/prefect-openapi.json
  - aid: prefect:prefect-server-rest-api
    name: Prefect Server REST API
    description: The Prefect Server REST API is the self-hosted variant of the Prefect orchestration API for managing workflows, flow runs, task runs, deployments, and work pools. When running Prefect server locally, the API is available at http://localhost:4200/api and interactive documentation is served at the /docs endpoint. The API can be fully described with an OpenAPI 3.0 compliant document generated from the running server.
    humanURL: https://docs.prefect.io/v3/api-ref/rest-api
    tags:
      - Open Source
      - Orchestration
      - REST API
      - Self-Hosted
      - Workflows
    properties:
      - type: Documentation
        url: https://docs.prefect.io/v3/api-ref/rest-api
      - type: API Reference
        url: https://docs.prefect.io/latest/api-ref/rest-api-reference/
      - type: Getting Started
        url: https://docs.prefect.io/v3/get-started/quickstart
      - type: GitHub Repository
        url: https://github.com/PrefectHQ/prefect
  - aid: prefect:prefect-python-sdk
    name: Prefect Python SDK
    description: The Prefect Python SDK is used to build, test, and execute workflows against the Prefect API. It provides decorators such as @flow and @task for defining workflows, along with programmatic interfaces for deployments, scheduling, state management, concurrency, caching, and retries. The SDK requires Python 3.10 or higher and includes a PrefectClient class for direct interaction with the REST API.
    humanURL: https://docs.prefect.io/v3/api-ref/python
    tags:
      - Orchestration
      - Python
      - SDK
      - Workflows
    properties:
      - type: Documentation
        url: https://docs.prefect.io/v3/api-ref/python
      - type: Getting Started
        url: https://docs.prefect.io/v3/get-started/quickstart
      - type: GitHub Repository
        url: https://github.com/PrefectHQ/prefect
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
common:
  - type: Portal
    url: https://www.prefect.io
  - type: Getting Started
    url: https://docs.prefect.io/v3/get-started/quickstart
  - type: Blog
    url: https://www.prefect.io/blog
  - type: Pricing
    url: https://www.prefect.io/pricing
  - type: Sign Up
    url: https://app.prefect.cloud/
  - type: Support
    url: https://www.prefect.io/support
  - type: Community
    url: https://www.prefect.io/community
  - type: Change Log
    url: https://www.prefect.io/changelog
  - type: Status
    url: https://status.prefect.io/
  - type: Security
    url: https://www.prefect.io/security
  - type: Terms of Service
    url: https://www.prefect.io/legal/terms
  - type: Privacy Policy
    url: https://www.prefect.io/privacy-policy
  - type: GitHub Organization
    url: https://github.com/PrefectHQ
  - type: Integrations
    url: https://docs.prefect.io/integrations/integrations
  - type: Login
    url: https://app.prefect.cloud/
---
