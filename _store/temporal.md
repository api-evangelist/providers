---
aid: temporal
name: Temporal
segments:
  - ProCode_API_Composition
  - Workflows
description: Temporal is an open-source durable execution platform for building reliable long-running distributed workflows and microservices.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - ProCode_API_Composition
  - Workflows
created: '2026-03-03'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/temporal/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: temporal:server-frontend-api
    name: Temporal Server Frontend API
    description: The Temporal Server Frontend API provides gRPC services for interacting with the Temporal Server, including WorkflowService for managing workflow executions, OperatorService for cluster operations, and HealthService for health checks. Client SDKs and the Temporal CLI use these gRPC services under the hood.
    humanURL: https://docs.temporal.io/self-hosted-guide/server-frontend-api-reference
    tags:
      - Durable Execution
      - gRPC
      - Workflows
    properties:
      - type: Documentation
        url: https://docs.temporal.io/self-hosted-guide/server-frontend-api-reference
      - type: GitHubRepository
        url: https://github.com/temporalio/api
  - aid: temporal:cloud-ops-api
    name: Temporal Cloud Ops API
    description: The Temporal Cloud Operations API is an open source, public HTTP API and gRPC API for programmatically managing Temporal Cloud control plane resources, including Namespaces, Users, Service Accounts, API keys, and other infrastructure components.
    humanURL: https://docs.temporal.io/ops
    tags:
      - Cloud
      - Operations
      - Workflows
    properties:
      - type: Documentation
        url: https://docs.temporal.io/ops
      - type: APIReference
        url: https://saas-api.tmprl.cloud/docs/httpapi.html
      - type: GitHubRepository
        url: https://github.com/temporalio/cloud-api
      - type: OpenAPI
        url: openapi/cloud-ops-api.yml
common:
  - type: Portal
    url: https://temporal.io/
  - type: Documentation
    url: https://docs.temporal.io/
  - type: GettingStarted
    url: https://docs.temporal.io/cloud/get-started
  - type: Quickstart
    url: https://docs.temporal.io/quickstarts
  - type: SDK
    url: https://docs.temporal.io/develop
  - type: CLI
    url: https://docs.temporal.io/cli
  - type: Pricing
    url: https://temporal.io/pricing
  - type: Blog
    url: https://temporal.io/blog
  - type: ChangeLog
    url: https://temporal.io/change-log
  - type: StatusPage
    url: https://status.temporal.io
  - type: Security
    url: https://temporal.io/security
  - type: TermsOfService
    url: https://temporal.io/terms-of-service
  - type: PrivacyPolicy
    url: https://temporal.io/global-privacy-policy
  - type: Login
    url: https://cloud.temporal.io/login
  - type: SignUp
    url: https://docs.temporal.io/cloud/get-started
  - type: GitHubOrganization
    url: https://github.com/temporalio
  - type: Training
    url: https://learn.temporal.io/
  - type: Features
    data:
      - name: Durable Execution
        description: Automatically persists workflow state and resumes execution after failures, ensuring long-running processes complete reliably.
      - name: Namespace Management
        description: Create and manage isolated namespaces for organizing workflows with independent retention policies and access controls.
      - name: User and Access Management
        description: Manage users, service accounts, and API keys for fine-grained access control to Temporal Cloud resources.
      - name: Multi-Region Deployment
        description: Deploy workflows across multiple cloud regions for low-latency execution and disaster recovery.
      - name: Workflow Versioning
        description: Safely deploy workflow code changes with built-in versioning that prevents breaking running executions.
      - name: Visibility and Search
        description: Query and filter workflow executions using custom search attributes for operational visibility and debugging.
      - name: mTLS Authentication
        description: Secure namespace communication with mutual TLS certificate-based authentication and codec server encryption.
      - name: Async Operations
        description: Track the status of long-running control plane operations like namespace creation and configuration changes.
  - type: UseCases
    data:
      - name: Microservice Orchestration
        description: Coordinate complex multi-service transactions with automatic retries, compensation logic, and timeout handling.
      - name: Data Pipeline Processing
        description: Build reliable ETL and data processing pipelines that handle failures gracefully and resume from the last checkpoint.
      - name: Order Fulfillment Workflows
        description: Automate end-to-end order processing including payment, inventory, shipping, and notification steps with guaranteed completion.
      - name: Infrastructure Provisioning
        description: Orchestrate cloud infrastructure deployment and configuration management with durable state tracking.
      - name: Subscription and Billing Management
        description: Manage recurring billing cycles, subscription renewals, and payment processing with long-running timer-based workflows.
  - type: Integrations
    data:
      - name: Go SDK
        description: Native Go client library for building Temporal workflows and activities with full type safety.
      - name: TypeScript SDK
        description: TypeScript/JavaScript SDK for building Temporal workflows in Node.js with async/await patterns.
      - name: Python SDK
        description: Python SDK for building Temporal workflows with native async support and type hints.
      - name: Java SDK
        description: Java SDK for building Temporal workflows with annotation-based workflow and activity definitions.
      - name: .NET SDK
        description: .NET SDK for building Temporal workflows in C# with strong typing and async patterns.
  - type: NaftikoCapability
    url: capabilities/cloud-operations.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
